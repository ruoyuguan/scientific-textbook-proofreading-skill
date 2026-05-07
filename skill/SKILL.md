---
name: scientific-textbook-proofreading
description: >
  Use this skill when the user asks to proofread, audit, verify, or produce errata
  for a long-form scientific textbook, lecture note, homework solution, or technical
  manuscript. Focus on scientific correctness: formula errors, dimensional consistency,
  first-principles derivations, numerical coefficients, unit systems, physical assumptions,
  outdated scientific claims, source-grounded corrections, and misleading scientific prose.
  Do not use for general grammar polishing, layout correction, bibliography formatting,
  or citation-placeholder cleanup unless explicitly requested.
---

# Scientific Textbook Proofreading Skill

## Purpose

This skill helps the assistant perform scientific proofreading and errata auditing for long-form scientific textbooks, lecture notes, homework solutions, and technical manuscripts.

The primary goal is to detect scientifically meaningful problems, especially:

- formula errors,
- dimensional inconsistencies,
- wrong numerical coefficients,
- incorrect physical assumptions,
- invalid approximation regimes,
- unit-system mistakes,
- notation inconsistencies,
- misleading scientific prose,
- outdated scientific claims,
- inconsistencies between equations and surrounding explanations.

This is not a general copyediting or layout-correction skill. The assistant should ignore typography, page layout, missing references, placeholder citations, figure placement, and grammar-only issues unless the user explicitly asks for them.

## User Context

The user is usually acting as an author, editor, instructor, graduate student, or technical reviewer of a scientific textbook or course manuscript.

Treat the request as a serious scientific errata audit. The output should be a candidate errata report for expert human review, not an unquestionable final judgement.

## When to Use This Skill

Use this skill when the user asks to:

- check a scientific textbook,
- proofread a scientific manuscript,
- inspect a course handout or lecture note,
- find formula errors,
- audit equations,
- verify derivations,
- check dimensional consistency,
- compare a draft against authoritative textbooks,
- produce errata,
- review a chapter for scientific correctness,
- determine whether older textbook statements have been superseded by later research.

Typical user requests may include phrases such as:

- "I am the editor of this textbook"
- "check the whole book"
- "find possible formula errors"
- "derive every formula from first principles"
- "original expression — re-derivation — judgement — correction"
- "continue to the next chapter"
- "only output problematic parts"
- "ignore layout problems"
- "compare against authoritative sources"
- "judge whether this has been superseded by later discoveries"
- "我是这本书的编者"
- "请你检索全书"
- "找出公式错误"
- "从第一性原理重推"
- "原式—重推—判定—修正"
- "继续下一章"
- "只输出有问题的部分"
- "忽略排版问题"
- "对照权威教材"

## Scope of Review

Focus on the scientific correctness of the manuscript.

Review the following:

1. Formula correctness.
2. Dimensional consistency.
3. Numerical coefficients and constants.
4. Unit-system consistency, including SI, cgs-Gaussian, natural units, geometrized units, and conventional astrophysical units.
5. Symbol definitions.
6. Notation consistency.
7. Physical assumptions.
8. Approximation regimes.
9. Boundary conditions.
10. Limiting cases.
11. Consistency between formulae and surrounding prose.
12. Consistency across chapters, sections, appendices, examples, and exercises.
13. Scientifically misleading language.
14. Outdated claims superseded by later research, observations, reviews, or textbooks.
15. Incorrect or ambiguous cross-references when they affect scientific meaning.
16. Numerical estimates, unit conversions, and powers of ten.
17. Source-frame versus observer-frame distinctions.
18. Exact formulae versus approximations, scaling laws, and order-of-magnitude estimates.

Ignore unless explicitly requested:

1. Typography.
2. Page layout.
3. Figure placement.
4. Missing references.
5. Placeholder citations.
6. Bibliography formatting.
7. Grammar-only issues.
8. General language polishing.
9. Chapter numbering or section-numbering problems.
10. Purely stylistic rewriting.
11. Incomplete citations that do not affect scientific meaning.

## Source Policy

Use the following hierarchy of sources.

### 1. User-provided manuscript

The draft manuscript being reviewed is the primary object of analysis.

If the user provides a PDF, TeX file, Markdown file, Word document, or extracted text, use it as the object to be checked.

### 2. User-provided authoritative sources

Prefer sources explicitly provided by the user, such as:

- uploaded textbook PDFs,
- TeX source files,
- solution manuals,
- course notes,
- instructor-provided references,
- local knowledge bases,
- trusted reference textbooks,
- field-specific websites or documents.

If the user designates a source as authoritative, use it as a baseline for:

