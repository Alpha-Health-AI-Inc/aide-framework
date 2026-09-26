import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('ci_source', ROOT / 'scripts/ci_source.py')
ci = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ci)

class DocumentationTests(unittest.TestCase):
    def setUp(self):
        self.doc = ci.read_json(ROOT / 'examples/example-export.ci.json')

    def valid(self, **kwargs):
        return ci.validate(self.doc, as_of='2026-09-26', **kwargs)

    def test_fixture_bytes_verified(self):
        self.assertEqual(self.valid(source_root=ROOT / 'examples'), ['export-config'])

    def test_template_does_not_claim_freshness(self):
        doc = ci.read_json(ROOT / 'assets/ci-source.template.json')
        ci.validate(doc, as_of='2026-09-26')
        self.assertEqual(doc['freshness']['status'], 'unknown')

    def test_tampered_source_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            Path(d, 'export-rules.json').write_text('{}')
            with self.assertRaisesRegex(ValueError, 'Source changed'):
                self.valid(source_root=d)

    def test_source_path_escape_rejected(self):
        self.doc['sources'][0]['local_path'] = '../outside.json'
        with self.assertRaisesRegex(ValueError, 'escapes'):
            self.valid(source_root=ROOT / 'examples')

    def test_duplicate_id_rejected(self):
        self.doc['miscellaneous_qa'][0]['id'] = 'csv-export'
        with self.assertRaisesRegex(ValueError, 'Duplicate ID'):
            self.valid()

    def test_duplicate_json_keys_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d, 'bad.json'); p.write_text('{"a":1,"a":2}')
            with self.assertRaisesRegex(ValueError, 'Duplicate JSON key'):
                ci.read_json(p)

    def test_unknown_reference_rejected(self):
        self.doc['topics'][0]['sections'][0]['source_ids'] = ['absent']
        with self.assertRaisesRegex(ValueError, 'Unknown source'):
            self.valid()

    def test_observed_claim_without_evidence_rejected(self):
        self.doc['topics'][0]['sections'][0]['source_ids'] = []
        with self.assertRaisesRegex(ValueError, 'Observed content'):
            self.valid()

    def test_expired_freshness_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Review expired'):
            ci.validate(self.doc, as_of='2026-10-27')

    def test_unversioned_freshness_rejected(self):
        self.doc['sources'][0]['revision'] = None
        self.doc['sources'][0]['content_sha256'] = None
        with self.assertRaisesRegex(ValueError, 'versioned'):
            self.valid()

    def test_impossible_chronology_rejected(self):
        self.doc['sources'][0]['observed_at'] = '2026-09-26T13:00:00Z'
        with self.assertRaisesRegex(ValueError, 'after comparison'):
            self.valid()

    def test_unknown_schema_rejected(self):
        self.doc['schema_version'] = '3.0'
        with self.assertRaises(ValueError): self.valid()

    def test_invalid_calendar_date_rejected(self):
        self.doc['last_reviewed'] = '2026-02-30'
        with self.assertRaises(ValueError): self.valid()

    def test_replacement_cycle_rejected(self):
        section = self.doc['topics'][0]['sections'][0]
        other = copy.deepcopy(section)
        other['id'] = 'new-export'; other['qa'] = []
        other['replaced_by'] = section['id']; section['replaced_by'] = other['id']
        self.doc['topics'][0]['sections'].append(other)
        with self.assertRaisesRegex(ValueError, 'Replacement cycle'):
            self.valid()

    def test_export_preserves_tombstone_scope_and_sources(self):
        self.doc['topics'][0]['sections'][0]['status'] = 'removed'
        records = [json.loads(x) for x in ci.chunks(self.doc, 'fixture-digest').splitlines()]
        section = records[0]
        self.assertEqual(section['content']['status'], 'removed')
        self.assertEqual(section['scope'], self.doc['scope'])
        self.assertEqual(section['sources'][0]['content_sha256'], self.doc['sources'][0]['content_sha256'])
        self.assertEqual(section['authority'], 'reference-only')
        self.assertEqual(section['content']['qa'][0]['evidence_state'], 'observed')

    def test_cli_determinism_overwrite_and_drift(self):
        with tempfile.TemporaryDirectory() as d:
            cmd = [sys.executable, str(ROOT / 'scripts/ci_source.py'), str(ROOT / 'examples/example-export.ci.json'), '--as-of', '2026-09-26', '--out-dir', d]
            def run(*extra): return subprocess.run(cmd + list(extra), capture_output=True, text=True)
            self.assertEqual(run().returncode, 0)
            p = Path(d, 'example-export.md'); original = p.read_bytes()
            self.assertNotEqual(run().returncode, 0)
            self.assertEqual(run('--check').returncode, 0)
            p.write_text('drift')
            self.assertNotEqual(run('--check').returncode, 0)
            self.assertEqual(run('--overwrite').returncode, 0)
            self.assertEqual(p.read_bytes(), original)

if __name__ == '__main__': unittest.main()
