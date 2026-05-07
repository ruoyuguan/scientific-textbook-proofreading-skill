# Scientific Textbook Proofreading Skill

A reusable AI skill for scientific textbook proofreading and errata auditing.

This skill is designed for long-form scientific manuscripts with equations, derivations, cross-references, appendices, exercises, and domain-specific terminology. It helps AI agents review scientific correctness chapter by chapter, focusing on formula errors, dimensional consistency, physical assumptions, numerical coefficients, convention mismatches, outdated claims, and misleading scientific prose.

## Repository Structure

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
│   ├── input/
│   └── expected_output/
├── evals/
│   ├── cases.jsonl
│   └── golden/
├── scripts/
└── .github/
    └── workflows/
```

## What This Skill Is For

- Scientific textbook proofreading.
- Lecture note auditing.
- Graduate course material checking.
- Formula and derivation verification.
- Errata report generation.
- Comparison against trusted reference textbooks.
- Identifying outdated claims superseded by later research.

## What This Skill Is Not For

- General grammar polishing.
- Layout correction.
- Typesetting cleanup.
- Bibliography formatting.
- Citation-placeholder completion.
- Replacing expert human review.

## Recommended Prompt

```text
Please use the Scientific Textbook Proofreading Skill. Review the attached textbook chapter for scientific correctness. Focus on formula errors, dimensional consistency, numerical coefficients, physical assumptions, unit systems, outdated scientific claims, and misleading prose. Ignore layout, citation placeholders, and grammar-only issues. Use the provided reference materials as authoritative sources where appropriate. Output only items requiring correction or clarification.
```

## File Role Mapping

When using this skill with multiple PDFs or source files, always tell the agent which file plays which role.

Recommended file naming convention:

```text
UNDER_REVIEW_textbook_draft.pdf
REFERENCE_Longair_High_Energy_Astrophysics.pdf
REFERENCE_Rybicki_Lightman_Radiative_Processes.pdf
ANSWER_KEY_chapter_12_reference_solution.pdf
IGNORE_old_notes.pdf
```

Recommended role mapping:

```text
- Manuscript under review: UNDER_REVIEW_textbook_draft.pdf
- Authoritative reference source: REFERENCE_Longair_High_Energy_Astrophysics.pdf
- Optional additional source: REFERENCE_Rybicki_Lightman_Radiative_Processes.pdf
- Answer key, not automatically authoritative: ANSWER_KEY_chapter_12_reference_solution.pdf
```

Do not assume the agent can reliably infer file roles from filenames alone. State the roles explicitly in the prompt.

## Local File Report Mode

For long textbooks, the recommended workflow is Local File Report Mode.

Instead of printing a long multi-chapter report in chat, the agent writes one Markdown report per chapter.

Recommended local project structure:

```text
proofreading-project/
├── input/
│   ├── UNDER_REVIEW_textbook_draft.pdf
│   └── REFERENCE_authoritative_source.pdf
├── reports/
│   ├── chapter_01_errata.md
│   ├── chapter_02_errata.md
│   ├── processing_notes.md
│   └── summary.md
└── README.md
```

Recommended prompt:

```text
Please use the scientific-textbook-proofreading skill in Local File Report Mode.

File roles:

- Manuscript under review: input/UNDER_REVIEW_textbook_draft.pdf
- Authoritative reference source: input/REFERENCE_authoritative_source.pdf

Review the manuscript chapter by chapter. Do not print the full report in chat. Write each chapter report to:

reports/chapter_01_errata.md
reports/chapter_02_errata.md
...

Each chapter report should contain only scientifically meaningful issues and a chapter-level summary. After processing multiple chapters, generate reports/summary.md. If PDF extraction, formula recognition, or chapter boundary detection is unreliable, write details to reports/processing_notes.md.
```

## Batch Chat Mode

If you are using a normal chat interface rather than a local coding agent, use batch mode.

```text
Please use the Scientific Textbook Proofreading Skill in batch mode.

Review chapters in order. After finishing one chapter, continue to the next chapter automatically within the same response. Stop only when the response length is approaching the limit, file extraction quality is unreliable, source roles are ambiguous, or all requested chapters have been reviewed.
```

Note: ordinary chat interfaces cannot continue sending messages after a response has ended. Batch mode means continuing within the same response as far as possible.

## Create a Local Proofreading Project

Use the helper script:

```bash
python scripts/make_project_template.py ~/proofreading-projects/my-textbook-review
```

Then place files under:

```text
~/proofreading-projects/my-textbook-review/input/
```

using explicit prefixes such as:

```text
UNDER_REVIEW_*.pdf
REFERENCE_*.pdf
ANSWER_KEY_*.pdf
```

## Local Installation for Codex

Install this skill for Codex using:

```bash
bash scripts/install_local.sh
```

Manual installation:

```bash
mkdir -p ~/ai-skills
cd ~/ai-skills
git clone https://github.com/ruoyuguan/scientific-textbook-proofreading-skill.git

mkdir -p ~/.agents/skills

ln -sfn ~/ai-skills/scientific-textbook-proofreading-skill/skill \
  ~/.agents/skills/scientific-textbook-proofreading
```

Update later with:

```bash
cd ~/ai-skills/scientific-textbook-proofreading-skill
git pull --ff-only
```

Because the installed skill is a symlink, pulling the latest repository version updates the local Codex skill automatically.

## Local Installation for Claude Code

The same installer also installs the skill for Claude Code:

```bash
bash scripts/install_local.sh
```

Manual installation:

```bash
mkdir -p ~/.claude/skills

ln -sfn ~/ai-skills/scientific-textbook-proofreading-skill/skill \
  ~/.claude/skills/scientific-textbook-proofreading
```

Invoke directly in Claude Code with:

```text
/scientific-textbook-proofreading
```

Update later with:

```bash
cd ~/ai-skills/scientific-textbook-proofreading-skill
git pull --ff-only
```

## Toward a Full Pipeline

This repository currently provides a skill and local file workflow. A future full pipeline may add:

1. PDF text extraction.
2. Formula extraction.
3. Chapter boundary detection.
4. Automatic chapter queue generation.
5. Per-chapter model calls.
6. Report validation against `schemas/errata_report.schema.json`.
7. Summary report aggregation.

The recommended development path is:

```text
Skill instructions
→ Local File Report Mode
→ Project template
→ Manual local-agent review
→ Semi-automated extraction scripts
→ Full pipeline
```

## Copyright Note

Do not commit copyrighted textbooks, private manuscripts, proprietary lecture notes, or unpublished drafts to this public repository.

Users should provide their own legally accessible manuscripts and reference PDFs at runtime.

## Human Review

The output is intended as a candidate errata report for expert human review. It should not be treated as a final authoritative judgement without manual checking.
