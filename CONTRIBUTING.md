# Contributing

Thank you for your interest in improving the Scientific Textbook Proofreading Skill.

This repository is an AI-agent skill for scientific textbook proofreading and errata auditing. Contributions should improve the skill's reliability, conservatism, reproducibility, and usefulness for expert human review.

## Project principles

Contributions should follow these principles:

1. **Scientific correctness first.** The skill should prioritize formula correctness, dimensional consistency, physical assumptions, approximation regimes, notation consistency, and source-grounded reasoning.
2. **Conservative reporting.** The skill should not flag a statement merely because it is simplified. It should report an issue only when the statement is wrong, misleading, internally inconsistent, dimensionally invalid, outside its stated regime, outdated relative to the manuscript date, or likely to confuse a graduate-level reader.
3. **Human review required.** Outputs are candidate errata for expert review, not final authoritative judgements.
4. **Evidence matters.** Issues should be supported by derivation, dimensional analysis, cross-reference checks, reference sources, or official/current sources where relevant.
5. **Respect copyright.** Do not commit copyrighted textbooks, solution manuals, proprietary manuscripts, or large excerpts from copyrighted sources.

## Good contributions

Good contributions include:

- Improvements to `skill/SKILL.md`.
- Clearer output-contract requirements.
- Better uncertainty and refusal policies.
- New problem-type categories with precise definitions.
- More robust JSON schemas.
- Synthetic examples that do not depend on copyrighted PDFs.
- Regression cases under `evals/`.
- Documentation improvements.
- CI checks for schema validity, JSONL formatting, and skill metadata.

## Repository layout

```text
scientific-textbook-proofreading-skill/
├── skill/
│   ├── SKILL.md
│   ├── output_contract.md
│   ├── scientific_rubric.md
│   ├── citation_policy.md
│   └── refusal_and_uncertainty_policy.md
├── schemas/
│   └── errata_report.schema.json
├── examples/
├── evals/
├── scripts/
└── .github/workflows/
```

## Before opening a pull request

Please run the basic checks:

```bash
python scripts/validate_schema.py
python scripts/lint_skill.py
python scripts/run_evals.py
```

If a check fails, either fix it or explain why it is expected to fail.

## Adding evaluation cases

Evaluation cases should be small and focused.

Prefer synthetic examples over copyrighted textbook excerpts.

A good eval case should include:

- A short scientific statement or formula.
- The expected judgement.
- The intended problem type.
- The corrected version, if applicable.
- A note explaining why the case should or should not be flagged.

Important: include negative cases where the statement is correct and should not be reported. This helps prevent the skill from becoming overly aggressive.

Useful categories include:

- Formula errors.
- Dimensional inconsistencies.
- Missing approximation regimes.
- Wrong physical regimes.
- Convention-dependent but self-consistent expressions.
- Outdated scientific claims.
- Overstrong scientific claims.
- Correct statements that should not be flagged.
- Cases where PDF extraction is unreliable.

## Copyright and source policy

Do not commit:

- Full copyrighted textbooks.
- Full solution manuals.
- Proprietary manuscripts.
- Large excerpts from copyrighted materials.
- Private review reports without permission.
- Any file containing sensitive or confidential information.

Allowed materials include:

- Synthetic textbook snippets.
- Short excerpts used only when legally appropriate.
- Public-domain or openly licensed materials with attribution.
- Metadata-only examples.
- Expected-output files that avoid reproducing long copyrighted passages.

## Pull request style

A pull request should ideally do one thing:

- One output-contract update.
- One schema update.
- One documentation update.
- One group of related eval cases.
- One script or CI improvement.

Please include:

1. Summary of the change.
2. Motivation.
3. Files changed.
4. Checks run.
5. Any limitations or follow-up work.

## Versioning

During the alpha stage, output formats and schemas may change.

Suggested version progression:

```text
v0.1.x-alpha  documentation, metadata, small compatibility fixes
v0.2.0-beta   richer output contract, expanded schema, more evals
v0.3.0-beta   full synthetic examples and stronger local workflows
v1.0.0        stable output contract, schema, examples, and evaluation suite
```

## Reporting issues

When opening an issue, please include:

- What you expected the skill to do.
- What it actually did.
- The relevant prompt or minimal example.
- Whether the issue concerns scientific correctness, output format, file handling, citation/source policy, or evaluation behavior.
- Whether copyrighted or private files are involved. Do not upload such files to public issues.

## Maintainer note

This project is intended to assist domain experts. It should never be presented as a replacement for expert scientific review.
