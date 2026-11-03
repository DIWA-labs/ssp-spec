import json
import unittest
from pathlib import Path
import sys

HERE = Path(__file__).resolve()
ROOT = HERE.parents[3]
sys.path.insert(0, str(HERE.parents[1]))

from ssp import SspError, canonical_json, validate_packet

class ReferenceTests(unittest.TestCase):
    def test_valid_examples(self):
        vectors = json.loads((ROOT / "test-vectors/valid/index.json").read_text())
        for vector in vectors:
            packet = json.loads((ROOT / vector["input"]).read_text())
            validate_packet(packet)

    def test_invalid_examples(self):
        base = ROOT / "test-vectors/invalid"
        vectors = json.loads((base / "index.json").read_text())
        for vector in vectors:
            packet = json.loads((base / vector["input"]).read_text())
            with self.assertRaises(SspError) as ctx:
                validate_packet(packet)
            self.assertEqual(vector["error"], ctx.exception.code)

    def test_canonical(self):
        value = json.loads((ROOT / "test-vectors/canonical/input.json").read_text())
        expected = (ROOT / "test-vectors/canonical/expected.json").read_text().strip()
        self.assertEqual(expected, canonical_json(value))

if __name__ == "__main__":
    unittest.main()
