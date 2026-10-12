# AI Context

**Current operational source of truth:** read `docs/MASTER-COMPASS-2026-10-12.md` first. It captures the verified C2 64E Run #55 state, current drift interpretation, gate status, and authorized next sequence. Then read the relevant run-specific record under `docs/experiments/`.

`docs/PROJECT-STATUS.md` is the historical experiment ledger. Its older narrative sections and prior dated summaries preserve provenance; when a summary conflicts with the latest dated compass or a newer run-specific audit, use the newer verified evidence and update documentation rather than guessing.

Persistent operating rules:

- Do not restart the project or invent results.
- Biology is evidence, not specification.
- Separate biological observations, synthetic structures, hypotheses, implementation validation, and scientific results.
- Every claimed advantage requires matched controls and ablations.
- Record dataset/version, configuration, seed, metrics, fingerprints, artifacts, and transformations.
- Never claim an experiment passed without an executed artifact or verified CI result.
- Keep large biological data out of Git.
- Avoid O(N^3) algorithms on full connectomes.
- Label sampling and transformations clearly.
- Keep the primary C2 constraint surface/kernel fixed; any stronger null is a separately named sensitivity family.
- Update the compass and experiment ledger when project state changes.
- Do not close Gate C or make architecture/commercial claims from descriptive curve stability or edge overlap alone.
