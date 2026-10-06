# AI Context

**Current operational source of truth:** read `docs/MASTER-COMPASS-2026-10-06.md` first for the live project stage, gate state, C2 status, recovery point, and next actions. Then use `docs/PROJECT-STATUS.md` as the historical experiment ledger and for detailed provenance.

This file contains only persistent operating rules:

- Do not restart the project or invent results.
- Continue from the current checkpoint in `docs/PROJECT-STATUS.md`.
- Biology is evidence, not specification.
- Separate biological observations, synthetic structures, hypotheses, implementation validation, and scientific results.
- Every claimed advantage requires matched controls and ablations.
- Record dataset/version, configuration, seed, metrics, and transformations.
- Never claim an experiment passed without an executed artifact or verified CI result.
- Keep large biological data out of Git.
- Avoid O(N^3) algorithms on full connectomes.
- Label sampling and transformations clearly.
- Update `docs/PROJECT-STATUS.md` when the project state changes.

Do not maintain an independent milestone checklist here; that caused stage drift.
