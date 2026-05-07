from __future__ import annotations

import argparse
from pathlib import Path


README_TEMPLATE = r"""# Scientific Textbook Proofreading Project

This directory is intended for local use with the Scientific Textbook Proofreading Skill.

## File roles

Place files under `input/` using explicit prefixes:

- `UNDER_REVIEW_*.pdf` for the manuscript to be checked.
- `REFERENCE_*.pdf` for authoritative reference sources.
- `ANSWER_KEY_*.pdf` for answer keys or solution manuals.
- `IGNORE_*.pdf` for files that should not be used.

## Reports

The agent should write review outputs to `reports/`:

~~~text
reports/chapter_01_errata.md
reports/chapter_02_errata.md
reports/processing_notes.md
reports/summary.md
~~~

## Recommended prompt

Please use the scientific-textbook-proofreading skill in Local File Report Mode.

File roles:

- Manuscript under review: input/UNDER_REVIEW_[filename].pdf
- Authoritative reference source: input/REFERENCE_[filename].pdf

Review the manuscript chapter by chapter. Write each chapter report to reports/chapter_NN_errata.md. Do not print the full report in chat. Generate reports/summary.md after processing multiple chapters. Write extraction or ambiguity problems to reports/processing_notes.md.
"""


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a local proofreading project directory."
    )
    parser.add_argument(
        "project_dir",
        help="Path to the local proofreading project directory to create.",
    )
    args = parser.parse_args()

    project_dir = Path(args.project_dir).expanduser().resolve()
    input_dir = project_dir / "input"
    reports_dir = project_dir / "reports"

    input_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)

    (input_dir / ".gitkeep").touch()
    (reports_dir / ".gitkeep").touch()

    readme_path = project_dir / "README.md"
    if not readme_path.exists():
        readme_path.write_text(README_TEMPLATE, encoding="utf-8")

    print(f"Created proofreading project at: {project_dir}")
    print(f"Input directory: {input_dir}")
    print(f"Reports directory: {reports_dir}")


if __name__ == "__main__":
    main()