- notation,
- conventional derivations,
- accepted approximations,
- terminology,
- formula normalization,
- pedagogical conventions.

Do not assume any source is infallible. A trusted source may still contain outdated claims, convention-specific formulae, typographical errors, or approximations that do not apply to the reviewed manuscript.

### 3. Field-standard references

Use standard textbooks, review articles, canonical papers, and widely accepted derivations to verify formulae, conventions, and physical reasoning.

Examples of relevant fields include:

- classical mechanics,
- electrodynamics,
- statistical mechanics,
- quantum mechanics,
- general relativity,
- cosmology,
- high-energy astrophysics,
- radiative processes,
- stellar structure,
- plasma physics,
- gravitational-wave physics,
- numerical methods,
- statistics and data analysis.

### 4. Recent literature and official sources

Use recent peer-reviewed literature, official mission pages, collaboration papers, catalogue documentation, data-release papers, or standards documents when checking:

- current observational values,
- mission status,
- catalogue sizes,
- discovery claims,
- physical constants,
- cosmological parameters,
- current best constraints,
- claims likely to have changed since an older textbook was written.

### 5. General web sources

Use general web sources only when necessary.

Do not use general web pages as the sole basis for correcting a technical formula if better sources are available.

When using web sources or external references, cite the source that actually supports the claim.

## Review Workflow

For long manuscripts, review chapter by chapter unless the user specifies a different unit.

Default review unit order:

1. chapter,
2. section,
3. subsection,
4. equation cluster,
5. page range,
6. individual formula or paragraph.

Do not attempt to produce a full-book review in one response when the manuscript is long. Review one manageable unit at a time. At the end of a review unit, stop. The user may continue with "continue", "next chapter", "继续下一章", or similar.

For each review unit, follow this workflow.

### Step 1: Extract candidate scientific items

Identify all scientifically meaningful candidate items:

- equations,
- definitions,
- scaling relations,
- numerical estimates,
- physical assumptions,
- unit conversions,
- cross-references,
- observational claims,
- factual claims,
- explanatory prose,
- limiting-case statements,
- exercise answers,
- derivation steps.

### Step 2: Check equations

For each important equation:

1. Restate the original expression.
2. Define symbols when needed.
3. Identify the unit system.
4. Check dimensional consistency.
5. Re-derive the expression from first principles when feasible.
6. Compare with authoritative sources when useful.
7. Test limiting cases.
8. Check sign conventions.
9. Check normalization conventions.
10. Check factors such as `2`, `4π`, `c`, `h`, `\hbar`, `k_B`, `G`, `\mu_0`, and `\epsilon_0`.
11. Check powers of variables, especially Lorentz factors, redshift factors, frequency factors, mass factors, and distance factors.
12. Check whether the equation matches the surrounding prose.
13. Check whether the equation is valid in the stated physical regime.
14. Check consistency with earlier and later equations in the manuscript.

### Step 3: Check numerical estimates

For each numerical value:

1. Identify all constants used.
2. Identify the unit system.
3. Reproduce the calculation.
4. Check conversion factors.
5. Check powers of ten.
6. Check significant figures.
7. Check whether the numerical value is consistent with the stated physical assumptions.
8. If a value depends on modern measurements, verify whether it is current or should be described as approximate or historical.

### Step 4: Check prose claims

For each scientific prose claim:

1. Extract the actual scientific claim.
2. Determine whether it is correct, misleading, outdated, too strong, too weak, ambiguous, or inconsistent.
3. Check whether the claim is supported by the equations.
4. Check whether the claim is supported by authoritative sources.
5. Propose a corrected publishable version when needed.

### Step 5: Check cross-references and internal consistency

For long textbooks, check whether:

1. Symbols are reused consistently.
2. Equation references point to the correct result.
3. A later formula contradicts an earlier definition.
4. A chapter uses a convention different from another chapter without warning.
5. A statement in prose conflicts with a figure, table, appendix, or exercise.
6. A derived formula silently changes unit system or frame.

### Step 6: Report only meaningful issues

Only report items that need correction, clarification, or explicit expert judgement.

Do not list every correct formula unless the user explicitly asks for a complete derivation log.

If no scientific issue is found in a review unit, say:

> No scientific error found in this section under the present review.

## Required Output Format

For each reported issue, use the following structure.

### Issue N — Page / Section / Equation

**Original formula or statement**

```tex
...
```

**Problem type**

Choose one or more:

- Formula error
- Dimensional inconsistency
- Wrong numerical coefficient
- Wrong physical assumption
- Wrong physical regime
- Unit-system mismatch
- Convention mismatch
- Ambiguous notation
- Inconsistent cross-reference
- Misleading prose
- Outdated scientific claim
- Pedagogical clarification
- Numerical error
- Source inconsistency

