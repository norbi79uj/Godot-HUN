#!/usr/bin/env python3
"""Read-only progress report about entries in versioned Godot-HUN catalogs."""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import re

from katalogus_olvaso import LINE, read_draft
from forditas_elokeszito import newest_catalog

HERE = Path(__file__).resolve().parent
CLASS = re.compile(r"(?m)^#\. ([A-Za-z_][A-Za-z0-9_]*)\.")
BLOCK = re.compile(r"\n\s*\n")


def classes_by_entry(catalog: Path) -> dict[str, set[str]]:
    """Class labels are hints from PO comments, not proof of class completeness."""
    import ast
    labels: dict[str, set[str]] = {}
    for block in BLOCK.split(catalog.read_text(encoding="utf-8-sig")):
        match = LINE.search(block)
        if not match:
            continue
        source = ast.literal_eval(match.group(1))
        if not source:
            continue
        found = set(CLASS.findall(block))
        if found:
            labels.setdefault(source, set()).update(found)
    return labels


def report(catalog: Path, directory: Path | None = None) -> str:
    current = read_draft(catalog)
    directory = directory or catalog.parent
    versions = []
    for path in directory.glob("Godot_4_7_2_hu_LEKTORALT_*.po"):
        number = path.stem.rsplit("_", 1)[-1]
        if number.isdecimal() and path != catalog:
            versions.append((int(number), path))
    previous_path = max(versions)[1] if versions else None
    # If current is a standard numbered catalog, compare to the immediately
    # preceding numbered version, never to a higher-numbered version.
    if catalog.stem.rsplit("_", 1)[-1].isdecimal():
        n = int(catalog.stem.rsplit("_", 1)[-1])
        preceding = [(v, p) for v, p in versions if v < n]
        previous_path = max(preceding)[1] if preceding else None
    prior = read_draft(previous_path) if previous_path else {}
    filled = sum(bool(value.strip()) for value in current.values())
    blank = len(current) - filled
    added = sum(source not in prior for source in current)
    newly_filled = sum(
        bool(value.strip()) and not prior.get(source, "").strip()
        for source, value in current.items()
    ) if previous_path else 0
    labels = classes_by_entry(catalog)
    tally: Counter[str] = Counter()
    for source, value in current.items():
        if value.strip():
            tally.update(labels.get(source, []))
    lines = [
        "# Godot-HUN – fordítási haladásjelentés", "",
        f"- Legfrissebb munkakatalógus: \`{catalog.name}\`",
        f"- Katalógusbejegyzések: **{len(current)}**",
        f"- Nem üres magyar szövegek: **{filled}**",
        f"- Üres magyar szövegek: **{blank}**",
        f"- A katalóguson belüli kitöltöttség: **{filled / len(current) * 100:.1f}%**" if current else "- A katalógus üres.",
        "",
        "**Fontos:** ez NEM a teljes Godot magyarítottsági százaléka! Csak a jelenlegi munkakatalógusé.",
        "",
        f"- Előző változat: \`{previous_path.name}\`" if previous_path else "- Előző változat: nincs",
        f"- Új msgid bejegyzések az előző verzióhoz képest: **{added}**" if previous_path else "- Nincs összehasonlítható korábbi verzió.",
        f"- Most kitöltött, előző verzióban hiányzó vagy üres fordítások: **{newly_filled}**" if previous_path else "",
        "",
        "## Osztályhivatkozások a katalógus megjegyzései alapján", "",
        "| Osztály | Nem üres magyar bejegyzések |",
        "| --- | ---: |",
    ]
    lines.extend(f"| \`{name}\` | {count} |" for name, count in tally.most_common(20))
    if not tally:
        lines.append("| Nincs felismerhető osztály-megjegyzés | 0 |")
    lines.extend(["", "> Egy osztály említése nem jelenti annak teljes fordítását.", ""])
    return "\n".join(line for line in lines if line is not None)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    catalog = args.catalog or newest_catalog()
    result = report(catalog)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result, encoding="utf-8")
        print(f"Haladásjelentés: {args.output}")
    else:
        print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
