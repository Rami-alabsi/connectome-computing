# Roadmap

**Current operational project state and milestone truth live in `docs/MASTER-COMPASS-2026-10-12.md`.**

Read that compass first, then the relevant run-specific record under `docs/experiments/`. Use `docs/PROJECT-STATUS.md` as the historical experiment ledger; older dated summaries are provenance and must not override newer verified run audits.

Immediate sequence:
1. Monitor active C2 128E continuation Run #56 (ID `38204750622`) until completion; do not dispatch competing long runs.
2. Audit final counters, fingerprints, all seven invariants, artifact, and full-curve drift against 8E/16E/32E/64E.
3. Keep the synthetic C2 small-effect sensitivity ladder (draft PR #7) separate and unexecuted until Run #56 is audited and Actions capacity is clear.
4. Continue C3-A synthetic/external-family validation; no full FAFB C3 until its gates pass.
5. Revisit Gate C only after the required biological controls, mixing/sensitivity evidence, and limitations are reviewed.

Historical milestone structure is preserved in Git history. Do not infer current completion status from older roadmap text.
