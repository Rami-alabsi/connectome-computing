# Project Status

## Current position

**Stage: M5 — Synthetic Connectome Generator**

### Completed

- [x] M0 Research foundation
- [x] M1 FlyWire/Codex ingestion layer
- [x] M2 Structural graph analysis
- [x] M2b Motif/null-model foundation
- [x] M3 Biological annotation layer
- [x] M4 Architecture primitives
- [x] M5 modular directed synthetic generator
- [x] M5 structural profile model
- [x] M5 first-order biological-profile calibration
- [x] M5 profile comparison/discrepancy layer
- [x] M5 scalable sparse generator baseline
- [x] M5 degree-distribution and hub metric layer
- [x] M5 novelty tracking and novelty-gate documentation
- [x] M5 literature-to-design-rule matrix
- [x] M5 literature review checkpoint

### Active

**M5 — Real FAFB validation + multi-constraint generator design**

Immediate tasks:

1. Run the pipeline against a real downloaded FAFB v783 resource.
2. Extract the observed structural profile.
3. Compare in/out degree distributions and hub statistics.
4. Add modularity and short/long-range structure.
5. Add spatial/distance/contact constraints.
6. Compare synthetic vs observed using independent validation metrics.
7. Add constraints one at a time with ablations.
8. Perform another targeted prior-art search once the exact method stabilizes.
9. Continue toward M6 with topology and dynamics kept as separate experimental factors.

### Scientific checkpoint

A 2025 Network Neuroscience study comparing fly, mouse, and human connectomes found
that degree sequence alone does not recover spatial structure, while distance constraints
alone do not recover broad degree distributions and hubs. Its scalable maximum-entropy
models combine these constraint families and recover additional properties such as
graphlets.

A separate 2025 study reports that long-range connectivity and hub topography can remain
poorly captured even when conventional topology metrics look similar. We therefore will
not accept aggregate degree or modularity matching as sufficient validation.

### Work path

[M0] Research foundation
  |
  v
[M1] FlyWire ingestion
  |
  v
[M2] Graph statistics
  |
  v
[M2b] Motifs + null models
  |
  v
[M3] Biological context
  |
  v
[M4] Architecture primitives
  |
  v
>>> [M5] Synthetic generator + multi-constraint validation <<<
  |
  v
[M6] Computational simulator
  |
  v
[M7] Controlled benchmarks + ablations
  |
  v
[M8] Scale 10K -> 100K -> 1M -> ...
  |
  v
[M9] Human-brain reference constraints
  |
  v
[M10] Neuromorphic/hardware mapping
  |
  v
[M11] Reproducible scientific release

## Scientific status

No biological or computational benchmark result is claimed until the corresponding
data and experiment have actually been executed.

## Novelty status

**No novelty claim yet.**

Relevant literature is treated as design constraints. See:

- docs/literature-review-2026-09-22.md
- docs/literature-to-design-rules.md
- docs/novelty-tracker.md
- docs/degree-and-hub-metrics.md

A **NOVELTY ALERT** is only raised when the exact method/result survives a targeted
prior-art check and reproducible experiments with controls and ablations.
