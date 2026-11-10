#!/usr/bin/env python3
"""A részleges magyar F1-katalógus lefedett osztályainak összesítése.

Csak olvas; egy osztály említése NEM jelenti a teljes osztály fordítását.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import re

CATALOG = Path(__file__).with_name("Godot_4_7_2_hu_LEKTORALT_15.po")
CLASS = re.compile(r"(?m)^#\. ([A-Za-z_][A-Za-z0-9_]*)\.")
MSGID = re.compile(r'(?m)^msgid "(?:\\.|[^"\\])*"$')
MSGSTR = re.compile(r'(?m)^msgstr "((?:\\.|[^"\\])*)"$')


def main() -> None:
    text = CATALOG.read_text(encoding="utf-8-sig")
    classes: Counter[str] = Counter()
    entries = 0
    for block in re.split(r"\n\s*\n", text):
        source = CLASS.search(block)
        original = MSGID.search(block)
        translated = MSGSTR.search(block)
        if not source or not original or not translated:
            continue
        if not translated.group(1):
            continue
        classes[source.group(1)] += 1
        entries += 1

    print("# Godot HUN – a fordítás jelenlegi mérete")
    print()
    print(f"- Magyarított, osztályhoz rendelt szövegbejegyzések: **{entries}**")
    print(f"- Érintett Godot-osztályok száma: **{len(classes)}**")
    print("- **Figyelem:** ezek részleges munkafordítások, nem teljes osztályfordítások.")
    print()
    print("## Tíz legtöbb bejegyzést tartalmazó osztály")
    print()
    print("| Osztály | Fordított bejegyzések |")
    print("| --- | ---: |")
    for name, count in sorted(classes.items(), key=lambda item: (-item[1], item[0]))[:10]:
        print(f"| `{name}` | {count} |")


if __name__ == "__main__":
    main()
