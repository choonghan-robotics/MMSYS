# MMSys editorial synchronization

- Main manuscript filename: `main.tex`.
- Existing `fig/`, bibliography, and LaTeX project assets are preserved.
- Editorial/logical corrections are synchronized; experiment reconciliation is tracked in `handoff/resolutions.json`.
- Canonical audit status (2026-09-18): **9 VERIFIED, 4 QUALIFIED (E03, E07, E10, E13), 0 OPEN**.
- The full project build is clean: 0 fatal LaTeX errors, 0 unresolved citations/references on the final pass, 0 overfull hboxes, 13 total PDF pages with body through page 10 and references from page 11.
- QUALIFIED means the current manuscript wording is bounded enough to retain, but the evidence chain for that item is not complete enough to label independently VERIFIED.
- Evidence repository/provenance is separate from the paper repository. Some evidence is pinned to `ETRI-OAC/Multi_Stereo`; that does **not** designate it as the paper repository.
- **Future paper-repository location is user-specified only.** Agents must use `TARGET_PAPER_REPOSITORY` and `BASE_BRANCH` supplied by the user and must not infer a paper repo from this file, previous chats, evidence repositories, or Overleaf remotes.
- See `handoff/POST_AGENT_AUDIT.md`, `handoff/FINAL_BUILD_AUDIT.md`, and `handoff/FIGURE_REVIEW.md`.
