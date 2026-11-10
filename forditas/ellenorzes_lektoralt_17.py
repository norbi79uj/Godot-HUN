#!/usr/bin/env python3
"""Godot HUN 17: 36 új Control F1-súgóbejegyzés és regresszióellenőrzés."""
from __future__ import annotations

import ast
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from ellenorzes import parse

DIR = Path(__file__).resolve().parent
OLD = DIR / "Godot_4_7_2_hu_LEKTORALT_16.po"
NEW = DIR / "Godot_4_7_2_hu_LEKTORALT_17.po"
EXPECTED_PREVIOUS = 2575
EXPECTED_ADDITIONS = 36

def main() -> int:
    try:
        previous, current = parse(OLD), parse(NEW)
        additions = set(current) - set(previous)
        if len(previous) != EXPECTED_PREVIOUS:
            raise ValueError(f"Korábbi bejegyzések száma: {len(previous)}")
        if len(current) != EXPECTED_PREVIOUS + EXPECTED_ADDITIONS:
            raise ValueError(f"Új bejegyzések száma: {len(current)}")
        if len(additions) != EXPECTED_ADDITIONS:
            raise ValueError(f"Új msgid-k száma: {len(additions)}")
        changed = [key for key, val in previous.items() if current.get(key) != val]
        if changed:
            raise ValueError(f"{len(changed)} korábbi fordítás változott!")
        all_blocks = NEW.read_text(encoding="utf-8").split("\n\n")
        found = set()
        for block in all_blocks:
            m = re.search(r"(?m)^#\. (Control\.[A-Za-z_0-9]+)$", block)
            if not m or "#: doc/classes/Control.xml" not in block:
                continue
            id_match = re.search(r'(?m)^msgid ("(?:\\.|[^"\\])*")$', block)
            str_match = re.search(r'(?m)^msgstr ("(?:\\.|[^"\\])*")$', block)
            if not id_match or not str_match:
                raise ValueError(f"Hiányos PO-bejegyzés: {m.group(1)}")
            original = ast.literal_eval(id_match.group(1))
            translated = ast.literal_eval(str_match.group(1))
            if original not in additions:
                continue
            if original in found:
                raise ValueError(f"Ismétlődő msgid: {m.group(1)}")
            if translated != current[original]:
                raise ValueError(f"Eltérő szöveg: {m.group(1)}")
            tags = lambda s: sorted(re.findall(r"\[[^\]]+\]", s))
            if tags(original) != tags(translated):
                raise ValueError(f"Eltérő Godot-hivatkozások: {m.group(1)}")
            found.add(original)
        if found != additions:
            raise ValueError(f"{len(additions)-len(found)} új Control bejegyzés hiányzik")
        compiler = shutil.which("msgfmt")
        if compiler is None:
            raise ValueError("A msgfmt nem érhető el")
        with tempfile.TemporaryDirectory() as folder:
            subprocess.run([compiler, "--check", "-o", str(Path(folder) / "v17.mo"), str(NEW)], check=True)
        print(f"SIKER: {len(previous)} megtartott + {len(additions)} új = "
              f"{len(current)} F1-bejegyzés, hivatkozások és gettext rendben.")
        return 0
    except (ValueError, TypeError, SyntaxError, OSError, subprocess.CalledProcessError) as exc:
        print(f"HIBA: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
