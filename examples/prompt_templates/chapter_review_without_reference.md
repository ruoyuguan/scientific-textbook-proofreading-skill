# Prompt Template: Chapter Review without Authoritative Reference

Please use the Scientific Textbook Proofreading Skill.

## File roles

- Manuscript under review: `[UNDER_REVIEW filename]`
- Authoritative reference source: none provided
- Optional additional sources: `[list if any]`

## Task

Review Chapter `[N]` or Section `[name]` of the manuscript.

Because no authoritative reference source is provided, use a conservative review standard:

1. Check only issues that can be verified from first principles, dimensional analysis, internal consistency, or well-established scientific knowledge.
2. Do not make strong source-comparison claims.
3. Mark uncertain issues as requiring manual review.
4. Do not invent citations or claim that a reference says something unless that reference is available.

## Review focus

Check for:

- formula errors,
- dimensional inconsistencies,
- missing approximation regimes,
- wrong physical regimes,
- unit-system mismatches,
- notation conflicts,
- inconsistent cross-references,
- outdated claims that require current-source verification,
- misleading scientific prose.

Ignore:

- layout,
- typography,
- citation placeholders,
- missing references,
- bibliography formatting,
- grammar-only issues.

## Output

Only report issues requiring correction, clarification, or expert review.

For each issue, include:

- stable issue identifier,
- exact location,
- original formula or statement,
- problem type,
- severity,
- extraction reliability,
- verification method,
- evidence/source basis,
- re-derivation or check,
- judgement,
- corrected formula or statement,
- suggested replacement prose when useful,
- human-review note,
- confidence.
