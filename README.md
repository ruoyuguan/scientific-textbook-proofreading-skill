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

## Human Review

The output is intended as a candidate errata report for expert human review. It should not be treated as a final authoritative judgement without manual checking.
