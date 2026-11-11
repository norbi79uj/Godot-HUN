#!/usr/bin/env python3
"""PO reader for draft catalogs, including untranslated entries (read-only)."""
from __future__ import annotations
import ast
from pathlib import Path
import re

LINE = re.compile(r'(?m)^msgid ("(?:\\.|[^"\\])*")\nmsgstr ("(?:\\.|[^"\\])*")$')


def read_draft(path: Path) -> dict[str, str]:
    entries = {}
    for number, block in enumerate(re.split(r"\n\s*\n", path.read_text(encoding="utf-8-sig")), 1):
        match = LINE.search(block)
        if not match:
            if re.search(r"(?m)^msgid ", block):
                raise ValueError(f"{path.name}: nem támogatott PO-blokk: {number}")
            continue
        source, target = (ast.literal_eval(value) for value in match.groups())
        if not source:
            continue
        if source in entries:
            raise ValueError(f"{path.name}: ismételt msgid: {source[:80]!r}")
        entries[source] = target
    return entries
