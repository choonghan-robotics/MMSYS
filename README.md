# MultiStereo manuscript

This repository is the Overleaf manuscript and the `paper/` Git submodule of
MultiStereo. The uploaded `acmart-primary/` template bundle is preserved unchanged.

## Entry point

- Main document: `main.tex`.
- Compiler: pdfLaTeX, using `latexmkrc` to locate the uploaded ACM class and BST.
- Format: `\documentclass[sigconf,review,anonymous]{acmart}`, as specified by the
  [MMSys 2027 Research Track](https://2027.acmmmsys.org/research-track.html)
  (checked 2026-09-06): two columns, up to 10 pages plus references.
- Bibliography: `references.bib`, with verified primary references and active
  bibliography commands.

In Overleaf, select `main.tex` as the **Main document** if it is not selected
automatically; the uploaded bundle also contains sample documents. On an authorized
TeX machine, build from this repository's root with `latexmk -pdf main.tex`.
The 2026-09-07 working draft is built on E12 using CPU-only Docker with the ACM
font dependencies. The parent repository contains `docker/paper/Dockerfile`.
The R4 results snapshot is preserved separately; R5 edits its language using
the supplied reference. The corresponding dated `PAPER_BUILD_R*.json` receipts
under `experiments/nonrig_completion_20260907/` record the build outcome,
source, image and PDF hashes, and remaining warnings. A planned revision is
not considered built until its receipt reports success. Neither a successful
build nor this draft is submission acceptance.

R6 introduces the author's logical-first priority and the first process-isolated
screen, including its initialization-stage thermal stop. Its build receipt and
source archive are under `experiments/logical_partition_20260907/` in the parent
repository. Earlier R4/R5 build records and scientific failures are preserved.

R7 adds verified embedded-context preparation, the complete 1/2/3/6-process
short comparison, and the later single-process sustained numerical failure.
Only 2×3 met all short timing gates. The paired sustained campaign stopped
before any long concurrent trial or new camera trial. Its build must be
checked against `PAPER_BUILD_R7.json`; no successful submission or runtime
qualification is implied by this revision.

R8 adds the separate userspace-shim comparison and kernel-managed buffer-sync
follow-up. Each runtime produced a preserved error, independently confirmed
on CPU-only E12. Neither remedy is described as successful. Its build record
is `experiments/xdna_sync_recovery_20260907/PAPER_BUILD_R8.json` in the parent
repository. Local editing and compilation do not publish changes to Overleaf.

R9 includes driver-free matched Python/C++ controls, the rejected zero-filter
output graph, the opt1 logical short pass followed by a sustained raw error,
and separate T3 compilation/opaque-replay procedures. The periodic-monitor
T3 replay reached 29.0--29.167 FPS per logical stream with exact checked
outputs, but failed the frozen timing gates and did not enter long testing.
The original thermal, checker, and timing failures are preserved separately.
The build authority is `experiments/xdna_driver_free_20260908/PAPER_BUILD_R9.json`
in the parent repository; R9 is built only if that receipt reports success.
It is not submission-ready and has not been published to Overleaf.

R10 specifies the matched host-scheduling comparison. R11 reports its completed
conditional path and changes the working title to *One NPU, Six Stereo Streams:
Integrity-Aware Multiplexing for Real-Time Multi-Camera Depth*. With complete
worker-thread affinity, the 2×3 logical configuration passes four short
conditions and three 600-s repetitions. The 3×2 configuration misses
the p99 gate, and the joint T3 family stops after a preserved raw-output error.
R11 also records the separate phase-routed FP32 accuracy result and the failed
Conv--ReLU--Add zero-CPU conversion gate; no XINT8 or board result is claimed
for that new model.

R14 records the completed direct-QAT and hardware-consistent-QAT rescue as
negative evidence. The hardware-consistent graphs have exact train-to-export
metrics but fail the OAK development comparison, so neither graph is promoted
to board execution. R14 also adds primary related work on video-DNN serving,
preemptible NPU scheduling, and physical accelerator fission. Its authoritative
build is the E12 CPU-only, network-disabled Docker receipt
`experiments/phase_routed_qat_rescue_20260909/PAPER_BUILD_R14.json` in the parent
repository. The receipt, not a local editor build, determines whether the ACM-font
PDF passed the page, citation, reference, font, and visual checks. This remains an
evidence-limited working paper because final-set and six-physical-camera results
are not available.

R15 closes the execution-specialized funnel and the common-model runtime
controls. All eight specialized FP32 candidates pass the exposed OAK gate, but
all eight exact-XINT8 candidates fail bad3; no candidate reaches board timing or
the sealed final set. The separate common C6-HWGT control validates pair and
joint organizations at four streams, while both six-stream organizations screen
out in unrepeated 10-second conditions. C1 pair passes, C2 pair is integrity-negative,
and C2 joint remains a technical limitation after its authorized retry. The
working title is now *Scaling Stereo Streams on One NPU: Integrity-Aware
Characterization of Runtime Organizations*. The final isolated CPU-only build
uses the ACM Libertine/NewTX fonts, is nine pages, and passes the page, font,
reference, box, and visual-layout checks. Canonical R3 conclusions and the R15
build receipt live under
`experiments/specialized_six_models_20260909/board_common_controls_recovery_r3/`
in the parent repository.

R16 applies a final evidence-cross-checked wording pass. It makes the replay
gate complete, records the 3-ms jitter and R2 provenance of the partial C2-joint
measurements, defines each C$n$ joint graph, and narrows cross-row latency,
energy, and temperature interpretation to the conditions actually recorded.
Its authoritative build is `PAPER_BUILD_R16.json` beside the R15 receipt.

## Draft and evidence policy

Use [WRITING_GUIDE.md](WRITING_GUIDE.md) for the author's requested vocabulary
and sentence structure. The supplied Lee and Yim (2024) paper was inspected
as a prose reference; its technical content is not evidence for this study.

The manuscript is a preliminary methods/results draft, not a completed paper.
Its primary comparison is T1 sequential serving, T2L process-isolated logical
partitioning, and T3 joint execution, with all six stereo cameras assigned
to one XDNA NPU. Physical partitioning is an optional extension; historical
T2 experiment labels are preserved and are not T2L success evidence.
The 30 FPS per-camera and
better-than-camera-default accuracy targets must not be written as achieved
results before validation. Logical sessions, replay streams, development-set
accuracy, and physical six-camera measurements must remain explicitly distinct.

The parent repository's `docs/SUBMISSION_PLAN_MMSYS2027_20260831.md` is the current
submission-plan authority. Its older `docs/PAPER_OUTLINE_MMSYS2027.md` contains a
superseded 4+2 headline and is not the current scope. Refer to dated experiment
receipts for actual results, rather than copying status summaries into the paper.
Check the venue's generative-AI disclosure policy before submission.

## Synchronization

Overleaf tracks `main`. From the parent MultiStereo checkout:

```bash
bash tools/sync_paper.sh pull
# Edit manuscript files, or fetch edits made in Overleaf with the command above.
git -C paper add main.tex references.bib
git -C paper commit -m "paper: update manuscript"
bash tools/sync_paper.sh sync
git add paper
git commit -m "paper: update Overleaf revision"
git push origin master
```

The helper refuses uncommitted manuscript changes and non-fast-forward merges;
it never force-pushes, commits other project files, or rewrites history. It disables
plaintext credential storage and permits an in-memory credential cache. If Git
asks for a password, enter an Overleaf Git authentication token; never put a token
in the remote URL or a tracked file. No periodic background synchronization is
installed. See `docs/PAPER_WORKFLOW.md` in the parent repository for details.
