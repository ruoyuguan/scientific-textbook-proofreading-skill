# Changelog

All notable changes to this project will be documented in this file.

This project follows a lightweight form of semantic versioning during the alpha stage. Until `v1.0.0`, the output contract, schema fields, evaluation cases, and recommended workflows may still change.

## [Unreleased]

### Added

- Added golden outputs for eval cases 003--006, covering inverse-Compton regime limits, dimensional consistency, overstrong EHT claims, and gamma-ray observing regimes.
- Added a reusable processing-notes template under `templates/processing_notes.template.md`.
- Added a synthetic textbook chapter under `examples/synthetic_textbook/chapter_01.md`.
- Added expected synthetic errata reports in both Markdown and JSON formats.
- Added `scripts/lint_markdown.py` to detect unbalanced Markdown code fences and known rendering-artifact tokens.
- Added `scripts/validate_examples.py` for lightweight validation of example JSON reports.
- Added prompt templates for chapter review without references and single-equation checks.
- Added project maintenance files: `CONTRIBUTING.md`, `SECURITY.md`, and `CITATION.cff`.
- Expanded `evals/cases.jsonl` with positive and negative regression cases.

### Changed

- Strengthened `skill/output_contract.md` with explicit severity, verification method, extraction reliability, evidence/source, and human-review fields.
- Expanded `schemas/errata_report.schema.json` to support richer machine-readable errata reports.
- Aligned `skill/SKILL.md` with the richer output contract.
- Updated Local File Report Mode instructions in `skill/SKILL.md`.
- Updated README documentation for the repository structure, synthetic examples, and validation checks.
- Updated CI to validate Markdown files, eval cases, and example JSON reports.

### Planned

- Add more golden outputs for existing eval cases.
- Add a full synthetic local-file workflow example.
- Strengthen `scripts/validate_examples.py` against schema enums.
- Improve README installation and usage documentation.
- Expand eval cases toward 20+ examples before the first beta release.
- Add more domain-specific synthetic examples for astrophysics, gravitational-wave physics, and radiative processes.

## [v0.1.0-alpha] - 2026-05-07

### Added

- Initial public alpha release of the Scientific Textbook Proofreading Skill.
- Core `skill/SKILL.md` instructions for scientific textbook proofreading and errata auditing.
- Structured chapter-level errata-report workflow.
- Basic output contract for formula errors, dimensional inconsistencies, wrong physical regimes, notation conflicts, outdated claims, and misleading scientific prose.
- Scientific review rubric, citation policy, and uncertainty/refusal policy.
- Basic JSON schema under `schemas/errata_report.schema.json`.
- Minimal evaluation scaffolding under `evals/`.
- Example input/output structure under `examples/`.
- Local file report mode for Codex and Claude Code workflows.
- File-role mapping rules for `UNDER_REVIEW_`, `REFERENCE_`, `ANSWER_KEY_`, and `IGNORE_` inputs.
- Prompt templates for chapter review, batch chat mode, local file report mode, and judgement challenges.
- Local proofreading project template.
- Helper scripts for local installation, project-template generation, schema validation, skill linting, and lightweight evaluation.
- `.gitignore` safeguards for PDFs and local generated reports.
- GitHub Actions validation workflow.

### Status

- Alpha release.
- Intended for expert-assisted scientific review, not final authoritative judgement.
- Output contract, JSON schema, examples, and evaluation cases are not yet stable.
- Current examples and evals are minimal and should be expanded before beta release.
