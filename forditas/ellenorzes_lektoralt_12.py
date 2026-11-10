#!/usr/bin/env python3
"""Godot HUN 12. szakasz: új és korábbi F1-súgószövegek ellenőrzése.

Az előző 2230 fordításnak változatlannak kell maradnia; a 78 új üzenet
súgójelöléseit és gettext-szerkezetét a közös parse() ellenőrzi.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from ellenorzes import parse

HERE = Path(__file__).resolve().parent
OLD = HERE / "Godot_4_7_2_hu_LEKTORALT_11.po"
NEW = HERE / "Godot_4_7_2_hu_LEKTORALT_12.po"
NEW_COUNT = 78
CHECK_NAMES = (
    "Timer.is_stopped",
    "CanvasLayer.follow_viewport_enabled",
    "RandomNumberGenerator.randf",
    "Tween.set_pause_mode",
    "Node.get_children",
    "CanvasItem.get_viewport_rect",
    "EditorInterface.get_editor_language",
    "AStarGrid2D.set_point_solid",
)


def main() -> int:
    try:
        old = parse(OLD)
        new = parse(NEW)
        if len(old) != 2230 or len(new) != len(old) + NEW_COUNT:
            raise ValueError(f"Váratlan katalógusméret: régi={len(old)}, új={len(new)}")
        changed = [key for key, value in old.items() if new.get(key) != value]
        if changed:
            raise ValueError(f"{len(changed)} korábbi fordítás megváltozott!")
        additions = set(new) - set(old)
        if len(additions) != NEW_COUNT:
            raise ValueError(f"Váratlan új üzenetszám: {len(additions)}")
        content = NEW.read_text(encoding="utf-8")
        for name in CHECK_NAMES:
            if f"#. {name}\n" not in content:
                raise ValueError(f"Hiányzó kulcs: {name}")
        msgfmt = shutil.which("msgfmt")
        if msgfmt is None:
            raise ValueError("msgfmt nem található")
        with tempfile.TemporaryDirectory(prefix="godot_hu_v12_") as temp:
            subprocess.run(
                [msgfmt, "--check", "-o", str(Path(temp) / "v12.mo"), str(NEW)],
                check=True,
            )
        print(f"SIKER: {len(old)} korábbi és {len(additions)} új F1-súgóbejegyzés; "
              "súgójelölések, duplikációk és gettext rendben.")
        return 0
    except (ValueError, OSError, SyntaxError, subprocess.CalledProcessError) as exc:
        print(f"HIBA: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
