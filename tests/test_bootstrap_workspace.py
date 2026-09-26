"""Local preparation must preserve work and never invent activation."""
import importlib.util,json,shutil,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('bootstrap',ROOT/'scripts/bootstrap_workspace.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class BootstrapTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)/'framework'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('__pycache__','.venv'))
        (self.root/'WORKSPACE').rename(self.root/'TEAM.KNOWLEDGE')
        self.target=self.root/'TEAM.KNOWLEDGE'
    def brief(self):
        return dict(schema_version=1,kind='aide-onboarding-brief',role='manager',workspace_name='TEAM.KNOWLEDGE',name='Example Owner')
    def test_scaffold_stays_pending_and_bundles_context(self):
        result=m.prepare(self.root,'TEAM.KNOWLEDGE',self.brief())
        self.assertEqual(result['status'],'local_scaffold_only')
        config=json.loads((self.target/'workspace.json').read_text())
        self.assertIsNone(config['repository_url']);self.assertIsNone(config['organization_id'])
        self.assertEqual(json.loads((self.target/'registry/participants.json').read_text())['participants'],[])
        for p in ['people','products','processes','projects']: self.assertTrue((self.target/p/'README.md').is_file())
        self.assertTrue((self.target/'.aide-framework/context/CORE.md').is_file())
        self.assertIn('.aide-framework/SETUP.md',(self.target/'onboard.html').read_text())
    def test_private_entry_and_connection_record_remain_honest(self):
        m.prepare(self.root,'TEAM.KNOWLEDGE')
        self.assertIn('.aide-framework/GIT-FIRST.md',(self.target/'CLAUDE.md').read_text())
        self.assertIn('does not grant access',(self.target/'JOIN.md').read_text())
        record=json.loads((self.target/'operations/git-connection.json').read_text())
        self.assertEqual(record['authentication_status'],'not_checked')
        self.assertEqual(record['publication_status'],'not_verified')
        self.assertIsNone(record['authenticated_login'])
        (self.target/'CLAUDE.md').write_text('Existing private instructions')
        record['authentication_status']='verified';record['authenticated_login']='example-user'
        (self.target/'operations/git-connection.json').write_text(json.dumps(record))
        m.prepare(self.root,'TEAM.KNOWLEDGE')
        self.assertEqual((self.target/'CLAUDE.md').read_text(),'Existing private instructions')
        self.assertEqual(json.loads((self.target/'operations/git-connection.json').read_text()),record)
    def test_resume_preserves_actual_work(self):
        m.prepare(self.root,'TEAM.KNOWLEDGE');p=self.target/'workspace.json';p.write_text('{"actual":"keep"}')
        result=m.prepare(self.root,'TEAM.KNOWLEDGE')
        self.assertEqual(p.read_text(),'{"actual":"keep"}');self.assertFalse(result['created'])
    def test_employee_cannot_create_another_org(self):
        brief=self.brief();brief['role']='employee'
        with self.assertRaises(ValueError):m.prepare(self.root,'TEAM.KNOWLEDGE',brief)
        self.assertFalse((self.target/'workspace.json').exists())
    def test_existing_team_cannot_bootstrap_another_org(self):
        brief={**self.brief(), "workspace_mode":"Team in an existing workspace"}
        with self.assertRaises(ValueError):m.prepare(self.root,"TEAM.KNOWLEDGE",brief)
        self.assertFalse((self.target/"workspace.json").exists())
    def test_mismatch_and_bad_structure(self):
        for brief in [[],{**self.brief(),'workspace_name':'OTHER'},{**self.brief(),'name':{'nested':'bad'}}]:
            with self.assertRaises(ValueError):m.prepare(self.root,'TEAM.KNOWLEDGE',brief)
    def test_reserved_and_traversal(self):
        for name in ['WORKSPACE','context','../outside','TEAM.KNOWLEDGE/people']:
            with self.assertRaises(ValueError):m.prepare(self.root,name)
    def test_links_are_rejected(self):
        (self.target/'outside').symlink_to(self.root)
        with self.assertRaises(ValueError):m.prepare(self.root,'TEAM.KNOWLEDGE')
        self.assertFalse((self.target/'workspace.json').exists())
if __name__=='__main__':unittest.main()
