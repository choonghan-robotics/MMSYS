# Post-agent audit — canonical status

## Status

- VERIFIED: E01, E02, E04, E05, E06, E08, E09, E11, E12
- QUALIFIED: E03, E07, E10, E13
- OPEN: none

This status is canonical for future handoffs.

## Why E03 remains QUALIFIED

The eight exported artifacts' admission records independently confirm the reported 0/8 exported-model accuracy admission result. However, the requested candidate-level FP terminal → QAT initial → QAT terminal → export linkage was not reconstructed, and the exact source for the internal-validation bad3 range 19.988–36.355% → 11.410–13.838% was not located. The manuscript's scoped wording is safe; the evidence chain is incomplete.

## Why E07 remains QUALIFIED

The manuscript's BFP recovery amount is kept at 8.844 pp, based on higher-precision values 50.35432 and 41.51051 (difference 8.84381 before display rounding). The figure record cited by the prior agent uses about 41.51299 for the plotted R6 permuted point, leaving an approximately 0.002 pp figure/prose provenance discrepancy. Do not hand-edit generated figure values; reconcile the generator/input source instead.

## Why E10 remains QUALIFIED

For the first decoder attempt, 45/256 wins gives raw exact two-sided sign-test p≈7.028e-27. The complete Holm family for that first attempt is not archived here, so main.tex correctly reports raw p only and asserts no adjusted p. The second decoder attempt's reported Holm range was separately verified against its decision table.

## Why E13 remains QUALIFIED

The figure/prose canonical-source discrepancy for the R6 permuted point remains. Other checked figure counts/labels are consistent, but this one point is not yet generated from a single documented canonical source.

## Final build

The full project build was completed successfully after fixing the malformed BFP math expression. The recorded final build has:
- LaTeX fatal errors: 0
- undefined citations on final pass: 0
- undefined references on final pass: 0
- duplicate labels reported: 0
- missing figures: 0
- overfull hboxes: 0
- page count: 13 total, body through page 10, references start page 11
- PDF SHA-256: dddf3d7748556b9f67d6ef66f99e12c950e0ec897d42353e6599d61b5138bfdf

## Paper repository policy

The paper repository is **not** encoded by historical repository references in this handoff.
Future agents must use only:

TARGET_PAPER_REPOSITORY=__USER_INPUT__
BASE_BRANCH=__USER_INPUT__

supplied by the user. Evidence repositories and Overleaf remotes are not automatically paper repositories.
