# Output Contract

This file defines the required output structure for the Scientific Textbook Proofreading Skill.

The goal of the output contract is to make every reported issue:

- scientifically meaningful,
- conservative,
- traceable,
- easy for a human expert to verify,
- suitable for later conversion into a machine-readable errata report.

The assistant should report only issues requiring correction, clarification, or expert judgement. It should not list every correct formula unless the user explicitly asks for a complete derivation log.

---

## 1. General Reporting Rules

Every reported issue must include:

1. A stable issue identifier.
2. Exact location in the manuscript.
3. The original formula or statement.
4. Problem type.
5. Severity.
6. Extraction reliability.
7. Verification method.
8. Evidence or source basis.
9. Re-derivation, dimensional analysis, source comparison, or logical check.
10. Judgement.
11. Corrected formula or statement.
12. Suggested replacement prose when useful.
13. Human-review note.
14. Confidence.

The assistant must not invent:

- page numbers,
- equation numbers,
- figure numbers,
- citations,
- source claims,
- consensus statements,
- constants,
- or claims about what a source says.

If the page number, equation number, or source location is unavailable, say so explicitly.

---

## 2. Controlled Problem Types

Use one or more of the following machine-readable problem types:

```text
formula_error
dimensional_inconsistency
wrong_numerical_coefficient
wrong_physical_assumption
wrong_physical_regime
missing_approximation_regime
unit_system_mismatch
notation_conflict
ambiguous_notation
inconsistent_cross_reference
misleading_prose
overstrong_claim
outdated_scientific_claim
source_inconsistency
numerical_error
pedagogical_clarification
pdf_extraction_uncertainty
```

Human-readable labels may also be shown, but the machine-readable values above should be preferred in JSON or structured output.

---

## 3. Severity

Use one of:

```text
critical
major
minor
clarification
```

Guidance:

- `critical`: A central formula, conclusion, or physical claim is wrong and may seriously mislead the reader.
- `major`: A meaningful scientific error, wrong regime, dimensional mistake, or outdated claim should be corrected.
- `minor`: A localized issue that does not undermine the surrounding scientific argument but still needs correction.
- `clarification`: The original statement is broadly correct but should be qualified, softened, or made more precise.

---

## 4. Extraction Reliability

Use one of:

```text
high
medium
low
```

Guidance:

- `high`: The statement or formula is clearly extracted from the manuscript or visually verified.
- `medium`: The prose is readable but notation, subscripts, superscripts, or equation layout may be partially degraded.
- `low`: PDF extraction, OCR, layout, equation formatting, or page mapping is unreliable.

If extraction reliability is `low`, do not make strong claims unless the issue is independently verified from a page image, TeX source, or another reliable representation.

---

## 5. Verification Method

Use one or more of:

```text
first_principles_derivation
dimensional_analysis
limiting_case_check
numerical_reproduction
source_comparison
cross_reference_check
current_status_check
notation_consistency_check
unit_system_check
manual_visual_check_required
```

A strong issue should normally be supported by at least one explicit verification method.

---

## 6. Evidence / Source Basis

Each issue should include an evidence section.

Possible evidence types:

```text
manuscript_internal
reference_textbook
peer_reviewed_paper
official_collaboration_source
mission_or_catalog_documentation
current_web_source
derivation_only
manual_check_required
```

For sources, include as much as available:

- source title,
- author or collaboration,
- chapter / section / page / equation if known,
- URL if used,
- access date for current web sources,
- short note explaining what the source supports.

Do not cite a source unless it actually supports the correction.

---

## 7. Required Markdown Issue Format

Use the following Markdown structure for each issue.

````markdown
### Issue CHNN-XXX — Page / Section / Equation

**Original formula or statement**

```tex
...
```

**Problem type**

- `problem_type`

**Severity**

- `major`

**Extraction reliability**

- `high`

**Verification method**

- `dimensional_analysis`
- `source_comparison`

**Evidence / sources**

- Manuscript: ...
- Reference source: ...
- Current source, if used: ...
- Notes: ...

**Re-derivation / check**

...

**Judgement**

Confirmed error / Likely error / Convention-dependent / Ambiguous / Correct but misleading / Correct but should be clarified / Outdated but historically understandable / No correction needed

**Corrected formula or statement**

```tex
...
```

**Suggested replacement prose**

...

**Human-review note**

...

**Confidence**

High / Medium / Low
````

---

## 8. Allowed Judgements

Use one of:

```text
Confirmed error
Likely error
Convention-dependent
Ambiguous
Correct but misleading
Correct but should be clarified
Outdated but historically understandable
No correction needed
```

Do not use `No correction needed` in the final issue list unless the user requested a complete derivation or audit log. For ordinary errata reports, omit correct items.

---

## 9. Chapter-Level Summary

At the end of each chapter report, include:

```markdown
## Chapter Summary

- Confirmed errors: N
- Likely errors: N
- Convention-dependent issues: N
- Clarification-only issues: N
- Extraction limitations: ...
- Highest-priority corrections: ...
- Manual checks required: ...
- Overall judgement: ...
```

The overall judgement should distinguish scientific reliability from style, layout, copyediting, or typesetting quality.

---

## 10. Local File Report Contract

When operating in Local File Report Mode, the assistant should write review outputs to Markdown files under `reports/`.

Recommended output layout:

```text
reports/
├── chapter_01_errata.md
├── chapter_02_errata.md
├── ...
├── processing_notes.md
└── summary.md
```

Each `chapter_NN_errata.md` file must include:

1. Chapter title or review unit.
2. Manuscript under review.
3. Reference sources used.
4. Extraction reliability notes.
5. List of reported issues.
6. Chapter-level summary.

The assistant should not dump a full multi-chapter report into chat when the user has requested file output. The chat response should only summarize what files were created or updated.

---

## 11. Processing Notes Contract

When file extraction, source matching, chapter detection, or formula recognition is imperfect, create or update:

```text
reports/processing_notes.md
```

This file should include:

- requested manuscript path,
- actual manuscript file used,
- reference files used,
- ignored files,
- extraction tools available,
- extraction method used,
- chapter boundary method,
- page-mapping method,
- extraction reliability by chapter if applicable,
- known limitations,
- manual checks required.

---

## 12. Conservative Reporting Policy

Do not flag a statement merely because it is simplified for an introductory chapter.

Report it only if:

- it is scientifically wrong,
- it is dimensionally inconsistent,
- it uses the wrong physical regime,
- it omits an approximation regime essential for correctness,
- it conflicts with another part of the manuscript,
- it makes an outdated current-status claim,
- it overstates what observations or derivations establish,
- or it is likely to mislead a graduate-level reader.

The goal is not to maximize the number of reported issues. The goal is to minimize both false positives and false negatives while preserving scientific correctness.
