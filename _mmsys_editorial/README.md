# MMSys editorial synchronization

- Main manuscript: repository-root `main.tex`.
- Existing `fig/`, bibliography, and LaTeX project assets are preserved.
- Editorial/logical corrections are synchronized; experiment reconciliation is tracked in `handoff/resolutions.json`.
- Full end-to-end pass status (2026-09-18): **11 VERIFIED, 2 QUALIFIED (E07, E13), 0 OPEN**.
- QUALIFIED means the current wording is intentionally bounded but the evidence chain is not yet independently reproducible from this GitHub repository alone.
- Most evidence files (11 of ~20 distinct citations) are now committed to `git@github.com:ETRI-OAC/Multi_Stereo.git` at `c0b2b3db3c60ea66794784fd9456db6b5e615947`, with repository+commit+path recorded per file in `handoff/resolutions.json`. The remainder sit under that repository's own `experiments/*/*/` .gitignore rule (bulk per-candidate exports); they are recorded there as local-filesystem SHA-256 attestations with that limitation stated, not silently force-added.
- See `handoff/POST_AGENT_AUDIT.md` for the remaining release blockers and `handoff/FIGURE_REVIEW.md` for figure-specific notes.
