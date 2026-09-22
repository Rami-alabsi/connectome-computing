# Architecture Plan

## High-Level Pipeline

Biological Connectome → Ingestion → Graph → Motifs/Modules/Hubs → Biological Rules → Computational Primitives → Connectome Architecture → Generator + Simulator + Benchmarks → Scaling Analysis → Human-Brain Constraints

## Layer 0 — Data
Neuron identifiers, synaptic edges, weights/counts, cell types, neurotransmitter predictions and anatomical regions where available. Every dataset must record version and provenance.

## Layer 1 — Graph
Represent the connectome as a directed weighted graph G=(V,E,W), with biological metadata retained as node and edge attributes.

## Layer 2 — Structural Analysis
Compute degree statistics, reciprocity, components, motifs, modularity, rich-club structure, path lengths and cross-region connectivity, with null-model comparisons.

## Layer 3 — Dynamics
Start deliberately simple: leaky integrate-and-fire, event-based transmission or discrete-time recurrent updates. The selected model must be documented and validated for the experiment.

## Layer 4 — Processing Unit
A unit exposes local state, input events, sparse outgoing connections, weighted communication, a local update rule and instrumentation.

## Layer 5 — Modules
Group units using anatomical, graph-community, cell-type or generated structural rules. Modules communicate through sparse inter-module edges.

## Layer 6 — Architecture
Support sparse communication, local state, recurrent processing, parallel module execution and explicit routing/integration resources. Initial implementation is hardware-neutral.

## Scaling Generator
Implement controlled modes:
1. Random baseline.
2. Degree-preserving model.
3. Motif-preserving model.
4. Module-preserving model.
5. Connectome-derived model preserving selected rules.

This lets experiments ask which biological property is actually responsible for an observed effect.

## Benchmark Records
Record dataset version, configuration, seed, unit count, connection count, activity, state/parameter count, communication events, memory, runtime and task performance.

## Human-Brain Reference
Do not directly resize the fly graph. Use human connectomics to propose candidate constraints such as hierarchy, multiscale organization, integration/segregation, long-range communication, recurrence and sparse organization.

## Hardware Mapping
Only after software profiling should CPU/GPU/distributed/neuromorphic mapping be investigated.
