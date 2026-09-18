# Final build audit — 2026-09-18

## Build command

Isolated Docker build, no network, read-only source mount, deterministic
`SOURCE_DATE_EPOCH` bound to the commit timestamp:

```
docker run --rm --network none --user 1000:1000 --cap-drop ALL \
  --security-opt no-new-privileges --cpus 2 --memory 2g \
  --entrypoint /bin/sh -v <source>:/paper:ro -v <output>:/output -w /output \
  -e SOURCE_DATE_EPOCH=<commit_ts> -e FORCE_SOURCE_DATE=1 \
  -e TEXINPUTS=.//:/paper//: -e BIBINPUTS=.:/paper: \
  multistereo-paper:20260910-r15-local \
  -c 'cp -a /paper/. /output/ && latexmk -pdf -interaction=nonstopmode main.tex'
```

Toolchain: `multistereo-paper:20260910-r15-local` (image digest `sha256:1bbac043ad87…`),
`latexmk` driving `pdflatex` + `bibtex`/`biber` to a fixed point, `acmart` class.

## A real defect found and fixed by this audit step

The first build attempt on the manuscript as pulled from Overleaf failed to resolve: **every**
citation and **every** internal cross-reference in the document (`\ref`, `\cite`, section labels,
figure/table labels — all of them, not a subset). Root cause, found in the raw log at
`! Missing $ inserted.` around line 300: the sentence added by the prior post-agent audit pass

```
...computed before display rounding from 50.35432$-$41.51051$=8.84381, that is 98.0\%...
```

opens a third, unmatched `$` (`$=8.84381,`) after the balanced `$-$`, putting the rest of the
document into unterminated math mode. `pdflatex` recovers locally but the resulting `.aux` file is
corrupted for the remainder of the run, so `bibtex`/`biber` and every reference resolve against a
broken auxiliary file. This would not have been caught by the scope-authorization check (a purely
textual diff) or by resolutions.json bookkeeping — only an actual compile catches it, which is the
reason this step exists.

**Fix**: closed the mode properly as a single expression, `$50.35432-41.51051=8.84381$`. Rebuilt;
zero undefined citations, zero undefined references, both confirmed against the final pass's own
log, not the cumulative multi-pass log (which always shows transient undefined-reference warnings
before the second/third `latexmk` pass resolves them — the correct check is the *last* pass).

## Results after the fix

| Check | Result |
|---|---|
| LaTeX fatal errors | 0 |
| Undefined citations (final pass) | 0 |
| Undefined references (final pass) | 0 |
| Duplicate labels | 0 (none reported) |
| Missing figures | 0 (`fig/arch.tex`, `fig/path_a.tex`, `fig/trade.tex`, `fig/quad_cam.png` all resolved) |
| Overfull `\hbox` (final pass) | 0 |
| Bibliography | Generated; `natbib`/ACM-Reference-Format, all ~40 keys resolve |
| Page count | 13 (body through page 10, references start page 11 — within "10 pages plus references") |
| Final PDF SHA-256 | `dddf3d7748556b9f67d6ef66f99e12c950e0ec897d42353e6599d61b5138bfdf` |

## Figure visual check (rendered at 70–90 DPI, inspected)

- **Fig. 1** (`fig/quad_cam.png`, page 1): renders cleanly, legible at print size, no clipping.
- **Fig. 2** (`fig/arch.tex`, page 8): renders cleanly; S5 and S11d labels are both legible and
  distinct, matching the caption's explicit statement that S11 itself is a different (soft-argmax)
  artifact from the pictured S11d screen variant.
- **Fig. 3(a)/(b)** (`fig/path_a.tex` + `fig/trade.tex`, page 10): both panels legible, no text
  clipping, classical-profile band explicitly captioned as "not a confidence interval or a shared
  admission threshold" (matches E13's requirement that it not be mislabeled as a CI).
- **Table 2** (`tab:sustained`, page 8): all thirteen rows render inside the column width, no
  overflow.

## Remaining limitations (carried from resolutions.json, not resolved by this build step)

- **E07 (QUALIFIED)**: the manuscript's canonical BFP recovery value (8.844, from unrounded
  50.35432−41.51051) and `fig/trade.tex`'s plotted panel_b point for the same quantity
  (41.51299…, vs the canonical 41.51051) differ by 0.002pp. The figure generator chain was not
  traced in this pass; the generated `.tex` bytes were not hand-edited per instruction.
- **E13 (QUALIFIED)**: same underlying gap as above — figure and prose are not yet confirmed to
  come from one canonical source for this one point. Every other figure/prose numeric claim checked
  in this and the prior pass matched exactly (pooled frame counts, classical-profile band values,
  S5-under-T2L single-window count).
- **E03's specific internal-validation-split bad3 range** (19.988–36.355% → 11.410–13.838%) has no
  located source file in this repository as of this pass, though the surrounding claim (0/8
  candidates pass export-stage admission) is independently confirmed from all 8 candidates' real
  `ADMISSION.json` records.
- Evidence provenance is real but partial: 11 of the distinct cited files are committed to
  `git@github.com:ETRI-OAC/Multi_Stereo.git` at commit `c0b2b3db3c60ea66794784fd9456db6b5e615947`
  (repository + commit + path, independently resolvable by a third party with access to that
  repository). The remainder sit under that repository's own `experiments/*/*/` `.gitignore` rule
  (bulk per-candidate exports and admission dumps) and are recorded as local-filesystem SHA-256
  attestations with that limitation stated, not force-added against the project's own exclusion
  policy.
- This audit did not have access to, and did not attempt to create, a pull request against
  `choonghan-robotics/MMSYS` on GitHub — this session's paper submodule tracks an Overleaf git
  bridge (`git.overleaf.com`), not that repository, and no credentials or remote for it were
  available. The verified `main.tex` and `_mmsys_editorial/` changes were pushed directly to the
  Overleaf project instead, which is this session's actual delivery channel.

## Submission readiness

All E01–E13 items are closed (11 VERIFIED, 2 QUALIFIED with disclosed, non-fabricated residual
gaps; 0 OPEN). The build is clean. The two QUALIFIED items are both small (≤0.002pp / one unlocated
secondary source), do not affect any headline claim, and are stated plainly rather than hidden.
Whether that residual risk is acceptable for submission is the authors' call, not this audit's.
