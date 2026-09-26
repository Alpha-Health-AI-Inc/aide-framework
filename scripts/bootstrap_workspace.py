#!/usr/bin/env python3
"""Prepare a renamed AIDE workspace locally. No network, Git mutations or credentials."""
import argparse
import hashlib
import json
from pathlib import Path

FRAMEWORK = Path(__file__).resolve().parents[1]
RESERVED = {'workspace', 'assets', 'skills', 'templates', 'scripts', 'tests', 'context'}
FOLDERS = {
    'organization': 'Shared organization context and authoritative source links.',
    'people': 'Team-visible roles and selected work. No private personnel records.',
    'products': 'What the team builds and uses, with owners, context and separate access checks.',
    'processes': 'How the team works, including approved procedures and decision routes.',
    'projects': 'Delivery scope, current status and links to authoritative work records.',
    'aides': 'Approved reusable agent definitions and their accountable owners.',
    'roles': 'Operating contracts for verified participants.',
    'teams': 'Team membership, responsibilities and routing.',
    'messages': 'Immutable addressed updates, requests and replies.',
    'receipts': 'Exact-content delivery receipts. Human acceptance is separate.',
    'verifications': 'Sender verification of matching receipts.',
    'operations': 'Setup evidence, continuity and unresolved gates.'
}

def encoded(value):
    return json.dumps(value, indent=2, ensure_ascii=False) + '\n'


def prepare(root, workspace, brief=None):
    root = root.resolve()
    selected = root / workspace
    if selected.is_symlink():
        raise ValueError('Workspace must not be a symlink')
    target = selected.resolve()
    if target.parent != root or target.name.lower() in RESERVED or target.name.startswith('.'):
        raise ValueError('Rename WORKSPACE to a distinct organization workspace folder directly inside this clone')
    marker = target / '.aide-workspace.json'
    if not marker.is_file() or json.loads(marker.read_text()).get('kind') != 'aide-workspace':
        raise ValueError('Workspace marker missing; rename the supplied WORKSPACE folder first')
    if brief is not None:
        if not isinstance(brief, dict):
            raise ValueError('Expected an onboarding brief object')
        if brief.get('kind') != 'aide-onboarding-brief' or brief.get('schema_version') != 1 or brief.get('role') != 'manager':
            raise ValueError('This scaffold accepts a manager brief only; employees join the existing deployment using ONBOARDING.md')
        if brief.get('workspace_mode', 'New organization workspace') != 'New organization workspace':
            raise ValueError('Existing teams must join their existing repository, not bootstrap a second organization')
        if brief.get('workspace_name') != target.name:
            raise ValueError('Brief workspace name does not match the selected folder')
        allowed = {'schema_version','kind','role','workspace_mode','parent_team','name','organization','workspace_name','team','job_title','scope','provider','repository_url','branch','manager','onboarding_url','agent','created_at','status','authority','checks'}
        if set(brief)-allowed or any(not isinstance(v, str) for k,v in brief.items() if k not in {'schema_version','checks'}) or ('checks' in brief and not isinstance(brief['checks'], dict)):
            raise ValueError('Unexpected brief structure')
        if any(len(v) > 4000 for v in brief.values() if isinstance(v,str)):
            raise ValueError('Brief field too long')
    # Do not follow links into unrelated local data, even on a resumed setup.
    if any(p.is_symlink() for p in target.rglob('*')):
        raise ValueError('Workspace contains symlinks; reconcile them before local preparation')
    created = []; preserved = []
    def put(relative, content):
        p = target / relative
        if p.exists():
            if not p.is_file(): raise ValueError('Expected file: ' + relative)
            preserved.append(relative); return
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open('x', encoding='utf-8') as f: f.write(content)
        created.append(relative)
    for folder, explanation in FOLDERS.items():
        put(folder+'/README.md', '# '+folder.title()+'\n\n'+explanation+'\n\nPopulate from authorized sources; missing facts remain pending.\n')
    config = json.loads((root/'templates/workspace/workspace.json').read_text())
    config.update(workspace_name=target.name, organization_id=None, provider=None,
                  repository_url=None, exchange_branch=None, manager_recipient=None,
                  procedure_revision=None, approval_reference=None)
    put('workspace.json', encoded(config))
    if brief is not None:
        put('operations/onboarding-brief.json', encoded(brief))
    if (root/'onboard.html').is_file():
        put('onboard.html', (root/'onboard.html').read_text().replace('href="SETUP.md"','href=".aide-framework/SETUP.md"').replace('href="CLAUDE-PROJECTS.md"','href=".aide-framework/CLAUDE-PROJECTS.md"').replace('context/CORE.md', '.aide-framework/context/CORE.md').replace('context/MANAGER.md', '.aide-framework/context/MANAGER.md').replace('context/EMPLOYEE.md', '.aide-framework/context/EMPLOYEE.md').replace('skills/aide-start-onboarding/SKILL.md', '.aide-framework/skills/aide-start-onboarding/SKILL.md'))
    for registry in ['participants', 'teams']:
        put('registry/'+registry+'.json', encoded({'schema_version':1, 'organization_id':None, registry:[]}))
    state = json.loads((root/'templates/workspace/operations/setup-state.json').read_text())
    state['organization_id']=None
    state['next_action']={'owner':None, 'action':'Agent reads .aide-framework/AGENT-SETUP.md, confirms scope and prepares the manager workspace. Authentication, publication and independent acceptance remain pending.'}
    put('operations/setup-state.json', encoded(state))
    put('.gitignore', '.aide-local/\n.env\n.env.*\n*.pem\n*.key\n.venv/\n__pycache__/\n')
    # Bundle procedures so a later private checkout works independently of this clone.
    source_files = list(root.glob('*.md'))
    if (root/'LICENSE').is_file(): source_files.append(root/'LICENSE')
    for directory in ['assets', 'skills', 'templates', 'context']:
        source_files += [p for p in (root/directory).rglob('*') if p.is_file() and not p.is_symlink() and '__pycache__' not in p.parts and '.venv' not in p.parts]
    manifest = {}
    for source in sorted(source_files):
        relative = str(source.relative_to(root))
        put('.aide-framework/'+relative, source.read_text(encoding='utf-8'))
        actual=(target/'.aide-framework'/relative).read_bytes()
        manifest[relative]=hashlib.sha256(actual).hexdigest()
    put('operations/framework-snapshot.json', encoded({'schema_version':1,'upstream':'https://github.com/Alpha-Health-AI-Inc/aide-framework','files_sha256':manifest,'note':'Local procedure bytes only. Does not certify upstream revision, authorization or installation.'}))
    return {'workspace':str(target),'created':created,'preserved':preserved,'status':'local_scaffold_only','next':'Ask the agent to follow START-HERE.md. No remote, identities, access or bots have been configured.'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace',required=True,help='Renamed folder directly inside this clone, e.g. NEO.CORTEX')
    parser.add_argument('--config',type=Path,help='Optional downloaded manager onboarding JSON brief')
    args=parser.parse_args()
    try:
        result=prepare(FRAMEWORK,args.workspace,json.loads(args.config.read_text()) if args.config else None)
        print(encoded(result))
    except (ValueError,OSError) as exc:
        parser.exit(1,'Preparation stopped: '+str(exc)+'\n')

if __name__=='__main__':main()
