# Prompt Template: Single Equation Check

Please use the Scientific Textbook Proofreading Skill.

## Equation or statement to check

```tex
[Paste equation or statement here]
```

## Context

- Field: `[physics / astronomy / astrophysics / etc.]`
- Unit convention: `[SI / cgs / geometrized units / natural units / unknown]`
- Relevant assumptions: `[list if known]`
- Source or manuscript location: `[optional]`

## Task

Check whether the equation or statement is scientifically correct.

Focus on:

1. Dimensional consistency.
2. Missing constants or numerical factors.
3. Unit-system assumptions.
4. Approximation regime.
5. Physical interpretation.
6. Notation consistency.
7. Limiting cases.

## Output

Use the following structure:

1. Original equation or statement.
2. Assumed conventions.
3. Dimensional check.
4. First-principles derivation or verification.
5. Regime of validity.
6. Judgement.
7. Corrected version, if needed.
8. Human-review note.
9. Confidence.

If the equation is correct under a specific convention but wrong otherwise, state the convention explicitly.
