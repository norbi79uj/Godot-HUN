#!/usr/bin/env python3
"""Ellenőrzi a 10. lektorálás változatlan, 2026-11-10-i kiadási alapját.

A folyamatosan frissülő munkakatalógus helyett a kiadáskor rögzített
Git-állapotot hasonlítja a Lektorált 10 fájlhoz. A PO-fájlokat nem módosítja.
A git history elérése szükséges (GitHub Actions: fetch-depth: 0).
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
# A Lektorált 10 nyilvános kiadásának változatlan forrásállapota.
RELEASE_COMMIT = "a1684f79a028f8542b7fef541eda7a1ef1f7477d"
RELEASE_ORIGINAL = "forditas/Godot_4_7_2_hu_osszevont_munkavaltozat.po"


def release_original() -> dict[str, str]:
    """A kiadáshoz tartozó eredeti PO betöltése a Git-előzményekből."""
    with tempfile.TemporaryDirectory(prefix="godot_hu_10_alap_") as temp:
        output = Path(temp) / "eredeti_10.po"
        with output.open("wb") as stream:
            subprocess.run(
                ["git", "show", f"{RELEASE_COMMIT}:{RELEASE_ORIGINAL}"],
                stdout=stream,
                cwd=ROOT.parent,
                check=True,
            )
        return parse(output)

REVIEWED = ROOT / "Godot_4_7_2_hu_LEKTORALT_10.po"
TEXTEDIT = ROOT / "TextEdit_4_7_2_hu_reszlet.po"


def main() -> int:
    try:
        old = release_original()
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
        print("Viszonyítási alap: Lektorált 10 kiadás (2026-11-10).")
        print(f"SIKER: {len(new)} bejegyzés; {len(changes)} megváltozott fordítás; "
              "TextEdit egyezik; BBCode jelölések és msgfmt rendben.")
        return 0
    except (OSError, ValueError, SyntaxError, subprocess.CalledProcessError) as error:
        print(f"HIBA: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
