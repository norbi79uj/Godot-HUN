#!/usr/bin/env python3
"""Lektorálási segéd: csak olvas, nem módosítja a PO-katalógusokat."""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
from ellenorzes import parse

ROOT = Path(__file__).resolve().parent


def latest_pair() -> tuple[Path, Path]:
    versions = []
    for path in ROOT.glob("Godot_4_7_2_hu_LEKTORALT_*.po"):
        suffix = path.stem.rsplit("_", 1)[-1]
        if suffix.isdecimal():
            versions.append((int(suffix), path))
    versions.sort()
    if len(versions) < 2:
        raise ValueError("Legalább két számozott LEKTORALT PO-fájl szükséges.")
    return versions[-2][1], versions[-1][1]


def report(previous: Path, current: Path) -> str:
    before, after = parse(previous), parse(current)
    added = [(source, after[source]) for source in after if source not in before]
    removed = [source for source in before if source not in after]
    changed = [(source, before[source], after[source]) for source in before
               if source in after and before[source] != after[source]]
    unchanged = len(before) - len(removed) - len(changed)
    suspicious = [(s, t) for s, t in added if s.strip() == t.strip()]
    rows = [
        "# Godot-HUN – automatikus lektorálási jelentés",
        "",
        f"- Előző katalógus: `{previous.name}`",
        f"- Aktuális katalógus: `{current.name}`",
        f"- Változatlan fordítás: **{unchanged}**",
        f"- Új fordítás: **{len(added)}**",
        f"- Megváltozott fordítás: **{len(changed)}**",
        f"- Eltűnt bejegyzés: **{len(removed)}**",
        f"- Az angollal teljesen egyező új magyar szöveg: **{len(suspicious)}** (kézi vizsgálat, nem feltétlenül hiba)",
        "",
        "## Új bejegyzések – lektorálási sor",
        "",
    ]
    if not added:
        rows.append("Nincsenek új bejegyzések.")
    for i, (source, translation) in enumerate(added, 1):
        rows.extend([f"### {i}. bejegyzés", "", "**Angol:**", "", source, "",
                     "**Magyar javaslat:**", "", translation, ""])
    rows += ["## Megváltozott korábbi fordítások", ""]
    if not changed:
        rows.append("Nincs megváltozott korábbi fordítás.")
    for source, old, new in changed:
        rows.extend([f"- **Angol:** {source}", f"  - Régi: {old}", f"  - Új: {new}"])
    rows += ["", "## Eltűnt bejegyzések", ""]
    if not removed:
        rows.append("Nincs eltűnt bejegyzés.")
    else:
        rows.extend(f"- {source}" for source in removed)
    rows += ["", "> A jelentés nem minősíti automatikusan helyesnek a fordítást. A véglegesítés emberi lektorálást igényel.", ""]
    return "\n".join(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    previous, current = latest_pair()
    content = report(previous, current)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content, encoding="utf-8")
        print(f"Lektorálási jelentés elkészült: {args.output}")
    else:
        print(content)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
