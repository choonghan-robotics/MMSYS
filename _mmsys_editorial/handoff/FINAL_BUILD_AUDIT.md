# Final build audit — 2026-09-18 (submission finalization pass)

Scope of this pass: pre-submission finalization only. No new experiment, no retraining, no new
baseline, and no re-verification of items already closed. Implementation/evidence checks, minimal
manuscript corrections, and the final PDF build.

**Paper repository: not designated.** Per the standing policy in `POST_AGENT_AUDIT.md` and the
user's instruction, the target paper repository and base branch are user-supplied and were not
supplied for this pass. Nothing was pushed anywhere. The changes below exist as an uncommitted
working-tree diff against source commit `3868891dd8cb71fc5276fcd3259af613ff0a2d3d`.

## 1. Queue implementation — checked against code, manuscript corrected

Read directly: `tools/rbq_sustained_replay_npu.py` (replay), `tools/rbq_e3_npu.py` and
`src/stereort/e3_frame_ring.py` (physical).

| Question | Finding in code |
|---|---|
| FIFO or latest-only? | **FIFO.** Replay: `pending[served].popleft()`. Physical: `RingReader.pending()` returns the oldest unserved sequence. Neither path takes "the latest pair". |
| Cross-stream selection | Oldest-first by capture stamp. Replay: `min` over each non-empty stream's **head** frame `captured_at`, ties broken by a rotating index. Physical: the stream whose pending frame has the smallest `capture_monotonic`. |
| `popleft` or `pop` on overflow? | **`popleft`** — the **oldest** queued frame is discarded, not the newest. |
| Overflow accounting | Discard increments `replaced[sid]`; the physical reader increments `self.replaced` by the number of sequences the producer overwrote past the bound (`oldest - next_sequence`). Both feed the acceptance policy's replacement rate. |
| Queue-wait timestamp | Replay: `queue_ms = dequeued - frame["captured_at"]`, and `captured_at` is the frame's **scheduled** arrival (`next_capture[sid]`), so the interval includes dispatch lag. Physical: `queue_ms = dequeued - published_at` (ring publication instant), with `usb_ms = published_at - captured_at` reported separately. |

**Manuscript correction (minimal).** The T1 sentence said a round-robin scheduler "takes the
**latest** pair from each non-empty camera slot" — contradicted by the code in both paths. Rewritten
to state oldest-pending selection by earliest capture stamp with rotation as the tie-break and FIFO
dequeue. The queue sentence now also states FIFO service, oldest-frame discard, the physical
reader's equivalent bound, and the two queue-wait timestamp definitions. **No measured value was
changed or removed**; the 234–242 ms mean host-side wait stands exactly as reported.

## 2. E03 — the bad3 range is sourced; grammar fixed

The range **19.988–36.355% → 11.410–13.838%** was located exactly. It is the **KITTI 2015
`native_bad3_macro_median_percent`** on the campaign's **63-pair internal validation split** (28
KITTI-2015 + 35 KITTI-2012 pairs), across the eight seed-0 candidates, moving from the
quantization-aware phase's **initial validation** to its **terminal epoch**:

| candidate | QAT initial | QAT terminal |
|---|---:|---:|
| S6-H128 | 30.1135 | 12.0137 |
| S6-H96 | 24.0138 | 12.7407 |
| S6-H64 | 20.3407 | 13.8382 |
| L6-H256 | 27.6546 | 11.4102 |
| L6-H192 | **36.3546** | 11.8624 |
| L6-H128 | **19.9879** | 11.9562 |
| J6-H128 | 27.9673 | 12.7239 |
| J6-H96 | 26.4613 | 12.0448 |

Sources: `experiments/specialized_six_models_20260909/qat/<candidate>/seed0/TERMINAL.json`
(`initial_validation`) and the terminal record of the matching `history.jsonl` (epoch 63
`validation`). Both printed endpoints reproduce exactly. The sentence was therefore **kept and made
explicit** about stage, split and aggregation rather than deleted.

**8/8 full-precision admission — confirmed**, not assumed:
`fp32_development/<candidate>/seed0/ADMISSION.json` reports
`fp32_development_oak_gate_passed: true` with both per-dataset gates true for all eight candidates.

**Grammar**: `"... exceeded its bad3 median, Thus, ..."` → `"... exceeded its bad3 median. Thus, ..."`.

Remaining E03 gap: the full per-candidate **FP terminal → QAT initial → QAT terminal → export**
linkage in one table is still not assembled (the export stage lives in a different record against a
different population). E03 therefore stays **QUALIFIED**, not promoted.

## 3–4. Fig. 3(b) — caption corrected, and the "discrepancy" was not one

