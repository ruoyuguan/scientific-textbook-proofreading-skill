# Scientific Textbook Proofreading Skill

A reusable AI skill for scientific textbook proofreading and errata auditing.

This skill is designed for long-form scientific manuscripts with equations, derivations, cross-references, appendices, exercises, and domain-specific terminology. It helps AI agents review scientific correctness chapter by chapter, focusing on formula errors, dimensional consistency, physical assumptions, numerical coefficients, convention mismatches, outdated claims, and misleading scientific prose.

The intended users are textbook authors, scientific editors, instructors, graduate students, and technical reviewers who want a structured, conservative, source-grounded errata workflow.

## What This Skill Is For

- Scientific textbook proofreading.
- Lecture note auditing.
- Graduate course material checking.
- Formula and derivation verification.
- Errata report generation.
- Comparison against trusted reference textbooks.
- Identifying outdated claims superseded by later research.
- Local file-based chapter-by-chapter review with Codex or Claude Code.
- Future semi-automated proofreading pipelines.

## What This Skill Is Not For

- General grammar polishing.
- Layout correction.
- Typesetting cleanup.
- Bibliography formatting.
- Citation-placeholder completion.
- Replacing expert human review.
- Uploading or redistributing copyrighted textbooks.

## Repository Structure

~~~text
scientific-textbook-proofreading-skill/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── .gitignore
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
│   │   ├── sample_page.md
│   │   └── sample_equations.tex
│   ├── expected_output/
│   │   └── sample_errata_report.md
│   ├── prompt_templates/
│   │   ├── batch_chat_mode.md
│   │   ├── challenge_previous_judgement.md
│   │   ├── chapter_review_with_reference.md
│   │   ├── chapter_review_without_reference.md
│   │   ├── local_file_report_mode.md
│   │   └── single_equation_check.md
│   └── project_template/
│       ├── README.md
│       ├── input/
│       │   └── .gitkeep
│       └── reports/
│           └── .gitkeep
├── evals/
│   ├── cases.jsonl
│   └── golden/
│       ├── case_001.md
│       └── case_002.md
├── scripts/
│   ├── install_local.sh
│   ├── make_project_template.py
│   ├── validate_schema.py
│   ├── lint_skill.py
│   └── run_evals.py
└── .github/
    └── workflows/
        └── ci.yml
~~~

## Core Skill File

The main skill instruction file is:

~~~text
skill/SKILL.md
~~~

It contains the activation metadata, scientific review workflow, output format, source policy, uncertainty policy, astrophysics-specific checklist, batch mode, and local file report mode.

## Recommended Prompt: Basic Chapter Review

~~~text
Please use the Scientific Textbook Proofreading Skill.

File roles:

- Manuscript under review: [draft_filename.pdf]
- Authoritative reference source: [reference_filename.pdf]
- Optional additional sources: [additional_sources_if_any]

Review the manuscript under review, starting from [chapter_or_section].

Focus on scientific correctness:

- formula errors,
- dimensional consistency,
- numerical coefficients,
- physical assumptions,
- approximation regimes,
- unit systems,
- notation consistency,
- consistency between formulae and prose,
- outdated scientific claims,
- misleading scientific prose.

Use the authoritative reference source to check standard derivations, conventions, terminology, and accepted formulae.

Ignore layout, typography, citation placeholders, missing references, bibliography formatting, and grammar-only issues.

Only report issues requiring correction or clarification.
~~~

## File Role Mapping

When using this skill with multiple PDFs or source files, always tell the agent which file plays which role.

Recommended file naming convention:

~~~text
UNDER_REVIEW_textbook_draft.pdf
REFERENCE_Longair_High_Energy_Astrophysics.pdf
REFERENCE_Rybicki_Lightman_Radiative_Processes.pdf
ANSWER_KEY_chapter_12_reference_solution.pdf
IGNORE_old_notes.pdf
~~~

Recommended role mapping:

~~~text
- Manuscript under review: UNDER_REVIEW_textbook_draft.pdf
- Authoritative reference source: REFERENCE_Longair_High_Energy_Astrophysics.pdf
- Optional additional source: REFERENCE_Rybicki_Lightman_Radiative_Processes.pdf
- Answer key, not automatically authoritative: ANSWER_KEY_chapter_12_reference_solution.pdf
~~~

Do not assume the agent can reliably infer file roles from filenames alone. State the roles explicitly in the prompt.

## Batch Chat Mode

If you are using an ordinary chat interface rather than a local coding agent, use batch mode.

~~~text
Please use the Scientific Textbook Proofreading Skill in batch mode.

Review chapters in order. After finishing one chapter, continue to the next chapter automatically within the same response. Stop only when the response length is approaching the limit, file extraction quality is unreliable, source roles are ambiguous, or all requested chapters have been reviewed.

Only report scientifically meaningful issues requiring correction or clarification.
~~~

Note: ordinary chat interfaces cannot continue sending messages after a response has ended. Batch mode means continuing within the same response as far as possible. It is not asynchronous background work.

## Local File Report Mode

