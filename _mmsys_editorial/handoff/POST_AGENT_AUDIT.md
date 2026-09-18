# Post-agent audit — 2026-09-18

## Status

After reviewing the agent's result ledger and the merged manuscript:

- VERIFIED: E01, E02, E04, E05, E06, E08, E09, E11, E12
- QUALIFIED: E03, E07, E10, E13
- OPEN: none

QUALIFIED means the manuscript wording is presently conservative enough to keep, but the evidence chain is not yet complete enough to call independently reproducible from this GitHub repository.

## Corrections applied in this audit

1. **E07 — BFP recovery amount**
   - The prior edit changed 8.844 to 8.843 using rounded display values.
   - The prior agent's own ledger records parent=50.35432 and permuted=41.51051.
   - Their difference is 8.84381, which rounds to **8.844**.
   - `main.tex` now reports 8.844 and states that it is computed before display rounding.
   - The 98.0% recovery statement is unchanged.

2. **E10 — sign-test / Holm wording**
   - 45/256 wins gives raw exact two-sided sign-test p≈7.028e-27.
   - That alone does not determine the Holm-adjusted familywise value.
   - `main.tex` now reports the raw p only and does not assert a Holm-adjusted value for this test.

3. **Ledger state consistency**
   - `resolutions.json`, `experiment_tasks.json`, and the editorial README now use the same 9 VERIFIED / 4 QUALIFIED status.

## Remaining release blockers

### E03 — FP → QAT → export phase linkage
Archive a candidate-level table or equivalent primary source showing, on the same population/aggregation:
FP terminal → QAT initial → QAT terminal → exported artifact → comparator.
The prior ledger entry had no evidence_files.

### E07 — exact silicon metric provenance and figure/prose reconciliation
Archive the primary source containing the higher-precision silicon parent/permuted metrics. Reconcile the small difference noted by the prior agent between the prose/high-precision permuted synthetic value (41.51051) and the figure-record value (41.51299).

### E10 — complete Holm family
Provide the full family of raw p-values, ties/win counts, ordering, and Holm step-down results for the decoder comparison family. Then either restore a correct adjusted p-value or keep the raw-only report.

### E13 — figure provenance
Re-run or archive the figure generator inputs for the classical-profile band and the R6 plotted point so that figure and prose are generated from one canonical source.

### Evidence source location
Many evidence paths in `resolutions.json` point to `tools/`, `experiments/`, or `paper/` locations that are not present in the current `choonghan-robotics/MMSYS` GitHub tree. Add a retrievable repository/archive/commit locator for those exact hashed files.

### Final build
Run the full project build with the actual figures and bibliography, inspect the produced PDF, and record:
- LaTeX/BibTeX errors and warnings
- page count
- figure legibility and clipping
- unresolved references/citations
- final PDF hash

Do not call the manuscript release-ready until the four QUALIFIED items and the final build are closed.
