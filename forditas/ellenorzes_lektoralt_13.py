#!/usr/bin/env python3
"""A 13. Godot-HUN F1-fordítási szakasz ellenőrzése.

Megőrzi a 12. szakasz összes szövegét, és ellenőrzi a 86 új fordítást,
a PO-szerkezetet, Godot-hivatkozásokat és a gettext-fordíthatóságot.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from ellenorzes import parse

ROOT = Path(__file__).resolve().parent
OLD = ROOT / "Godot_4_7_2_hu_LEKTORALT_12.po"
NEW = ROOT / "Godot_4_7_2_hu_LEKTORALT_13.po"
NEW_TRANSLATIONS = ROOT / "lektoralt_13_uj_forditas.json"
COUNT = 86


def main() -> int:
    try:
        old, new = parse(OLD), parse(NEW)
        details = json.loads(NEW_TRANSLATIONS.read_text(encoding="utf-8"))
        translations = details["translations"]
        if len(old) != 2308 or len(new) != len(old) + COUNT:
            raise ValueError(f"Váratlan bejegyzésszám: 12={len(old)}, 13={len(new)}")
        if len(translations) != COUNT:
            raise ValueError(f"A forrásfordítások száma eltér: {len(translations)}")
        changes = [key for key in old if new.get(key) != old[key]]
        if changes:
            raise ValueError(f"{len(changes)} korábbi fordítás megváltozott!")
        additions = set(new).difference(old)
        if len(additions) != COUNT:
            raise ValueError(f"Új fordítások száma: {len(additions)}")
        content = NEW.read_text(encoding="utf-8")
        for name, translated in translations.items():
            if f"#. {name}\n" not in content:
                raise ValueError(f"Hiányzó Godot-osztályhivatkozás: {name}")
            if translated not in (new[key] for key in additions):
                raise ValueError(f"Hiányzó magyar fordítás: {name}")
        msgfmt = shutil.which("msgfmt")
        if not msgfmt:
            raise ValueError("A GNU gettext msgfmt nem található.")
        with tempfile.TemporaryDirectory(prefix="godot_hu_v13_") as temp:
            subprocess.run(
                [msgfmt, "--check", "-o", str(Path(temp) / "v13.mo"), str(NEW)],
                check=True,
            )
        print(f"SIKER: {len(old)} korábbi + {len(additions)} új = {len(new)} "
              "Godot F1-bejegyzés; jelölések, duplikációk és msgfmt rendben.")
        return 0
    except (KeyError, TypeError, OSError, ValueError, SyntaxError,
            subprocess.CalledProcessError) as exc:
        print(f"HIBA: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
