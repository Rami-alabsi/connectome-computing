# Project Status

## Current position

**Stage: M4 — Computational abstraction → M5 Synthetic architecture**

Last completed layers:

- [x] M0 Research foundation
- [x] M1 FlyWire/Codex ingestion layer
- [x] M2 Structural graph analysis
- [x] M2b Motif/null-model foundation
- [x] M3 Biological annotation layer
- [x] M4 Architecture primitives
- [ ] M5 Synthetic connectome generator
- [ ] M6 Architecture simulator
- [ ] M7 Controlled benchmarks
- [ ] M8 Scaling experiments
- [ ] M9 Human-brain reference constraints
- [ ] M10 Neuromorphic/hardware mapping
- [ ] M11 Scientific release

## Active work

**M5 — Synthetic Connectome Generator**

Goal: generate larger computational graphs from measurable biological constraints rather
than copying a fly connectome node-for-node.

Current generator targets:

1. node count;
2. directed edge density;
3. degree distribution;
4. modular organization;
5. recurrence;
6. optional hub structure.

## Work path

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
>>> [M5] Synthetic connectome generator <<< CURRENT
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

## Rules for continuing the project

- Never claim biological validity from generated networks alone.
- Keep observed biological data separate from synthetic data.
- Every architecture claim requires a matched control.
- Every large experiment records seed, configuration, source dataset/version, and metrics.
- Do not treat human brain measurements as a direct scaling factor for the fly.
- Prefer falsifiable hypotheses over narrative similarity.

## Resume point

When returning to the project, start at **M5 — Synthetic Connectome Generator**.
The immediate next task is to implement a configurable modular directed graph generator
and tests for its measurable structural properties.
