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

### Active

**M5 — Generator validation against biological structure**

Immediate tasks:

1. Run the calibration against a real downloaded FAFB resource.
2. Measure the generated graph.
3. Compare generated vs observed density, degree, reciprocity, modularity and hub statistics.
4. Add a discrepancy report.
5. Add better distribution-preserving calibration where first-order probabilities are insufficient.

### Work path

```text
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
>>> [M5] Synthetic connectome generator + validation <<<
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
```

## Scientific status

No biological or computational benchmark result is claimed until the corresponding
data and experiment have actually been executed. Generator calibration is currently
a baseline hypothesis.

## Resume point

Continue from **M5 — Generator validation against real FAFB data**.
