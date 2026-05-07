# Sample Errata Report

## Scope

- Manuscript under review: `examples/input/sample_equations.tex`
- Reference sources: standard photon energy relation
- Review unit: sample equation
- Date: 2026-05-07

## Issues

### Issue CH01-001 — sample_equations.tex / Photon energy relation

**Original formula or statement**

```tex
E = \frac{h}{\lambda}
```

**Problem type**

- `formula_error`
- `dimensional_inconsistency`

**Severity**

- `major`

**Extraction reliability**

- `high`

**Verification method**

- `dimensional_analysis`
- `first_principles_derivation`

**Evidence / sources**

- Manuscript: `examples/input/sample_equations.tex`
- Source basis: derivation from $begin:math:text$E\=h\\nu$end:math:text$ and $begin:math:text$\\nu\=c\/\\lambda$end:math:text$.
- Notes: No external source is required for this elementary relation.

**Re-derivation / check**

Photon energy is

```tex
E = h\nu .
```

For a photon of wavelength $begin:math:text$\\lambda$end:math:text$,

```tex
\nu = \frac{c}{\lambda}.
```

Therefore,

```tex
E = h\nu = \frac{hc}{\lambda}.
```

The original expression $begin:math:text$E\=h\/\\lambda$end:math:text$ is dimensionally inconsistent because $begin:math:text$h\/\\lambda$end:math:text$ has dimensions of momentum, not energy.

**Judgement**

Confirmed error.

**Corrected formula or statement**

```tex
E = \frac{hc}{\lambda}
```

**Suggested replacement prose**

Replace the original formula with $begin:math:text$E\=hc\/\\lambda$end:math:text$. If natural units are used, explicitly state $begin:math:text$c\=1$end:math:text$ before writing $begin:math:text$E\=h\/\\lambda$end:math:text$, though this is not standard SI notation.

**Human-review note**

Verify whether the surrounding text states a natural-unit convention. If no such convention is stated, the correction is required.

**Confidence**

High.

## Chapter Summary

- Confirmed errors: 1
- Likely errors: 0
- Convention-dependent issues: 0
- Clarification-only issues: 0
- Extraction limitations: None for this synthetic example.
- Highest-priority corrections: Correct the photon energy formula.
- Manual checks required: Check whether the source text declares natural units.
- Overall judgement: The sample contains one deliberate formula and dimensional error.
