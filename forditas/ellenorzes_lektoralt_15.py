#!/usr/bin/env python3
"""Godot HUN: 15. szakasz, a 39 új F1-súgóbejegyzés ellenőrzése.

A 14. szakasz 2460 fordítása változatlan marad. Megőrizzük a
Godot hivatkozásokat és gettext-ellenőrzéssel vizsgáljuk a PO-fájlt.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from ellenorzes import parse

BASE = Path(__file__).resolve().parent
OLD = BASE / "Godot_4_7_2_hu_LEKTORALT_14.po"
NEW = BASE / "Godot_4_7_2_hu_LEKTORALT_15.po"
TRANSLATIONS = BASE / "lektoralt_15_uj_forditas.json"
OLD_COUNT = 2460
ADDED_COUNT = 39


def main() -> int:
    try:
        old = parse(OLD)
        new = parse(NEW)
        data = json.loads(TRANSLATIONS.read_text(encoding="utf-8"))["translations"]
        extra = set(new) - set(old)
        if len(old) != OLD_COUNT or len(new) != OLD_COUNT + ADDED_COUNT:
            raise ValueError(f"Váratlan méret: előző={len(old)}, aktuális={len(new)}")
        if len(data) != ADDED_COUNT or len(extra) != ADDED_COUNT:
            raise ValueError(f"Váratlan új fordításszám: adat={len(data)}, PO={len(extra)}")
        changes = [k for k, v in old.items() if new.get(k) != v]
        if changes:
            raise ValueError(f"{len(changes)} korábbi fordítás megváltozott")
        content = NEW.read_text(encoding="utf-8")
        checked = set()
        for block in re.split(r"\n\s*\n", content):
            found = re.search(r"(?m)^#\. ([A-Za-z0-9_]+\.[A-Za-z0-9_]+)$", block)
            if not found or found.group(1) not in data:
                continue
            key = found.group(1)
            if key in checked:
                raise ValueError(f"Ismételt súgóazonosító: {key}")
            if f"#: doc/classes/{key.split('.')[0]}.xml" not in block:
                raise ValueError(f"Hibás osztályhivatkozás: {key}")
            translation = re.search(r'(?m)^msgstr ("(?:\\.|[^"\\])*")$', block)
            if not translation:
                raise ValueError(f"Hiányzó msgstr: {key}")
            import ast
            if ast.literal_eval(translation.group(1)) != data[key]:
                raise ValueError(f"Fordítás eltér a tervezettől: {key}")
            checked.add(key)
        if checked != set(data):
            raise ValueError(f"Hiányzó azonosítók: {set(data) - checked}")
        msgfmt = shutil.which("msgfmt")
        if msgfmt is None:
            raise ValueError("A GNU gettext msgfmt nem található")
        with tempfile.TemporaryDirectory(prefix="godot_hu_15_") as tmp:
            subprocess.run([msgfmt, "--check", "-o", str(Path(tmp) / "v15.mo"), str(NEW)], check=True)
        print(f"SIKER: {OLD_COUNT} régi + {ADDED_COUNT} új = {len(new)} fordítás, PO és BBCode rendben.")
        return 0
    except (KeyError, SyntaxError, TypeError, ValueError, OSError, subprocess.CalledProcessError) as ex:
        print(f"HIBA: {ex}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
