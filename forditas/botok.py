#!/usr/bin/env python3
"""Godot-HUN: read-only terminology and placeholder audits.

No translation file is written. Terminology warnings are advisory; broken
machine placeholders fail CI. Scans the latest numbered reviewed catalog.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys

from katalogus_olvaso import read_draft

ROOT = Path(__file__).resolve().parent
PRINTF = re.compile(r"%(?:\d+\$)?[-+#0 ]*(?:\d+|\*)?(?:\.(?:\d+|\*))?[hlLzjt]*[diuoxXfFeEgGaAcsp]")
BRACES = re.compile(r"(?<!\{)\{[A-Za-z_][A-Za-z_0-9]*\}(?!\})")
GODOT_TAG = re.compile(r"\[[^\]\n]+\]")


def latest_catalog() -> Path:
    versions = []
    for p in ROOT.glob("Godot_4_7_2_hu_LEKTORALT_*.po"):
        suffix = p.stem.rsplit("_", 1)[-1]
        if suffix.isdecimal():
            versions.append((int(suffix), p))
    if not versions:
        raise ValueError("Nincs számozott lektorált PO-katalógus.")
    return max(versions)[1]


def placeholder_problems(source: str, target: str) -> list[str]:
    problems = []
    for title, regex in (
        ("printf helyőrző", PRINTF),
        ("kapcsos helyőrző", BRACES),
        ("Godot hivatkozás", GODOT_TAG),
    ):
        original = Counter(regex.findall(source))
        translated = Counter(regex.findall(target))
        if original != translated:
            problems.append(f"{title}: {dict(original)} -> {dict(translated)}")
    return problems


def glossary_warnings(entries: dict[str, str], glossary: list[dict]) -> list[str]:
    warnings = []
    for source, target in entries.items():
        for term in glossary:
            english, hungarian = term["english"], term["hungarian"]
            # Only apply to straightforward standalone terms, never snippets of
            # API identifiers such as Node2D or method names.
            source_rx = r"(?<![\w])" + re.escape(english) + r"(?![\w])"
            if not re.search(source_rx, source, re.IGNORECASE):
                continue
            if re.search(re.escape(hungarian), target, re.IGNORECASE):
                continue
            # A glossary is a review hint, not proof of a mistranslation.
            warnings.append(f"{english} -> {hungarian} | EN: {source[:110]} | HU: {target[:110]}")
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, help="Markdown report path")
    parser.add_argument("--catalog", type=Path, help="Optional PO catalog for local tests")
    args = parser.parse_args()
    try:
        source_file = args.catalog or latest_catalog()
        entries = read_draft(source_file)
        glossary = json.loads((ROOT / "godot_szotar.json").read_text(encoding="utf-8"))
        errors = []
        for source, target in entries.items():
            if not target:
                continue  # Not yet translated; list as unfinished, not a structural error.
            for issue in placeholder_problems(source, target):
                errors.append(f"{issue} | {source[:130]}")
        warnings = glossary_warnings({s: t for s, t in entries.items() if t}, glossary)
        untranslated = sum(not t for t in entries.values())
        lines = [
            "# Godot-HUN: szótárbot és hibavadász",
            "", f"- Katalógus: `{source_file.name}`",
            f"- Katalógusbejegyzések: **{len(entries)}**",
            f"- Még üres magyar fordítások: **{untranslated}**",
            f"- Szerkezeti eltérések: **{len(errors)}**",
            f"- Szótári lektorálási javaslatok: **{len(warnings)}**",
            "",
            "## Hibavadász – lehetséges szerkezeti hibák", "",
        ]
        lines += [f"- {issue}" for issue in errors] or ["Nincs észlelt helyőrző- vagy hivatkozáseltérés."]
        lines += ["", "## Szótárbot – kézi ellenőrzést igénylő javaslatok", ""]
        lines += [f"- {issue}" for issue in warnings[:100]] or ["Nincs szótári figyelmeztetés."]
        if len(warnings) > 100:
            lines += [f"", f"További {len(warnings) - 100} figyelmeztetés nincs felsorolva."]
        lines += ["", "> A szótári találat nem automatikus fordítási hiba. A bot nem módosít katalógust.", ""]
        report = "\n".join(lines)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(report, encoding="utf-8")
        else:
            print(report)
        print(f"Szótárbot: {len(warnings)} javaslat; hibavadász: {len(errors)} eltérés.")
        return 1 if errors else 0
    except (ValueError, OSError, SyntaxError, json.JSONDecodeError) as exc:
        print(f"HIBA: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
