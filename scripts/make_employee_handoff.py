#!/usr/bin/env python3
"""Generate a pasteable employee handoff from a configured local deployment.

No network or credentials. Remote verification and invitations remain separate.
"""
import argparse,json,re
from pathlib import Path
from urllib.parse import urlsplit,quote

def generate(workspace):
    root=Path(workspace)
    required=['JOIN.md','START-HERE.md','workspace.json','registry/participants.json','registry/teams.json','.aide-framework/GIT-FIRST.md','.aide-framework/ONBOARDING.md']
    missing=[p for p in required if not (root/p).is_file()]
    if missing:raise ValueError('Manager setup incomplete: missing deployed root files: '+', '.join(missing)+'. Do not share templates/workspace/JOIN.md.')
    config=json.loads((root/'workspace.json').read_text())
    for k in ['organization_id','repository_url','exchange_branch']:
        value=config.get(k)
        if not isinstance(value,str) or not value.strip() or re.search(r'[<>\r\n]',value):raise ValueError('Unconfigured destination field: '+k)
    url=config['repository_url'].rstrip('/');u=urlsplit(url)
    if u.scheme!='https' or not u.hostname or u.username or u.password or u.query or u.fragment or any(c.isspace() for c in url):raise ValueError('Use a clean HTTPS repository URL without credentials')
    branch=config['exchange_branch']
    if '..' in branch or branch.startswith('-') or re.search(r'[\s~^:?*\[\\]',branch):raise ValueError('Invalid branch')
    for path in ['JOIN.md','START-HERE.md']:
        if re.search(r'<[a-z][a-z0-9_-]*(?:\s[^>]*)?>',(root/path).read_text(),re.I):raise ValueError('Unresolved placeholder in '+path)
    link=url[:-4] if url.endswith('.git') else url
    parts=[x for x in u.path.split('/') if x]
    if u.hostname=='github.com' and len(parts)==2:
        join=link+'/blob/'+quote(branch,safe='')+'/JOIN.md'
    else:join='JOIN.md on the verified '+branch+' branch of '+url
    return f'''Start employee onboarding in this existing workspace: {url}
Branch: {branch}
Employee entry: {join}

Connect me as an employee, not as the workspace creator. Check my actual Git
sign-in and private-repository access first. Help me complete browser/device
sign-in if needed. Do not ask me to choose SSH keys or tokens. If access is
missing, tell me which verified account needs an invitation and pause there.
Use the selected working folder; reuse a matching checkout or clone into a
new subfolder without overwriting work. Do not ask for an existing repo path.
Read root JOIN.md and START-HERE.md, verify my membership and assigned team,
then ask only for missing personal details and assignments. If the root
entries are missing, report incomplete manager setup rather than using
framework templates. Preserve work and verify each completed step.
'''

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--workspace',type=Path,required=True);a=p.parse_args()
    try: print(generate(a.workspace))
    except (ValueError,OSError) as e:p.exit(1,str(e)+'\n')
if __name__=='__main__':main()