For long textbooks, the recommended workflow is Local File Report Mode.

Instead of printing a long multi-chapter report in chat, the agent writes one Markdown report per chapter.

Recommended local project structure:

~~~text
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
~~~

Recommended prompt:

~~~text
Please use the scientific-textbook-proofreading skill in Local File Report Mode.

File roles:

- Manuscript under review: input/UNDER_REVIEW_textbook_draft.pdf
- Authoritative reference source: input/REFERENCE_authoritative_source.pdf

Review the manuscript chapter by chapter. Do not print the full report in chat. Write each chapter report to:

reports/chapter_01_errata.md
reports/chapter_02_errata.md
...

Each chapter report should contain only scientifically meaningful issues and a chapter-level summary. After processing multiple chapters, generate reports/summary.md. If PDF extraction, formula recognition, or chapter boundary detection is unreliable, write details to reports/processing_notes.md.
~~~

## Create a Local Proofreading Project

Use the helper script:

~~~bash
python scripts/make_project_template.py ~/proofreading-projects/my-textbook-review
~~~

This creates:

~~~text
~/proofreading-projects/my-textbook-review/
├── input/
├── reports/
└── README.md
~~~

Then place files under:

~~~text
~/proofreading-projects/my-textbook-review/input/
~~~

using explicit prefixes such as:

~~~text
UNDER_REVIEW_*.pdf
REFERENCE_*.pdf
ANSWER_KEY_*.pdf
IGNORE_*.pdf
~~~

## Local Installation for Codex

Codex user-level skills can be installed under:

~~~text
~/.agents/skills
~~~

Install this skill locally with:

~~~bash
mkdir -p ~/ai-skills
cd ~/ai-skills

git clone https://github.com/ruoyuguan/scientific-textbook-proofreading-skill.git

cd scientific-textbook-proofreading-skill
bash scripts/install_local.sh
~~~

The installer creates a symlink at:

~~~text
~/.agents/skills/scientific-textbook-proofreading
~~~

Update later with:

~~~bash
cd ~/ai-skills/scientific-textbook-proofreading-skill
git pull --ff-only
~~~

Because the installed skill is a symlink, pulling the latest repository version updates the local Codex skill automatically.

Restart Codex if the skill does not appear immediately.

## Local Installation for Claude Code

Claude Code personal skills can be installed under:

~~~text
~/.claude/skills/<skill-name>/SKILL.md
~~~

The same installer also installs this skill for Claude Code:

~~~bash
cd ~/ai-skills/scientific-textbook-proofreading-skill
bash scripts/install_local.sh
~~~

The installer creates a symlink at:

~~~text
~/.claude/skills/scientific-textbook-proofreading
~~~

You can invoke the skill directly in Claude Code with:

~~~text
/scientific-textbook-proofreading
~~~

Update later with:

~~~bash
cd ~/ai-skills/scientific-textbook-proofreading-skill
git pull --ff-only
~~~

Restart Claude Code if the skill does not appear immediately.

## Suggested Local Workflow

1. Install the skill locally.
2. Create a local proofreading project.
3. Put the manuscript and reference files under `input/`.
4. Start Codex or Claude Code inside the project directory.
5. Ask the agent to use Local File Report Mode.
6. Review generated files under `reports/`.

Example:

~~~bash
python scripts/make_project_template.py ~/proofreading-projects/hea-review

cd ~/proofreading-projects/hea-review

# Put PDFs under input/
# input/UNDER_REVIEW_my_draft.pdf
# input/REFERENCE_Longair_High_Energy_Astrophysics.pdf

claude
~~~

Then prompt:

~~~text
Please use the scientific-textbook-proofreading skill in Local File Report Mode.

File roles:

- Manuscript under review: input/UNDER_REVIEW_my_draft.pdf
- Authoritative reference source: input/REFERENCE_Longair_High_Energy_Astrophysics.pdf

Review Chapter 1. Do not print the full report in chat. Write the chapter report to reports/chapter_01_errata.md. If extraction quality is poor, write notes to reports/processing_notes.md.
~~~

## Evaluation Files

This repository includes a minimal eval structure:

~~~text
evals/
├── cases.jsonl
└── golden/
    ├── case_001.md
    └── case_002.md
~~~

These are not full automated scientific evaluations. They are lightweight regression examples intended to keep the skill behavior stable as the instructions evolve.

Run basic checks with:

~~~bash
python scripts/validate_schema.py
python scripts/lint_skill.py
python scripts/run_evals.py
~~~

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

~~~text
Skill instructions
→ Local File Report Mode
→ Project template
→ Manual local-agent review
→ Semi-automated extraction scripts
→ Full pipeline
~~~

## Human Review

The output is intended as a candidate errata report for expert human review. It should not be treated as a final authoritative judgement without manual checking.

The skill is designed to reduce false positives and false negatives, but it cannot guarantee perfect scientific correctness.

## Copyright Note

Do not commit copyrighted textbooks, private manuscripts, proprietary lecture notes, or unpublished drafts to this public repository.

Users should provide their own legally accessible manuscripts and reference PDFs at runtime.
