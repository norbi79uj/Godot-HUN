#!/usr/bin/env python3
# Godot 4.7.2 magyar F1-katalógus ellenőrzése.
# Csak olvas: nem módosítja a PO-fájlokat és a Godot telepítését.
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MERGED = ROOT / "Godot_4_7_2_hu_osszevont_munkavaltozat.po"
TEXTEDIT = ROOT / "TextEdit_4_7_2_hu_reszlet.po"
ENTRY = re.compile(r'(?m)^msgid ("(?:\\.|[^"\\])*")\nmsgstr ("(?:\\.|[^"\\])*")$')
TAG = re.compile(r'\[[^\]]+\]')

def parse(path: Path) -> dict[str, str]:
    import ast
    content = path.read_text(encoding="utf-8-sig")
    result: dict[str, str] = {}
    for number, block in enumerate(re.split(r"\n\s*\n", content), start=1):
        match = ENTRY.search(block)
        if not match:
            if "msgid " in block:
                raise ValueError(f"{path.name}: hibás vagy nem támogatott PO-blokk: {number}")
            continue
        original, translated = (ast.literal_eval(value) for value in match.groups())
        if not isinstance(original, str) or not isinstance(translated, str):
            raise ValueError(f"{path.name}: nem szöveges érték")
        if not original:
            continue  # PO-fejléc
        if original in result:
            raise ValueError(f"{path.name}: ismétlődő msgid: {original[:80]!r}")
        if not translated:
            raise ValueError(f"{path.name}: hiányzó fordítás: {original[:80]!r}")
        if sorted(TAG.findall(original)) != sorted(TAG.findall(translated)):
            raise ValueError(f"{path.name}: súgójelölés-eltérés: {original[:80]!r}")
        result[original] = translated
    return result

def main() -> int:
    parser = argparse.ArgumentParser(description="Godot F1 magyar munkakatalógus ellenőrzése")
    parser.add_argument("--require-msgfmt", action="store_true",
                        help="Hibának tekinti, ha a gettext msgfmt nem található.")
    args = parser.parse_args()
    try:
        combined = parse(MERGED)
        textedit = parse(TEXTEDIT)
        problems = [src[:100] for src, hu in textedit.items() if combined.get(src) != hu]
        if problems:
            raise ValueError(f"TextEdit: {len(problems)} hiányzó vagy eltérő bejegyzés, pl. {problems[0]!r}")
        print(f"Előzetes ellenőrzés rendben: {len(combined)} közös + {len(textedit)} TextEdit fordítás.")
        binary = shutil.which("msgfmt")
        if binary is None:
            print("FIGYELEM: msgfmt nincs telepítve, a szabványos gettext ellenőrzés NEM történt meg.")
            return 1 if args.require_msgfmt else 0
        # A Windows alatti msgfmt egyes kiadásai nem tudják megnyitni
        # az ékezetes elérési utakat. A másolatokat ASCII nevű átmeneti
        # könyvtárban ellenőrizzük, az eredeti PO-fájlokat nem módosítjuk.
        with tempfile.TemporaryDirectory(prefix="godot_po_check_") as temp:
            work = Path(temp)
            for index, file in enumerate((MERGED, TEXTEDIT), start=1):
                print(f"Gettext-ellenőrzés: {file.name}", flush=True)
                copy = work / f"catalog_{index}.po"
                shutil.copyfile(file, copy)
                subprocess.run([binary, "--check", "-o", str(work / f"catalog_{index}.mo"),
                                str(copy)], check=True)
        print("msgfmt --check: mindkét fájl rendben.")
        return 0
    except (ValueError, SyntaxError, OSError, subprocess.CalledProcessError) as exc:
        print(f"HIBA: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
