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
- [x] M5 hierarchical generator baseline
- [x] M5 spatial wiring-cost and distance-decay baseline
- [x] M5 rich-club metric layer
- [x] M5 2026 neuroscience literature checkpoint
- [x] M5 novelty tracking and novelty-gate documentation
- [x] M5 literature-to-design-rule matrix
- [x] M5 literature review checkpoint
- [x] M5 capacity-triggered hierarchy prototype

### Active

**M5 — Real FAFB validation + multi-constraint generator design**

Immediate tasks:

1. Run the pipeline against a real FAFB v783 resource.
2. Extract the observed structural profile.
3. Compare in/out degree distributions and hub statistics.
4. Add modularity and short/long-range structure.
5. Add spatial/distance/contact constraints.
6. Compare synthetic vs observed using independent validation metrics.
7. Add constraints one at a time with ablations.
8. Benchmark bounded-capacity hierarchy against matched controls.
9. Perform another targeted prior-art search once the combined method stabilizes.
10. Continue toward M6 with topology and dynamics kept as separate experimental factors.

### Scientific checkpoint

The current literature supports hierarchical modularity as a computationally relevant structural factor, but not the specific capacity-triggered rule proposed here. A 2026 Nature Communications study generated hierarchical modular networks while preserving size, density, degree and modularity and found benefits for memory, multitasking and temporal dynamics in reservoir models.

Earlier network-growth work already used module-size thresholds/division to generate modular and hierarchical topology. This prevents a novelty claim for threshold-based module growth alone.

Neuromorphic work also shows that memory, sparse activity, communication and hardware resource constraints are practical scaling factors, supporting explicit resource accounting in later benchmarks.

## Scientific status

No biological or computational benchmark result is claimed until the corresponding data and experiment have actually been executed.

## Novelty status

**No novelty claim yet.**

The present capacity idea is explicitly treated as a hypothesis with substantial prior art around hierarchical modular growth. Any future novelty claim must be narrower and evidence-based.

See:
- docs/literature-review-2026-09-22.md
- docs/literature-to-design-rules.md
- docs/novelty-tracker.md
- docs/cross-domain-synthesis-atomic-capacity.md
