# Sample Errata Report

## Scope

- Manuscript under review: `examples/input/sample_equations.tex`
- Reference sources: standard photon energy relation
- Review unit: sample equation
- Date: 2026-05-07

## Issues

### Issue CH01-001 — sample_equations.tex / Photon energy relation

**Original formula or statement**

    E = \frac{h}{\lambda}

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
- Source basis: derivation from `E = h\nu` and `\nu = c/\lambda`.
- Notes: No external source is required for this elementary relation.

**Re-derivation / check**

Photon energy is

    E = h\nu .

For a photon of wavelength `\lambda`, the frequency is

    \nu = \frac{c}{\lambda}.

Therefore,

    E = h\nu = \frac{hc}{\lambda}.

The original expression `E = h/\lambda` is dimensionally inconsistent because `h/\lambda` has dimensions of momentum, not energy.

**Judgement**

Confirmed error.

**Corrected formula or statement**

    E = \frac{hc}{\lambda}

**Suggested replacement prose**

Replace the original formula with `E = hc/\lambda`. If natural units are used, explicitly state `c = 1` before writing `E = h/\lambda`, though this is not standard SI notation.

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
