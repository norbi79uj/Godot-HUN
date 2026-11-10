#!/usr/bin/env python3
"""Ellenőrzi, hogy a 11. fordítási szakasz a 10. változatra épül-e.

A korábbi bejegyzések változatlanok; az újonnan bevont osztálysúgó-szövegek
nem üresek, a Godot hivatkozásai megmaradnak és a PO lefordítható.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from ellenorzes import parse

ROOT = Path(__file__).resolve().parent
OLD = ROOT / "Godot_4_7_2_hu_LEKTORALT_10.po"
NEW = ROOT / "Godot_4_7_2_hu_LEKTORALT_11.po"
NEW_COUNT = 42
REQUIRED_EXAMPLES = (
    "Returns a [Rect2] representing the Sprite2D's boundary in local coordinates.",
    "Aligns the camera to the tracked node.",
    "Emitted when the animation loops.",
    "Emitted when the received [param area] enters this area.",
)


def main() -> int:
    try:
        old, new = parse(OLD), parse(NEW)
        if len(old) != 2188 or len(new) != len(old) + NEW_COUNT:
            raise ValueError(f"Váratlan bejegyzésszám: előző={len(old)}, új={len(new)}")
        changed = [k for k in old if new.get(k) != old[k]]
        if changed:
            raise ValueError(f"A 10. fordításból {len(changed)} korábbi bejegyzés megváltozott!")
        additional = set(new) - set(old)
        if len(additional) != NEW_COUNT:
            raise ValueError(f"Az új msgid-k száma nem {NEW_COUNT}: {len(additional)}")
        for required in REQUIRED_EXAMPLES:
            if not any(k.startswith(required) for k in additional):
                raise ValueError(f"Kötelező új fordítás hiányzik: {required}")
        cmd = shutil.which("msgfmt")
        if not cmd:
            raise ValueError("A msgfmt nem található.")
        with tempfile.TemporaryDirectory(prefix="godot_hu_v11_") as tmp:
            output = Path(tmp) / "v11.mo"
            subprocess.run([cmd, "--check", "-o", str(output), str(NEW)], check=True)
        print(f"SIKER: {len(old)} megtartott és {len(additional)} új F1-súgó bejegyzés; "
              "Godot-súgójelölések és msgfmt rendben.")
        return 0
    except (OSError, ValueError, SyntaxError, subprocess.CalledProcessError) as exc:
        print(f"HIBA: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
