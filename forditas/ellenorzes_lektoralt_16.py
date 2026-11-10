#!/usr/bin/env python3
"""Godot HUN – 16. fordítási szakasz (76 új F1-bejegyzés) ellenőrzése.

Nem módosítja a fordításokat. Ellenőrzi a 15. szakasz megtartását,
az új osztályazonosítókat, az XML-forrásmegjelöléseket, a Godot
súgójelöléseit és a PO gettext-kompatibilitását.
"""
from __future__ import annotations

import ast
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from ellenorzes import parse

ROOT = Path(__file__).resolve().parent
PREVIOUS = ROOT / "Godot_4_7_2_hu_LEKTORALT_15.po"
CURRENT = ROOT / "Godot_4_7_2_hu_LEKTORALT_16.po"
SOURCE = ROOT / "lektoralt_16_uj_forditas.json"
EXPECTED_OLD = 2499
EXPECTED_NEW = 76

def main() -> int:
    try:
        previous = parse(PREVIOUS)
        current = parse(CURRENT)
        planned = json.loads(SOURCE.read_text(encoding="utf-8"))["translations"]
        additions = set(current) - set(previous)

        if len(previous) != EXPECTED_OLD:
            raise ValueError(f"Korábbi bejegyzések száma: {len(previous)}")
        if len(planned) != EXPECTED_NEW or len(additions) != EXPECTED_NEW:
            raise ValueError(f"Új bejegyzések száma: terv={len(planned)}, katalógus={len(additions)}")
        if len(current) != EXPECTED_OLD + EXPECTED_NEW:
            raise ValueError(f"Új katalógus mérete: {len(current)}")

        modified = [k for k, v in previous.items() if current.get(k) != v]
        if modified:
            raise ValueError(f"{len(modified)} korábbi fordítás módosult")

        seen = set()
        for block in re.split(r"\n\s*\n", CURRENT.read_text(encoding="utf-8")):
            match = re.search(r"(?m)^#\. ([A-Za-z0-9_]+\.[A-Za-z0-9_]+)$", block)
            if match is None or match.group(1) not in planned:
                continue
            name = match.group(1)
            if name in seen:
                raise ValueError(f"Ismétlődő hivatkozás: {name}")
            if f"#: doc/classes/{name.split('.')[0]}.xml" not in block:
                raise ValueError(f"Érvénytelen osztály-forrás: {name}")
            msg = re.search(r'(?m)^msgid ("(?:\\.|[^"\\])*")$', block)
            val = re.search(r'(?m)^msgstr ("(?:\\.|[^"\\])*")$', block)
            if msg is None or val is None:
                raise ValueError(f"Hiányos PO-bejegyzés: {name}")
            original = ast.literal_eval(msg.group(1))
            translated = ast.literal_eval(val.group(1))
            if original not in additions or translated != planned[name] or current[original] != translated:
                raise ValueError(f"Eltérő vagy nem új fordítás: {name}")
            seen.add(name)
        if seen != set(planned):
            raise ValueError(f"Hiányzó osztályazonosítók: {set(planned) - seen}")

        msgfmt = shutil.which("msgfmt")
        if not msgfmt:
            raise ValueError("GNU gettext msgfmt nem található")
        with tempfile.TemporaryDirectory(prefix="godot_hun_16_") as temp:
            subprocess.run(
                [msgfmt, "--check", "-o", str(Path(temp) / "v16.mo"), str(CURRENT)],
                check=True,
            )
        print(f"SIKER: {len(previous)} megtartott + {len(additions)} új = "
              f"{len(current)} magyar F1-bejegyzés; Godot-hivatkozások és msgfmt rendben.")
        return 0
    except (ValueError, SyntaxError, TypeError, KeyError, OSError,
            subprocess.CalledProcessError) as exc:
        print(f"HIBA: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
