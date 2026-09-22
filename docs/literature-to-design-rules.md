# Literature-to-Design Rules

Updated: 2026-09-22

This document turns established neuroscience/connectomics findings into testable
engineering constraints. It does **not** assume that a biological property is
automatically computationally optimal.

| Evidence | Design constraint to test | Metric | Ablation |
|---|---|---|---|
| Sparse biological connectivity is repeatedly observed, and sparse connectome-constrained models can predict neural activity. | Sparse/event-driven communication | active edges, messages/step, memory traffic | dense/randomized connectivity |
| Fly whole-brain models and connectome statistics show recurrent and reciprocal structure. | Recurrent state + reciprocal pathways | reciprocal-edge fraction, cycle statistics, activity persistence | remove recurrence/reciprocity |
| Brain networks contain modules and connector hubs. | Modular local processing + limited global integration | modularity, hub participation, path efficiency | flat random graph |
| Brain organization reflects a cost/efficiency trade-off. | Optimize communication benefit under wiring/resource cost | path efficiency, edge count, communication cost, memory/energy proxy | unconstrained efficiency |
| Human and animal connectomes show non-random small-world-like organization. | Short-range dense modules plus sparse long-range shortcuts | clustering, path length, small-world controls | degree-matched random graph |
| Recent scalable generative work shows that topology plus spatial constraints can reproduce additional neural-network properties. | Include spatial/contact constraints, not topology alone | distance-dependent connection probability, wiring length, graphlets | topology-only generator |
| Recent FlyWire dynamical modeling identifies a compact neuropil core and sparse inhibitory/excitatory reciprocal hub structure associated with spontaneous activity. | Test typed hub/core structure, not just untyped degree hubs | core participation, typed reciprocity, activity stability | degree-matched untyped hubs |
| Fly visual-system work shows connectivity can constrain task-optimized mechanistic models when neuron/synapse parameters are learned. | Separate topology from learnable dynamics and task optimization | task accuracy, fitted dynamics, parameter count | unconstrained topology |
| Neuromorphic FlyWire mapping demonstrates sparse, irregular, recurrent connectivity creates hardware constraints and can benefit from event-driven hardware. | Treat communication pattern and fan-in/fan-out as first-class architecture constraints | memory footprint, event throughput, latency, utilization | dense ANN baseline |

## Rules for interpretation

1. A structural match is not a functional match.
2. A functional match is not an engineering advantage.
3. An engineering advantage must survive strong non-biological controls.
4. Spatial constraints must be tested separately from topological constraints.
5. Biological neuron/synapse types must not be collapsed into one generic node if
   doing so destroys a tested mechanism.
6. Every claimed advantage must report resource cost as well as task performance.

## Priority order

The next generator versions should therefore progress in this order:

1. density + degree distribution;
2. hubs + reciprocity;
3. modularity + short/long-range structure;
4. spatial distance/contact constraints;
5. motif/graphlet constraints;
6. typed inhibitory/excitatory dynamics;
7. activity-derived constraints;
8. hardware mapping and resource measurements.

This ordering is deliberately conservative: it moves from directly measurable
structure toward increasingly mechanistic constraints.