`FIGURES_R1.json` `/figures_in_the_manuscript[1]/derived/panel_b` stores **two values per artifact**
(`sf` synthetic, `ds` driving) and a four-value classical band (SceneFlow 41.6826/42.5851,
DrivingStereo 41.8262/46.8659). The panel plots the two populations **separately**; the old caption's
"macro-averaged over the 512-pair development population" implied a single merged population.
Corrected to name the 256-pair synthetic and 256-pair driving populations separately. The band's
"not a confidence interval or a shared admission threshold" limitation is retained verbatim.

**The previously recorded ~0.002 pp figure/prose discrepancy does not exist.** Checked by condition
rather than by value: `panel_b`'s `records_read` are
`permutation_npu512_opt3_r1/output/RESULT.json` and
`permutation_opt3_actual_dev_r1/output/DEVELOPMENT_000000.json`, both carrying
`"optimize_level": 3` and the value `41.51299370659722`. The prose's 41.51051 is the **level-1**
silicon measurement. Different optimization levels, same artifact — not a same-condition mismatch,
so nothing was unified. A short caption clause now says panel (b) is level 3, so a reader does not
repeat the comparison. The BFP arithmetic (50.35432 − 41.51051 = 8.84381 → 8.844 pp, 98.0%) is
untouched.

## 5. Architecture figure — caption corrected, figure untouched

`tools/rbq_fig_architecture.py` reads the drawn stages, shapes and kernel extents **off the S11
graph** (`splits['S11']`, `geom['S11']`, "Shapes and kernel extents read off the S11 graph"), then
annotates S5 and S11d as the two variants that differ. So **S11 is the pipeline shown**, and the
prior claim that the figure omits S11 was wrong. Caption now reads "Speed-line soft-argmax pipeline
with the S5 and S11d modifications indicated…", and the matching prose sentence was corrected the
same way. No figure source byte was edited.

## 6. Final build

Same isolated toolchain as before: `multistereo-paper:20260910-r15-local`, `--network none`,
`--read-only` source mount, `SOURCE_DATE_EPOCH` bound to the source commit, `latexmk -pdf` to a
fixed point with the real `fig/`, `references.bib` and ACM class assets.

| Check | Result |
|---|---|
| LaTeX fatal errors | 0 |
| Undefined citations (final pass) | 0 |
| Undefined references (final pass) | 0 |
| Duplicate/multiply-defined labels | 0 |
| Missing figures | 0 |
| Overfull `\hbox` | 0 |
| Bibliography | generated, 49 entries |
| Total pages | 13 |
| References start | page 11 |
| Table overflow | none (Table 1 and Table 2 render inside the text block) |
| Fig. 1 / 2 / 3 | rendered and inspected; legible, no clipping |
| PDF metadata | no `Author` field; no author-identifying string (`pdfinfo` scan for name/affiliation/e-mail returns 0 hits) |
| **Final PDF SHA-256** | `b05210e960cc1153692e92851ad71dd99deed0f5239f46552d6f07d8adc8283a` |

This hash is newly issued for this build; the earlier
`dddf3d77…` hash belongs to the previous pass and is superseded.

### Page-budget finding (unresolved, authors' decision)

**The body does not fit in 10 pages, and did not before this pass either.** With the references
beginning on page 11, roughly 1.5 columns of body text (the tail of Limitations and the Conclusion)
sit above them on that page:

- source commit `3868891` as pulled: **88** body lines on page 11 before the first reference;
- after this pass's corrections: **94** body lines — a net `+519` characters, about six lines.

So the overflow is pre-existing and this pass added ~7% to it while fixing four factual errors. I
did not cut content to force the fit: length decisions were reserved by the authors. To land the
body inside 10 pages, about 1.5 columns must come out; the Limitations paragraph and the R6
execution-cost subsection are the largest compressible blocks.

One float-packing note, in case the text is edited further: at the source commit, Table 2 and
Figure 2 pack together on page 8. Adding roughly 800 characters anywhere before them splits that
pair across pages 8 and 9 and costs a full page, pushing the references to page 12. The corrections
in this pass were compressed until that packing was restored.

## Verification ledger

Unchanged by this pass: **9 VERIFIED, 4 QUALIFIED (E03, E07, E10, E13), 0 OPEN**, as recorded in
`POST_AGENT_AUDIT.md`. Two of this pass's findings bear on that ledger and are recorded here rather
than used to promote anything:

- **E07/E13's figure–prose gap is explained** (level 3 vs level 1, same artifact), which removes the
  stated reason for the discrepancy but does not by itself establish single-canonical-source
  generation, so neither item is promoted here.
- **E03's internal-split range is now sourced exactly**, but the full FP→QAT→export candidate
  linkage is still not assembled, so E03 stays QUALIFIED.

## Submission readiness

**Not ready as-is — one blocking item: the body exceeds the 10-page limit** (see above). Every other
mechanical check passes: clean build, no undefined references or citations, no overfull boxes,
figures legible, anonymous metadata. Once ~1.5 columns are removed from the body, the same build
procedure reproduces a submittable PDF.
