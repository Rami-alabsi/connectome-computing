# Roadmap

## M0 — Research Foundation
**In progress**
- [x] Define project scope and research questions.
- [x] Identify major prior-art categories.
- [ ] Build a continuously updated prior-art log.
- [ ] Document FlyWire/Codex data access and licensing.
- [ ] Define experiment naming and provenance conventions.

## M1 — Connectome Ingestion
- [ ] Select a stable FlyWire/Codex release.
- [ ] Implement data access instructions.
- [ ] Build normalized neuron and edge representations.
- [ ] Preserve biological metadata.
- [ ] Add dataset validation tests.
- [ ] Create a small public test fixture without redistributing restricted data.

## M2 — Structural Analysis
- [ ] Degree and weighted-degree distributions.
- [ ] Reciprocity and connected components.
- [ ] Motif analysis.
- [ ] Rich-club analysis.
- [ ] Community/module detection.
- [ ] Cross-region connectivity.
- [ ] Null-model comparisons.

## M3 — Dynamic Model
- [ ] Define a minimal neuron model.
- [ ] Define synaptic transmission.
- [ ] Define event-driven and time-stepped modes.
- [ ] Validate small subnetworks.
- [ ] Measure compute and memory cost.

## M4 — Computational Abstraction
- [ ] Define processing-unit abstraction.
- [ ] Define sparse communication and local state.
- [ ] Define recurrent feedback primitives.
- [ ] Define module and hub abstractions.
- [ ] Separate biological measurements from engineering assumptions.

## M5 — First Architecture
- [ ] Implement software-first architecture.
- [ ] Support sparse asynchronous communication.
- [ ] Add latency, memory and communication instrumentation.
- [ ] Add deterministic experiment replay.

## M6 — Benchmark Suite
- [ ] Classification.
- [ ] Sequence/recurrent processing.
- [ ] Graph reasoning.
- [ ] Control or decision-making.
- [ ] Optional chess/game workload.
- [ ] Conventional and random baselines.

## M7 — Scalable Generator
- [ ] Define preserved statistics.
- [ ] Implement graph expansion.
- [ ] Motif/module/hub-preserving generation.
- [ ] Test 10K, 100K and 1M units.
- [ ] Investigate larger scales after validation.

## M8 — Human-Brain Reference
- [ ] Survey human connectomics.
- [ ] Identify cross-species candidate principles.
- [ ] Define multiscale constraints.
- [ ] Test human-informed constraints experimentally.

## M9 — Hardware
- [ ] Profile CPU/GPU execution.
- [ ] Identify communication and memory requirements.
- [ ] Evaluate neuromorphic platforms.
- [ ] Compare simulated and hardware behavior.

## M10 — Scientific Release
- [ ] Freeze reproducible experiments.
- [ ] Publish benchmark results.
- [ ] Publish architecture specification.
- [ ] Prepare technical report/preprint.
