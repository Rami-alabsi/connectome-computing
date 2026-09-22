# Cross-study synthesis: sparse control backbone hypothesis

Updated: 2026-09-22

## Why these papers are interesting together

Several recent results point to different layers of the same systems problem:

1. A 2026 FlyWire-constrained Drosophila model found that resting dynamics can depend on a **compact neuropil core** containing a sparse, brain-spanning population of inhibitory hub neurons with reciprocal excitatory partners. The study is a preprint, so this is treated as promising rather than established. 
2. A 2026 human network-control study found that excluding rich-club regions increased the control energy required for transitions and reduced state stability in the tested datasets.
3. A 2026 cross-species mammalian study found that models combining modular cooperation with diffuse, long-range competition reproduced empirical dynamics better than cooperation-only models and produced more hierarchical/synergistic dynamics.
4. Work on combined spatial + topological maximum-entropy models shows that geometry and topology together can predict additional biological properties, rather than either constraint being sufficient alone.

These are not the same experiment and should **not** be treated as proof of one universal architecture.

## Project synthesis hypothesis

We will test the following engineering hypothesis:

> A scalable connectome-inspired architecture may benefit from a **small, sparse control/integration backbone** embedded in hierarchical local modules, with reciprocal typed interactions near the backbone and a limited long-range competitive/inhibitory channel. Spatial cost constrains which backbone links are affordable.

This is a **hypothesis, not a novelty claim**.

The interesting possibility is that the backbone is not simply a collection of high-degree nodes. It may be a resource-limited control layer whose value comes from the interaction of:

- high structural centrality / rich-club position,
- reciprocal typed interactions,
- hierarchy-crossing links,
- spatially expensive but sparse long-range communication,
- state-dependent effective routing.

## Falsifiable predictions

A synthetic architecture implementing this hypothesis should be compared against controls matched for node count, edge count, degree distribution and, where possible, wiring cost.

### P1 — Backbone sparsity
A small backbone should reproduce or improve global state transitions without requiring dense all-to-all communication.

### P2 — Typed reciprocity
Reciprocal E/I-like interactions around selected hubs should stabilize useful recurrent dynamics better than sign-randomized or untyped reciprocity.

### P3 — Long-range competition
Adding a sparse long-range competitive channel should change global coordination differently from simply adding cooperative long-range edges.

### P4 — Spatial budget
If long-range links are made arbitrarily cheap, the biological constraint loses meaning. Performance therefore must be reported jointly with wiring/communication cost.

### P5 — State dependence
The structurally defined backbone should not be assumed to be the same as the dynamically active backbone in every state.

## Required controls

1. Random graph with matched density.
2. Degree-preserving rewired graph.
3. Hierarchical modular graph without a backbone.
4. Backbone graph without typed signs.
5. Backbone with sign-shuffled long-range edges.
6. Cooperation-only long-range graph.
7. Competition-only long-range graph.
8. Cost-matched graph with the same total wiring budget.
9. Flat hierarchy versus hierarchical hierarchy.
10. Static routing versus state-dependent routing.

## Metrics

### Structure
- degree distribution and tail statistics
- reciprocity
- participation coefficient
- hierarchy-crossing fraction
- rich-club curve
- long-range fraction
- mean and tail wiring length
- module density / between-module density

### Dynamics
- state-transition controllability proxy
- stability / recovery after perturbation
- memory capacity
- avalanche or burst statistics where applicable
- multiscale spectral/eigenmode reconstruction

### Engineering
- events per inference
- bytes moved
- fan-in/fan-out pressure
- peak active state
- latency
- energy proxy

## Novelty gate

The combined hypothesis is **not declared novel** merely because the individual ingredients appear in different papers.

A novelty alert requires:

1. exact combined architecture defined in code;
2. targeted search for the exact combination and close variants;
3. reproducible experiments;
4. ablations showing which interaction is necessary;
5. strong non-biological baselines;
6. evidence that the effect is not caused by parameter count, density, degree sequence or cost differences.

Only after these conditions are met will the project label the result as a possible new computational principle.
