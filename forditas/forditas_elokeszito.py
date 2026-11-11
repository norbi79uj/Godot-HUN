#!/usr/bin/env python3
"""Read-only preparation of the next Godot-HUN translation batch.

Only untranslated entries already present in the newest reviewed PO catalog
are candidates. It does not claim to scan the entire upstream Godot source.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from katalogus_olvaso import read_draft

HERE = Path(__file__).resolve().parent


def newest_catalog(directory: Path = HERE) -> Path:
    versions = []
    for path in directory.glob("Godot_4_7_2_hu_LEKTORALT_*.po"):
        number = path.stem.rsplit("_", 1)[-1]
        if number.isdecimal():
            versions.append((int(number), path))
    if not versions:
        raise ValueError("Nem található számozott lektorált PO-katalógus.")
    return max(versions)[1]


def prepare(catalog: Path, limit: int = 40) -> str:
    if limit < 1 or limit > 500:
        raise ValueError("A csomagméret 1 és 500 között lehet.")
    entries = read_draft(catalog)
    remaining = [(source, target) for source, target in entries.items() if not target.strip()]
    chosen = remaining[:limit]
    lines = [
        "# Godot-HUN – következő fordítási csomag",
        "",
        f"- Forráskatalógus: \`{catalog.name}\`",
        f"- A katalógus bejegyzései: **{len(entries)}**",
        f"- Üres magyar fordítások ebben a katalógusban: **{len(remaining)}**",
        f"- Előkészített bejegyzések: **{len(chosen)}**",
        "",
        "> Csak a tároló legfrissebb számozott munkakatalógusában már szereplő, üres msgstr sorok kerülnek ide.",
        "> A teljes Godot forrásában lévő további, itt nem szereplő szövegeket ez a bot nem fedezi fel.",
        "> Azonosítók, [hivatkozások] és helyőrzők változatlanul hagyandók. Ez csak előkészítő lista.",
        "",
        "## Fordítandó szövegek",
        "",
    ]
    if not chosen:
        lines.append("Nincs üres magyar fordítás ebben a katalógusban. Az új szövegek forráskatalógusba emelése külön munkafolyamat.")
    for number, (source, _) in enumerate(chosen, 1):
        lines.extend([
            f"### {number}. szöveg", "",
            "**Angol eredeti:**", "",
            "~~~text", source, "~~~", "",
            "**Magyar fordítás (kézi lektorálásra):**", "",
            "_Még nincs fordítás._", "",
        ])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, help="Egy konkrét munkakatalógus")
    parser.add_argument("--limit", type=int, default=40)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    catalog = args.catalog or newest_catalog()
    result = prepare(catalog, args.limit)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result, encoding="utf-8")
        print(f"Fordítás-előkészítő jelentés: {args.output}")
    else:
        print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
