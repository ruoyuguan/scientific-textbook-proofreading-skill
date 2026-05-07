# Synthetic Chapter 1 Errata Report

## Scope

- Manuscript under review: `examples/synthetic_textbook/chapter_01.md`
- Reference sources: first-principles checks and standard high-energy astrophysics conventions
- Review unit: Chapter 1
- Date: 2026-05-07

## Issues

### Issue CH01-001 — Section 1.1 / Photon Energy

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

- Manuscript: `examples/synthetic_textbook/chapter_01.md`, Section 1.1.
- Source basis: photon energy relation from `E = h nu` and `nu = c/lambda`.
- Notes: No external source is required for this elementary relation.

**Re-derivation / check**

Photon energy is

    E = h nu.

For a photon of wavelength lambda,

    nu = c / lambda.

Therefore,

    E = h nu = hc / lambda.

The original expression `E = h/lambda` has dimensions of momentum rather than energy.

**Judgement**

Confirmed error.

**Corrected formula or statement**

    E = \frac{hc}{\lambda}

**Suggested replacement prose**

Replace the original expression with `E = hc/lambda`, unless the text explicitly declares a natural-unit convention with `c = 1`.

**Human-review note**

Check whether the surrounding text declares natural units. If not, the correction is required.

**Confidence**

High.

---

### Issue CH01-002 — Section 1.2 / Inverse-Compton-to-Synchrotron Power Ratio

**Original formula or statement**

    P_IC / P_syn = U_rad / U_B

The text states that this expression is valid at all photon energies.

**Problem type**

- `missing_approximation_regime`
- `wrong_physical_regime`
- `misleading_prose`

**Severity**

- `major`

**Extraction reliability**

- `high`

**Verification method**

- `source_comparison`
- `limiting_case_check`

**Evidence / sources**

- Manuscript: `examples/synthetic_textbook/chapter_01.md`, Section 1.2.
- Source basis: standard inverse-Compton and synchrotron power comparison.
- Notes: The simple ratio applies in the Thomson regime for the same electron population and isotropic fields.

**Re-derivation / check**

For the same electron population, the total inverse-Compton to synchrotron power ratio can be approximated by

    P_IC / P_syn = U_rad / U_B

in the Thomson limit.

At sufficiently high energies, Klein-Nishina suppression modifies the inverse-Compton cross section and the simple ratio no longer applies generally.

**Judgement**

Correct but misleading.

**Corrected formula or statement**

    In the Thomson regime, for the same electron population, the approximate total power ratio is P_IC / P_syn = U_rad / U_B. At high energies, Klein-Nishina effects must be considered.

**Suggested replacement prose**

Add the regime qualifier “in the Thomson regime” and remove the statement that the expression is valid at all photon energies.

**Human-review note**

Check whether a later chapter introduces Klein-Nishina corrections. If so, cross-reference that discussion.

**Confidence**

High.

---

### Issue CH01-003 — Section 1.3 / Gamma-Ray Observations

**Original formula or statement**

    All gamma rays must be detected by space telescopes because Earth's atmosphere is opaque to gamma rays.

**Problem type**

- `misleading_prose`
- `wrong_physical_regime`

**Severity**

- `major`

**Extraction reliability**

- `high`

**Verification method**

- `source_comparison`
- `cross_reference_check`

**Evidence / sources**

- Manuscript: `examples/synthetic_textbook/chapter_01.md`, Section 1.3.
- Source basis: standard distinction between space-based low-to-medium energy gamma-ray detection and ground-based indirect VHE/UHE gamma-ray detection.
- Notes: The atmosphere is opaque to primary gamma rays but enables air-shower-based indirect detection.

**Re-derivation / check**

The statement is correct for X-rays and for low-to-medium energy gamma rays that require space-based instruments. It is misleading for the entire gamma-ray band because very-high-energy and ultra-high-energy gamma rays can be detected indirectly from the ground through atmospheric showers, Cherenkov light, or particle arrays.

**Judgement**

Correct but misleading.

**Corrected formula or statement**

    X-rays and low-to-medium energy gamma rays usually require space-based telescopes. Very-high-energy and ultra-high-energy gamma rays cannot directly penetrate the atmosphere, but they can be detected indirectly from the ground through atmospheric showers, Cherenkov light, or particle arrays.

**Suggested replacement prose**

Replace “all gamma rays must be detected by space telescopes” with a statement distinguishing direct space-based detection from indirect ground-based detection.

**Human-review note**

Check whether the manuscript later discusses H.E.S.S., MAGIC, VERITAS, HAWC, LHAASO, or CTA. If so, ensure the wording is internally consistent.

**Confidence**

High.

---

### Issue CH01-004 — Section 1.4 / IceCube-Gen2 Detector Scale

**Original formula or statement**

    IceCube-Gen2 will increase the detector area to about 8 km^3.

**Problem type**

- `dimensional_inconsistency`
- `unit_system_mismatch`

**Severity**

- `major`

**Extraction reliability**

- `high`

**Verification method**

- `dimensional_analysis`
- `unit_system_check`

**Evidence / sources**

- Manuscript: `examples/synthetic_textbook/chapter_01.md`, Section 1.4.
- Source basis: dimensional analysis.
- Notes: Area must have dimensions of length squared, whereas `km^3` is a volume.

**Re-derivation / check**

An area must be measured in units such as square kilometres, while `8 km^3` is a volume. If the intended quantity is the in-ice instrumented volume, the text should say volume rather than area.

**Judgement**

Confirmed error.

**Corrected formula or statement**

    IceCube-Gen2 will increase the instrumented volume to about 8 km^3.

**Suggested replacement prose**

Replace “detector area” with “instrumented volume” if `8 km^3` is the intended quantity.

**Human-review note**

If the surrounding discussion concerns effective area or point-source sensitivity, give that quantity separately and do not describe it in cubic kilometres.

**Confidence**

High.

## Chapter Summary

- Confirmed errors: 2
- Likely errors: 0
- Convention-dependent issues: 0
- Clarification-only issues: 2
- Extraction limitations: None for this synthetic Markdown example.
- Highest-priority corrections: Correct the photon energy formula and the IceCube-Gen2 dimensional statement.
- Manual checks required: Check whether natural units are declared and whether later sections discuss ground-based gamma-ray facilities or Klein-Nishina corrections.
- Overall judgement: The synthetic chapter contains four deliberate issues and one correct negative-control statement.
