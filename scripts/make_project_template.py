from __future__ import annotations

import argparse
from pathlib import Path


README_TEMPLATE = """# Scientific Textbook Proofreading Project

This directory is intended for local use with the Scientific Textbook Proofreading Skill.

## File roles

Place files under `input/` using explicit prefixes:

- `UNDER_REVIEW_*.pdf` for the manuscript to be checked.
- `REFERENCE_*.pdf` for authoritative reference sources.
- `ANSWER_KEY_*.pdf` for answer keys or solution manuals.
- `IGNORE_*.pdf` for files that should not be used.

## Reports

The agent should write review outputs to `reports/`:

```text
reports/chapter_01_errata.md
reports/chapter_02_errata.md
reports/processing_notes.md
reports/summary.md
