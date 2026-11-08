#!/usr/bin/env python3
"""Regressziós próbák a fordításellenőrző hibafelismeréséhez.

Csak ideiglenes, mesterséges mintákat használ; az éles PO-katalógusokat nem módosítja.
"""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ellenorzes import parse


class ForditasEllenorzesProba(unittest.TestCase):
    def parse_sample(self, content):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "minta.po"
            path.write_text(content, encoding="utf-8")
            return parse(path)

    def test_helyes_forditas(self):
        sample = 'msgid "Hello [param name]!"\nmsgstr "Szia [param name]!"\n'
        self.assertEqual(self.parse_sample(sample), {"Hello [param name]!": "Szia [param name]!"})

    def test_ures_forditas_elutasitva(self):
        sample = 'msgid "Hello"\nmsgstr ""\n'
        with self.assertRaisesRegex(ValueError, "hiányzó fordítás"):
            self.parse_sample(sample)

    def test_ismetelt_azonosito_elutasitva(self):
        sample = 'msgid "Hello"\nmsgstr "Szia"\n\nmsgid "Hello"\nmsgstr "Helló"\n'
        with self.assertRaisesRegex(ValueError, "ismétlődő msgid"):
            self.parse_sample(sample)

    def test_hianyzo_sugo_jeloles_elutasitva(self):
        sample = 'msgid "See [method Node2D.move_local_x]."\nmsgstr "Lásd a metódust."\n'
        with self.assertRaisesRegex(ValueError, "súgójelölés-eltérés"):
            self.parse_sample(sample)

    def test_hibas_po_blokk_elutasitva(self):
        sample = 'msgid "Hello"\nmsgstr\n'
        with self.assertRaisesRegex(ValueError, "hibás vagy nem támogatott PO-blokk"):
            self.parse_sample(sample)

    def test_po_fejlec_kimarad(self):
        sample = 'msgid ""\nmsgstr ""\n"Language: hu\\n"\n\nmsgid "Hi"\nmsgstr "Szia"\n'
        self.assertEqual(self.parse_sample(sample), {"Hi": "Szia"})


if __name__ == "__main__":
    unittest.main()
