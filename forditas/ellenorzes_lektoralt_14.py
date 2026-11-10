#!/usr/bin/env python3
"""Godot HUN – a RichTextLabel súgó 14. fordítási szakaszának ellenőrzése.

A teljes korábbi 2394 bejegyzésnek változatlanul meg kell maradnia;
a 66 új fordítás jelöléseinek, szerkezetének és gettext-kimenetének helyesnek kell lennie.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from ellenorzes import parse

HERE = Path(__file__).resolve().parent
OLD = HERE / "Godot_4_7_2_hu_LEKTORALT_13.po"
NEW = HERE / "Godot_4_7_2_hu_LEKTORALT_14.po"
TRANSLATIONS = HERE / "lektoralt_14_uj_forditas.json"
EXPECTED_OLD = 2394
EXPECTED_ADDED = 66


def main() -> int:
    try:
        old = parse(OLD)
        new = parse(NEW)
        additions = set(new) - set(old)
        translations = json.loads(TRANSLATIONS.read_text(encoding="utf-8"))["translations"]
        if len(old) != EXPECTED_OLD or len(additions) != EXPECTED_ADDED:
            raise ValueError(f"Eltérő bejegyzésszám: régi={len(old)}, új={len(additions)}")
        if len(new) != EXPECTED_OLD + EXPECTED_ADDED:
            raise ValueError(f"Váratlan új katalógusméret: {len(new)}")
        if len(translations) != EXPECTED_ADDED:
            raise ValueError(f"Eltérő fordítási tervezet: {len(translations)}")
        changed = [key for key, value in old.items() if new.get(key) != value]
        if changed:
            raise ValueError(f"{len(changed)} korábbi fordítás megváltozott.")
        source = NEW.read_text(encoding="utf-8")
        for name, hu in translations.items():
            if f"#. {name}\n#: doc/classes/RichTextLabel.xml\n" not in source:
                raise ValueError(f"Hiányzik az osztályhivatkozás: {name}")
            if hu not in (new[key] for key in additions):
                raise ValueError(f"Hiányzik az új magyar szöveg: {name}")
        msgfmt = shutil.which("msgfmt")
        if msgfmt is None:
            raise ValueError("A gettext msgfmt nem érhető el.")
        with tempfile.TemporaryDirectory(prefix="godot_hu_v14_") as folder:
            subprocess.run(
                [msgfmt, "--check", "-o", str(Path(folder) / "v14.mo"), str(NEW)],
                check=True,
            )
        print(f"SIKER: {len(old)} megtartott + {len(additions)} új = "
              f"{len(new)} bejegyzés; BBCode és msgfmt rendben.")
        return 0
    except (KeyError, TypeError, ValueError, OSError, SyntaxError,
            subprocess.CalledProcessError) as exc:
        print(f"HIBA: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
