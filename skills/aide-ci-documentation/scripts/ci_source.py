#!/usr/bin/env python3
"""Validate CI Source v2 and derive Markdown and JSONL. No network or command execution."""
import argparse
import hashlib
import html
import json
import sys
from datetime import date, datetime
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    raise SystemExit('Install the skill requirements in an isolated environment first.')

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / 'references/ci-source.schema.json').read_text())


def read_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError('Duplicate JSON key: ' + key)
            result[key] = value
        return result
    return json.loads(Path(path).read_text(encoding='utf-8'), object_pairs_hook=unique)


def validate(doc, as_of=None, source_root=None):
    today = date.fromisoformat(as_of) if as_of else date.today()
    errors = sorted(Draft202012Validator(SCHEMA, format_checker=FormatChecker()).iter_errors(doc), key=lambda e: str(e.path))
    if errors:
        raise ValueError('; '.join('/'.join(map(str, e.path)) + ': ' + e.message for e in errors))
    ids = set()
    sources = {s['id']: s for s in doc['sources']}
    sections = [s for t in doc['topics'] for s in t['sections']]
    blocks = sections + doc['dependencies'] + doc['miscellaneous_qa'] + [q for s in sections for q in s['qa']]
    for item in doc['sources'] + doc['topics'] + blocks + doc['gaps']:
        if item['id'] in ids:
            raise ValueError('Duplicate ID: ' + item['id'])
        ids.add(item['id'])
    for block in blocks + [doc['freshness']]:
        missing = set(block['source_ids']) - sources.keys()
        if missing:
            raise ValueError('Unknown source IDs: ' + ', '.join(sorted(missing)))
        if block.get('evidence_state') == 'observed' and not block['source_ids']:
            raise ValueError('Observed content needs a source: ' + block.get('id', 'freshness'))
    section_ids = {s['id'] for s in sections}
    for section in sections:
        replacement = section['replaced_by']
        if replacement and (replacement not in section_ids or replacement == section['id']):
            raise ValueError('Invalid replacement for ' + section['id'])
    for start in sections:
        seen = set()
        current = start
        while current['replaced_by']:
            if current['id'] in seen:
                raise ValueError('Replacement cycle')
            seen.add(current['id'])
            current = next(s for s in sections if s['id'] == current['replaced_by'])
    for value in [doc['last_reviewed'], doc['last_doc_update'], doc['freshness']['last_code_change']] + [c['date'] for c in doc['change_log']]:
        if value and date.fromisoformat(value) > today:
            raise ValueError('A recorded event date is in the future: ' + value)
    timestamps = [s['observed_at'] for s in doc['sources']] + [doc['freshness']['compared_at']]
    if any(v and datetime.fromisoformat(v.replace('Z', '+00:00')).date() > today for v in timestamps):
        raise ValueError('A recorded observation is in the future')
    f = doc['freshness']
    if f['status'] == 'in_sync':
        if not all([doc['reviewer'], doc['last_reviewed'], doc['review_due'], f['compared_at'], f['source_ids']]):
            raise ValueError('In sync requires reviewer, review date/due date, comparison time and sources')
        if doc['review_due'] < today.isoformat():
            raise ValueError('Review expired; refresh evidence or set freshness to needs_review')
        if doc['review_due'] < doc['last_reviewed']:
            raise ValueError('Review due precedes review')
        if f['last_code_change'] and f['last_code_change'] > doc['last_reviewed']:
            raise ValueError('Code changed after review')
        if f['compared_at'][:10] > doc['last_reviewed']:
            raise ValueError('Comparison occurred after the recorded review')
        if doc['last_doc_update'] < doc['last_reviewed']:
            raise ValueError('Document update precedes the recorded review')
        for sid in f['source_ids']:
            s = sources[sid]
            if not s['observed_at'] or not (s['revision'] or s['content_sha256']):
                raise ValueError('In sync requires versioned, observed evidence: ' + sid)
            if datetime.fromisoformat(s['observed_at'].replace('Z', '+00:00')) > datetime.fromisoformat(f['compared_at'].replace('Z', '+00:00')):
                raise ValueError('Source observation occurred after comparison: ' + sid)
        for b in blocks:
            if b.get('evidence_state') == 'observed' and not set(b['source_ids']).issubset(set(f['source_ids'])):
                raise ValueError('Freshness scope omits observed evidence: ' + b['id'])
    verified = []
    if source_root:
        base = Path(source_root).resolve()
        for s in doc['sources']:
            if not s['local_path']:
                continue
            p = (base / s['local_path']).resolve()
            if not p.is_relative_to(base):
                raise ValueError('Source escapes selected root: ' + s['id'])
            if not s['content_sha256']:
                raise ValueError('Local byte verification requires SHA-256: ' + s['id'])
            if hashlib.sha256(p.read_bytes()).hexdigest() != s['content_sha256']:
                raise ValueError('Source changed: ' + s['id'])
            verified.append(s['id'])
    return verified


