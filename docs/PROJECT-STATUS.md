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
- [x] M5 novelty tracking and novelty-gate documentation

### Active

**M5 — Real FAFB validation**

Immediate tasks:

1. Run the pipeline against a real downloaded FAFB v783 resource.
2. Extract observed structural profile from the real connection table.
3. Calibrate a synthetic graph and measure it independently.
4. Compare density, degree, reciprocity, modularity, hub structure and later motif statistics.
5. Add distribution-preserving calibration where first-order probabilities are insufficient.
6. Add controlled ablations for each biological constraint.
7. Re-run targeted literature searches before any novelty claim.

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
>>> [M5] Synthetic connectome generator + real-data validation <<<
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

## Novelty status

**No novelty claim yet.**

The broad project direction is supported by substantial prior art: connectome-constrained
models, generative biological network models, connectomics-derived architecture search,
and neuromorphic fly-connectome implementations all exist.

The potentially distinctive target is the experimentally validated combination of
multi-constraint connectome extraction, scalable synthetic expansion, controlled
ablations, and computational efficiency/scaling measurements. This remains a research
hypothesis until the exact method and results pass the novelty gate documented in
docs/novelty-tracker.md.

## Scientific status

No biological or computational benchmark result is claimed until the corresponding
data and experiment have actually been executed. The sparse generator and calibration
are computational baselines, not validated biological models.

## Resume point

Continue from **M5 — Real FAFB validation**.

When a result appears to satisfy the novelty gate, explicitly raise a **NOVELTY ALERT**
with the exact method/result, supporting evidence, closest prior art checked, and
remaining limitations.
