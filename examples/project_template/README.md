# Scientific Textbook Proofreading Project Template

This directory is a minimal local project template for using the Scientific Textbook Proofreading Skill with Codex, Claude Code, or another local AI agent.

## Directory structure

```text
project_template/
├── input/
│   └── .gitkeep
└── reports/
    └── .gitkeep
```

## File roles

Place source files under `input/` using explicit prefixes:

```text
UNDER_REVIEW_*.pdf
REFERENCE_*.pdf
ANSWER_KEY_*.pdf
IGNORE_*.pdf
```

Recommended examples:

```text
input/UNDER_REVIEW_textbook_draft.pdf
input/REFERENCE_Longair_High_Energy_Astrophysics.pdf
input/REFERENCE_Rybicki_Lightman_Radiative_Processes.pdf
input/ANSWER_KEY_chapter_12_solution.pdf
input/IGNORE_old_notes.pdf
```

## Reports

The agent should write generated reports under `reports/`:

```text
reports/chapter_01_errata.md
reports/chapter_02_errata.md
reports/processing_notes.md
reports/summary.md
```

## Recommended prompt

```text
Please use the scientific-textbook-proofreading skill in Local File Report Mode.

File roles:

- Manuscript under review: input/UNDER_REVIEW_textbook_draft.pdf
- Authoritative reference source: input/REFERENCE_authoritative_source.pdf

Review Chapter 1. Do not print the full report in chat. Write the chapter report to reports/chapter_01_errata.md. If extraction quality is poor, write notes to reports/processing_notes.md.
```

## Important note

Do not commit copyrighted textbooks, private manuscripts, proprietary lecture notes, or generated reports containing large copyrighted excerpts to a public repository.
