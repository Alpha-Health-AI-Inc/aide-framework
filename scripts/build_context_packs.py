#!/usr/bin/env python3
"""Build small role-specific context packs from canonical runbooks; no network."""
import argparse,hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PACKS={'MANAGER.md':['SETUP.md','AGENT-SETUP.md','EXCHANGE-CONTRACT.md'], 'EMPLOYEE.md':['ONBOARDING.md','EXCHANGE-CONTRACT.md']}
def build(root=ROOT,check=False):
    output=root/'context';output.mkdir(exist_ok=True)
    manifest={'schema_version':1,'measurement':'UTF-8 bytes and whitespace-delimited words. Not token counts or provider capacity.','packs':{}}
    for name,paths in PACKS.items():
        title='Manager setup' if name.startswith('MANAGER') else 'Employee onboarding'
        parts=['# '+title+' context pack','','Generated from the canonical runbooks listed below. Sync this pack and CORE.md; do not also select its source runbooks. Linked references are not included automatically. Read or attach a needed reference before executing its procedure.','']
        source_hashes={}
        for path in paths:
            text=(root/path).read_text();source_hashes[path]=hashlib.sha256(text.encode()).hexdigest()
            text=re.sub(r'\]\((?![a-z]+:|#)([^)]+)\)',lambda m:'](../'+m.group(1)+')',text)
            parts+=['---','','Source: ['+path+'](../'+path+')','',text]
        content='\n'.join(parts)
        target=output/name
        if check:
            if not target.exists() or target.read_text()!=content:raise ValueError('Context pack drift: '+name)
        else:target.write_text(content)
        manifest['packs'][name]={'bytes':len(content.encode()),'words':len(content.split()),'sha256':hashlib.sha256(content.encode()).hexdigest(),'sources':source_hashes}
    core=(output/'CORE.md').read_bytes()
    manifest['packs']['CORE.md']={'bytes':len(core),'words':len(core.decode().split()),'sha256':hashlib.sha256(core).hexdigest(),'sources':{}}
    manifest['launch_files']={}
    for path in ['skills/aide-start-onboarding/SKILL.md','onboard.html']:
        raw=(root/path).read_bytes()
        manifest['launch_files'][path]={'bytes':len(raw),'words':len(raw.decode().split()),'sha256':hashlib.sha256(raw).hexdigest()}
    content=json.dumps(manifest,indent=2)+'\n';target=output/'manifest.json'
    if check:
        if not target.exists() or target.read_text()!=content:raise ValueError('Context manifest drift')
    else:target.write_text(content)
    return manifest
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    try: print(json.dumps(build(check=args.check),indent=2))
    except (ValueError,OSError) as e:p.exit(1,str(e)+'\n')