**Re-derivation / check**

Show the derivation, dimensional analysis, limiting-case test, numerical reproduction, or source comparison.

The check should be explicit enough for a human expert to verify.

**Judgement**

Choose one:

- Confirmed error
- Likely error
- Convention-dependent
- Ambiguous
- Correct but misleading
- Correct but should be clarified
- Outdated but historically understandable
- No correction needed

**Corrected formula or statement**

```tex
...
```

**Suggested replacement prose**

Provide a publishable corrected sentence or paragraph when appropriate.

**Confidence**

Choose one:

- High
- Medium
- Low

## Chapter-Level Summary

At the end of each chapter review, include a short chapter-level summary.

Use this format:

```markdown
## Chapter Summary

- Confirmed errors: N
- Likely errors: N
- Convention-dependent issues: N
- Clarification-only issues: N
- Overall judgement: ...
```

The overall judgement should be concise and should distinguish scientific reliability from style, layout, or editorial polish.

## Uncertainty Policy

Do not overclaim.

If extraction from a PDF is poor, say so.

If a formula may be correct under a different convention, label it as convention-dependent rather than wrong.

If a source is old but historically correct, distinguish that from a present-day false statement.

If a claim depends on current observational data, recent discoveries, software versions, catalogue sizes, mission status, or standards, verify from current authoritative sources when tools are available.

If evidence is insufficient, say:

> I cannot confirm this as an error from the available material. It should be manually checked against [specific source, equation, or topic].

Never invent:

- page numbers,
- equation numbers,
- citations,
- sources,
- constants,
- claims about consensus,
- claims about what a source says.

## Scientific Rubric

When checking formulae and claims, always consider:

1. Dimensions.
2. Unit system.
3. Missing constants.
4. Sign conventions.
5. Normalization conventions.
6. Powers of variables.
7. Frame dependence.
8. Source-frame versus observer-frame quantities.
9. Approximation regime.
10. Boundary conditions.
11. Limiting cases.
12. Whether a formula is exact, approximate, asymptotic, empirical, or order-of-magnitude.
13. Whether the surrounding prose claims more than the formula justifies.
14. Whether a numerical estimate follows from the stated constants.
15. Whether an old statement has been superseded by later research.

## Astrophysics-Specific Checklist

For astrophysics, high-energy astrophysics, gravitational-wave physics, and cosmology, pay special attention to:

1. Confusion between luminosity and flux.
2. Confusion between intensity, flux density, luminosity density, and emissivity.
3. Confusion between frequency `ν` and angular frequency `ω`.
4. Missing factors of `2π`.
5. Missing redshift factors.
6. Source-frame versus observer-frame confusion.
7. Luminosity distance versus comoving distance versus angular-diameter distance.
8. Isotropic-equivalent energy versus beaming-corrected true energy.
9. Missing beaming or Doppler factors.
10. Missing pitch-angle factors in synchrotron radiation.
11. Incorrect synchrotron critical-frequency conventions.
12. Incorrect synchrotron cooling time.
13. Incorrect inverse-Compton energy scaling.
14. Thomson versus Klein-Nishina regime errors.
15. Incorrect bremsstrahlung cooling-time coefficients or density dependence.
16. Incorrect Eddington luminosity constants.
17. Confusion between number density and mass density.
18. Wrong opacity dimensions.
19. Incorrect virial-theorem coefficients.
20. Wrong cosmic-ray spectral-index conventions.
21. Incorrect Fermi acceleration coefficients.
22. Incorrect shock-jump conditions.
23. Incorrect gravitational-wave strain scaling.
24. Incorrect chirp-mass powers.
25. Incorrect post-Newtonian order statements.
26. Confusion between strain amplitude, characteristic strain, ASD, PSD, and energy density.
27. Incorrect cosmological parameter values presented as exact.
28. Outdated observational claims from older textbooks.

## Interaction Protocol

When the user asks to start a book review:

1. Begin with the first requested chapter, section, or page range.
2. Review only that unit unless the user explicitly asks for a larger scope.
3. Output only scientifically meaningful issues.
4. Use the required issue format.
5. End with a chapter-level summary.

When the user says "continue", "next chapter", "继续", or "继续下一章":

1. Continue using the same review standard.
2. Do not ask the user to repeat the instructions.
3. Preserve the same output format.
4. Review the next logical unit.

When the user challenges a judgement:

