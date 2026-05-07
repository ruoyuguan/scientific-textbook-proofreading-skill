# Changelog

All notable changes to this project will be documented in this file.

This project follows a lightweight form of semantic versioning during the alpha stage. Until `v1.0.0`, the output contract, schema fields, evaluation cases, and recommended workflows may still change.

## [Unreleased]

### Planned

- Add explicit evidence/source fields to the errata output contract.
- Add `severity`, `verification_method`, `extraction_reliability`, and `human_review_note` fields.
- Expand `schemas/errata_report.schema.json` to match the richer output contract.
- Add a reusable `processing_notes` template.
- Add synthetic textbook examples that can be publicly shared without copyrighted source PDFs.
- Expand `evals/cases.jsonl` with positive and negative regression cases.
- Add stronger CI checks for schemas, JSONL files, skill metadata, and example reports.
- Improve README documentation for installation, local file report mode, and maintenance.

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
