import importlib.util,json,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('handoff',ROOT/'scripts/make_employee_handoff.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class HandoffTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
  for path in ['JOIN.md','START-HERE.md','registry/participants.json','registry/teams.json','.aide-framework/GIT-FIRST.md','.aide-framework/ONBOARDING.md']:
   p=self.root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text('Configured example')
  self.config={'organization_id':'example','repository_url':'https://github.com/example/team-space','exchange_branch':'team/pilot'};self.save()
 def save(self):(self.root/'workspace.json').write_text(json.dumps(self.config))
 def test_person_gets_action_and_deployed_link(self):
  out=m.generate(self.root);self.assertIn('/blob/team%2Fpilot/JOIN.md',out);self.assertIn('Start employee onboarding',out);self.assertNotIn('templates/workspace',out)
 def test_template_only_not_accepted(self):
  (self.root/'JOIN.md').unlink();p=self.root/'templates/workspace/JOIN.md';p.parent.mkdir(parents=True);p.write_text('template')
  with self.assertRaisesRegex(ValueError,'Manager setup incomplete'):m.generate(self.root)
 def test_unconfigured_destination_blocked(self):
  self.config['organization_id']='<organization-id>';self.save()
  with self.assertRaises(ValueError):m.generate(self.root)
 def test_credentials_not_exported(self):
  self.config['repository_url']='https://secret@example.com/team/repo';self.save()
  with self.assertRaises(ValueError):m.generate(self.root)
 def test_startup_template_not_accepted(self):
  (self.root/'START-HERE.md').write_text('Organization: <organization-id>')
  with self.assertRaises(ValueError):m.generate(self.root)
if __name__=='__main__':unittest.main()
