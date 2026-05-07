# Prompt Template: Chapter Review with Authoritative Reference

Please use the Scientific Textbook Proofreading Skill.

## File roles

- Manuscript under review: `[draft_filename.pdf]`
- Authoritative reference source: `[reference_filename.pdf]`
- Optional additional sources: `[additional_sources_if_any]`

## Task

Review the manuscript under review, starting from `[chapter_or_section]`.

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

If later research or more recent references supersede an old textbook statement, explicitly distinguish:

- still-valid formula,
- outdated observational value,
- historically correct but now incomplete statement,
- genuinely incorrect claim.

Ignore:

- layout,
- typography,
- citation placeholders,
- missing references,
- bibliography formatting,
- grammar-only issues.

## Output

Only report issues requiring correction or clarification.

For each issue, use:

1. Original formula or statement.
2. Problem type.
3. Re-derivation / check.
4. Judgement.
5. Corrected formula or statement.
6. Suggested replacement prose when needed.
7. Confidence.

Do not list correct formulae unless needed to explain an issue.
