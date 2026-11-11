#!/usr/bin/env python3
"""Unit tests for read-only report generators."""
import tempfile
import unittest
from pathlib import Path

from forditas_elokeszito import newest_catalog, prepare
from haladasfigyelo import report


def po(path: Path, pairs: list[tuple[str, str]]) -> None:
    text = 'msgid ""\nmsgstr ""\n\n'
    for source, target in pairs:
        text += f'msgid "{source}"\nmsgstr "{target}"\n\n'
    path.write_text(text, encoding="utf-8")


class BotTests(unittest.TestCase):
    def test_prepare_only_blanks(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "Godot_4_7_2_hu_LEKTORALT_2.po"
            po(path, [("Tree", "Fa"), ("Stone", ""), ("River", "")])
            result = prepare(path, 1)
            self.assertIn("Stone", result)
            self.assertNotIn("River", result)
            self.assertNotIn("**Angol eredeti:**\n\n~~~text\nTree", result)

    def test_progress_and_previous(self):
        with tempfile.TemporaryDirectory() as folder:
            directory = Path(folder)
            earlier = directory / "Godot_4_7_2_hu_LEKTORALT_1.po"
            latest = directory / "Godot_4_7_2_hu_LEKTORALT_2.po"
            po(earlier, [("Tree", ""), ("Stone", "Kő")])
            po(latest, [("Tree", "Fa"), ("Stone", "Kő"), ("River", "")])
            self.assertEqual(newest_catalog(directory), latest)
            result = report(latest)
            self.assertIn("66.7%", result)
            self.assertIn("**2**", result)
            self.assertIn("**1**", result)

    def test_empty_catalog(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "Godot_4_7_2_hu_LEKTORALT_1.po"
            po(path, [])
            self.assertIn("Nincs üres magyar fordítás", prepare(path))
            self.assertIn("A katalógus üres", report(path))


if __name__ == "__main__":
    unittest.main()
