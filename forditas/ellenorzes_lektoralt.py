#!/usr/bin/env python3
"""Ellenőrzi a Godot-HUN eredeti és 10. szakaszban lektorált F1-PO fájlját.

Olvasásra használja a bemeneti fájlokat, a beépített Godot-ot nem módosítja.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

from ellenorzes import parse

ROOT = Path(__file__).resolve().parent
ORIGINAL = ROOT / "Godot_4_7_2_hu_osszevont_munkavaltozat.po"
REVIEWED = ROOT / "Godot_4_7_2_hu_LEKTORALT_10.po"
TEXTEDIT = ROOT / "TextEdit_4_7_2_hu_reszlet.po"


def main() -> int:
    try:
        old = parse(ORIGINAL)
        new = parse(REVIEWED)
        subset = parse(TEXTEDIT)
        if old.keys() != new.keys():
            raise ValueError("Változott a fordítási kulcsok halmaza!")
        changes = [k for k in old if old[k] != new[k]]
        if len(old) != 2188 or len(changes) != 77:
            raise ValueError(
                f"Váratlan méret vagy változásszám: bejegyzés={len(old)}, eltérő={len(changes)}."
            )
        for key, value in subset.items():
            if new.get(key) != value:
                raise ValueError("TextEdit-részhalmaz eltér az új fájltól.")
        import re
        tags = lambda txt: Counter(re.findall(r"\[[^\]]+\]", txt))
        for key in old:
            if tags(old[key]) != tags(new[key]):
                raise ValueError(f"Eltérő súgójelölések: {key[:90]}")
        binary = shutil.which("msgfmt")
        if binary is None:
            raise ValueError("A GNU gettext msgfmt nincs telepítve.")
        with tempfile.TemporaryDirectory(prefix="godot_hu_lektoralt_") as temp:
            dest = Path(temp)
            shutil.copyfile(REVIEWED, dest / "lektoralt.po")
            subprocess.run(
                [binary, "--check", "-o", str(dest / "lektoralt.mo"), str(dest / "lektoralt.po")],
                check=True,
            )
        print(f"SIKER: {len(new)} bejegyzés; {len(changes)} megváltozott fordítás; "
              "TextEdit egyezik; BBCode jelölések és msgfmt rendben.")
        return 0
    except (OSError, ValueError, SyntaxError, subprocess.CalledProcessError) as error:
        print(f"HIBA: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
