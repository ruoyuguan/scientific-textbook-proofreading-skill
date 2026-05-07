# Prompt Template: Local File Report Mode

Please use the Scientific Textbook Proofreading Skill in Local File Report Mode.

## File roles

- Manuscript under review: `input/UNDER_REVIEW_[filename].pdf`
- Authoritative reference source: `input/REFERENCE_[filename].pdf`
- Optional additional sources: `[list if any]`

## Task

Review the manuscript chapter by chapter.

Do not print the full review in chat. Write the results to Markdown files:

```text
reports/chapter_01_errata.md
reports/chapter_02_errata.md
reports/chapter_03_errata.md
...
reports/summary.md
reports/processing_notes.md
```

## Review focus

Check scientific correctness only:

- formula errors,
- dimensional consistency,
- numerical coefficients,
- physical assumptions,
- approximation regimes,
- unit systems,
- notation consistency,
- consistency between formulae and prose,
- cross-chapter consistency,
- outdated scientific claims,
- misleading scientific prose.

Ignore:

- layout,
- typography,
- citation placeholders,
- missing references,
- bibliography formatting,
- grammar-only issues,
- figure placement.

## Output requirements

Each chapter report should include only issues requiring correction or clarification.

For each issue, use:

1. Original formula or statement.
2. Problem type.
3. Re-derivation / check.
4. Judgement.
5. Corrected formula or statement.
6. Suggested replacement prose when needed.
7. Confidence.

After all processed chapters, generate `reports/summary.md`.

If PDF extraction, formula recognition, or chapter boundary detection is unreliable, write details to `reports/processing_notes.md`.