1. Re-check the original expression.
2. Identify the convention and assumptions.
3. Re-derive the result explicitly.
4. State whether the original judgement should be retained, weakened, or corrected.
5. Acknowledge mistakes plainly if the previous judgement was wrong.

## Batch Mode

When the user requests "batch mode", "auto continue", "automatic chapter-by-chapter review", "continuous chapter review", "批处理模式", "自动继续", or similar, the assistant should continue reviewing chapters in order without waiting for the user to type "continue" after each chapter, as far as the current interaction mode allows.

In batch mode, the assistant should:

1. Review chapters in order.
2. Preserve the same issue format for every chapter.
3. Insert a clear chapter heading before each chapter report.
4. Output only scientifically meaningful issues requiring correction or clarification.
5. Include a chapter-level summary after each chapter.
6. Stop only when:
   - the output length is approaching the limit,
   - the current review unit is too large to complete safely,
   - file extraction quality is too poor,
   - source roles are ambiguous,
   - the user must clarify a critical assumption,
   - or all requested chapters have been reviewed.

In ordinary chat interfaces, the assistant cannot send additional messages after a response has ended. Therefore, batch mode means "continue within the same response as much as possible", not asynchronous background work.

If working in a local coding-agent environment, prefer Local File Report Mode instead of printing all chapter reports in chat.

## Local File Report Mode

When the user requests "local file report mode", "write reports to files", "generate chapter report files", "方案 B", or similar, the assistant should write review results into local Markdown files rather than printing the full report in chat.

This mode is recommended for Codex, Claude Code, or any local coding-agent environment.

### Recommended project layout

```text
proofreading-project/
├── input/
│   ├── UNDER_REVIEW_textbook_draft.pdf
│   └── REFERENCE_authoritative_source.pdf
├── reports/
│   ├── chapter_01_errata.md
│   ├── chapter_02_errata.md
│   ├── chapter_03_errata.md
│   ├── processing_notes.md
│   └── summary.md
└── README.md
```

### File role rules

The user should explicitly identify file roles. If roles are not explicit, infer from filename prefixes when possible:

- `UNDER_REVIEW_` means the manuscript to be checked.
- `REFERENCE_` means an authoritative or optional comparison source.
- `ANSWER_KEY_` means an answer key or reference solution, useful but not automatically authoritative.
- `IGNORE_` means the file should not be used.

If file roles remain ambiguous, ask for clarification before performing a long review.

### Report writing rules

When writing reports to files:

1. Create one Markdown report per chapter.
2. Use zero-padded chapter numbers, such as `chapter_01_errata.md`.
3. Write only issues requiring correction or clarification.
4. Include a chapter-level summary in each chapter report.
5. Create `reports/summary.md` after processing multiple chapters.
6. Create or update `reports/processing_notes.md` when:
   - PDF text extraction is unreliable,
   - formula recognition is poor,
   - chapter boundaries are ambiguous,
   - reference source matching is incomplete,
   - or a manual check is required.

### Chapter report template

Each chapter report should use this structure:

```markdown
# Chapter N Errata Report

## Scope

- Manuscript under review:
- Reference sources:
- Review unit:
- Date:

## Issues

### Issue 1 — Page / Section / Equation

**Original formula or statement**

```tex
...
```

**Problem type**

- ...

**Re-derivation / check**

...

**Judgement**

...

**Corrected formula or statement**

```tex
...
```

**Suggested replacement prose**

...

**Confidence**

High / Medium / Low.

## Chapter Summary

- Confirmed errors: N
- Likely errors: N
- Convention-dependent issues: N
- Clarification-only issues: N
- Overall judgement: ...
```

### Summary report template

The final `reports/summary.md` should include:

```markdown
# Scientific Textbook Proofreading Summary

## File Roles

- Manuscript under review:
- Reference sources:

## Chapter Overview

| Chapter | Confirmed errors | Likely errors | Convention-dependent | Clarification-only | Notes |
|---|---:|---:|---:|---:|---|

## Highest-Priority Corrections

1. ...

## Manual Checks Required

1. ...

## Processing Notes

- ...
```

## Output Language

Use the user's language by default.

If the user writes in Chinese, explain in Chinese while preserving equations, symbols, and technical terms in standard mathematical notation.

If the user asks for LaTeX patches, provide copyable LaTeX code blocks.

## Quality Standard

The output should be suitable for:

- a textbook author,
- a scientific editor,
- a graduate-level instructor,
- a technically competent copyeditor,
- a domain expert performing manual review.

The assistant should be rigorous, conservative, traceable, and explicit about uncertainty.

The goal is not to maximize the number of reported issues. The goal is to minimize false positives and false negatives while preserving scientific correctness.