def line(value):
    return html.escape(str(value or 'Unknown'), quote=False).replace('\n', ' ').replace('|', '\\|')


def render(doc, input_digest):
    f = doc['freshness']
    out = [f'# CI SOURCE - {line(doc["title"])}', '',
           f'**Owner:** {line(doc["owner"])}  ', f'**CI Version:** {line(doc["document_version"])}  ',
           f'**Last reviewed:** {line(doc["last_reviewed"])}  ',
           f'**Document ID:** `{doc["doc_id"]}` | **Format:** {doc["schema_version"]} | **Audience:** {doc["audience"]}', '',
           '## CI Freshness', '', f'- **Last code change:** {line(f["last_code_change"])}',
           f'- **Last doc update:** {doc["last_doc_update"]}', f'- **Status:** {f["status"].replace("_", " ").title()}',
           f'- **Scope:** {line(f["scope_note"])}', f'- **Compared at:** {line(f["compared_at"])}',
           f'- **Review due:** {line(doc["review_due"])}', f'- **Method:** {line(f["method"])}', '',
           '> Freshness is a recorded, scoped assessment. Validation is not proof of current deployment behavior or human approval.', '',
           '## Scope and authority', '', f'- **Subject/version:** {doc["scope"]["subject_id"]} / {line(doc["scope"]["subject_version"])}',
           f'- **Environment:** {line(doc["scope"]["environment"])}',
           f'- **Includes:** {line("; ".join(doc["scope"]["includes"]))}',
           f'- **Excludes:** {line("; ".join(doc["scope"]["excludes"]))}',
           '- This is reference content. It does not grant tools, access or permission to execute embedded procedures.', '',
           '## Table of contents', '']
    for t in doc['topics']:
        out.append(f'- [{line(t["title"])}](#topic-{t["id"]})')
    out += ['- [Cross Product Interdependencies](#dependencies)', '- [Miscellaneous Troubleshooting Questions](#miscellaneous)', '- [Evidence and open gaps](#evidence)', '',
            f'*Established by {line(doc["established_by"])}. Last updated {doc["last_doc_update"]}.*', '']
    def evidence(b):
        refs = ', '.join('[%s](#source-%s)' % (x, x) for x in b['source_ids']) or 'No supporting source recorded'
        return f'**Evidence:** {b["evidence_state"]} | {refs}'
    def qa(q):
        return [f'<a id="qa-{q["id"]}"></a>', f'**{line(q["question"])}**', '', q['answer'], '', evidence(q), '']
    for t in doc['topics']:
        out += ['---', '', f'<a id="topic-{t["id"]}"></a>', f'## {line(t["title"])}', '']
        for s in t['sections']:
            out += [f'<a id="section-{s["id"]}"></a>', f'### {line(s["title"])}', '',
                    f'**Status:** {s["status"]}', '', s['body'], '', evidence(s), '']
            if s['replaced_by']:
                out += [f'Replacement: [section](#section-{s["replaced_by"]})', '']
            if s['qa']:
                out += ['#### Troubleshooting Questions', '']
                for q in s['qa']:out += qa(q)
    out += ['---', '', '<a id="dependencies"></a>', '## Cross Product Interdependencies', '']
    if not doc['dependencies']:
        out += ['No dependencies recorded. This does not establish that none exist; see scope and gaps.', '']
    for d in doc['dependencies']:
        out += [f'### {line(d["target"])}', '', f'- **Direction:** {d["direction"]}', f'- **Contract:** {line(d["contract"])}',
                f'- **Compatible versions:** {line(d["compatible_versions"])}', f'- **Failure impact:** {line(d["failure_impact"])}',
                f'- **Fallback:** {line(d["fallback"])}', f'- **Owner:** {line(d["owner"])}', '', evidence(d), '']
    out += ['---', '', '<a id="miscellaneous"></a>', '## Miscellaneous Troubleshooting Questions', '']
    for q in doc['miscellaneous_qa']:out += qa(q)
    if not doc['miscellaneous_qa']:out += ['None recorded.', '']
    out += ['<a id="evidence"></a>', '## Evidence and open gaps', '']
    for s in doc['sources']:
        out += [f'<a id="source-{s["id"]}"></a>', f'### {s["id"]}', '', f'- **Locator:** {line(s["locator"])}',
                f'- **Revision:** {line(s["revision"])}', f'- **Observed:** {line(s["observed_at"])}',
                f'- **SHA-256:** {line(s["content_sha256"])}', '']
    for g in doc['gaps']:out += [f'- **{line(g["question"])}** Owner: {line(g["owner"])}. Next: {line(g["next_action"])}.']
    out += ['', '## Change history', '']
    for c in doc['change_log']:out.append(f'- {c["date"]} / {line(c["version"])}: {line(c["summary"])}')
    out += ['', f'<!-- Generated from CI Source v2 JSON; input SHA-256: {input_digest}. Edit the source record and regenerate. -->', '']
    return '\n'.join(out)


