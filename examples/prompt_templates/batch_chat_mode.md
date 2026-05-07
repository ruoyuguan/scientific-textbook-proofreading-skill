# Prompt Template: Batch Chat Mode

Please use the Scientific Textbook Proofreading Skill in batch mode.

## File roles

- Manuscript under review: `[UNDER_REVIEW filename]`
- Authoritative reference source: `[REFERENCE filename]`

## Task

Start from Chapter `[N]` and review chapters in order.

After finishing one chapter, continue to the next chapter automatically within the same response. Stop only when:

1. the response length is approaching the limit,
2. the current review unit is too large to complete safely,
3. file extraction quality is unreliable,
4. source roles are ambiguous,
5. or all requested chapters have been reviewed.

Only report scientifically meaningful issues requiring correction or clarification.

Use the required issue format:

- original formula or statement,
- problem type,
- re-derivation / check,
- judgement,
- corrected version,
- confidence.