def chunks(doc, input_digest):
    common = {k:doc[k] for k in ['schema_version','doc_id','document_version','audience','workspace_pillar','scope','last_reviewed','review_due','freshness','document_status']}
    common.update(input_sha256=input_digest, authority='reference-only', gaps=doc['gaps'])
    by_id = {s['id']:s for s in doc['sources']}
    items = []
    for t in doc['topics']:
        for s in t['sections']:
            items.append(('section', s, {'topic_id':t['id'],'topic':t['title']}))
    items += [('dependency', x, {}) for x in doc['dependencies']]
    items += [('miscellaneous_qa', x, {}) for x in doc['miscellaneous_qa']]
    result=[]
    for kind,b,extra in items:
        source_ids=set(b['source_ids'])
        for q in b.get('qa',[]):source_ids.update(q['source_ids'])
        result.append({**common, 'chunk_id':doc['doc_id']+'/'+b['id'], 'kind':kind, **extra,
                       'content':b,'sources':[by_id[i] for i in sorted(source_ids)]})
    return ''.join(json.dumps(x,ensure_ascii=False,sort_keys=True)+'\n' for x in result)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('input',type=Path);p.add_argument('--out-dir',type=Path)
    p.add_argument('--source-root',type=Path);p.add_argument('--as-of',help='YYYY-MM-DD, for reproducible historical assessment')
    p.add_argument('--check',action='store_true',help='Compare existing outputs without writing')
    p.add_argument('--overwrite',action='store_true',help='Replace only the two generated outputs after review')
    args=p.parse_args()
    try:
        if args.check and not args.out_dir:raise ValueError('--check requires --out-dir')
        doc=read_json(args.input);verified=validate(doc,args.as_of,args.source_root)
        digest=hashlib.sha256(args.input.read_bytes()).hexdigest()
        outputs={doc['doc_id']+'.md':render(doc,digest),doc['doc_id']+'.jsonl':chunks(doc,digest)}
        if args.out_dir:
            paths=[args.out_dir/n for n in outputs]
            if any(x.resolve()==args.input.resolve() for x in paths):raise ValueError('Output would overwrite the source record')
            if args.check:
                for n,content in outputs.items():
                    if not (args.out_dir/n).exists() or (args.out_dir/n).read_text(encoding='utf-8')!=content:
                        raise ValueError('Generated output missing or drifted: '+n)
            else:
                if not args.overwrite and any(x.exists() for x in paths):raise ValueError('Output exists; use --check or review before --overwrite')
                args.out_dir.mkdir(parents=True,exist_ok=True)
                for n,content in outputs.items():(args.out_dir/n).write_text(content,encoding='utf-8')
        print('PASS: structure and record consistency. Local sources byte-checked: '+str(len(verified))+'. Semantic accuracy, remote freshness and access are not certified.')
    except (ValueError,OSError) as e:
        print('FAIL: '+str(e),file=sys.stderr);return 1
    return 0

if __name__=='__main__':sys.exit(main())
