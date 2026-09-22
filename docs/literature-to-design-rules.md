# Literature-to-Design Rules

Updated: 2026-09-22

This matrix converts established neuroscience findings into testable engineering
constraints. A biological property is never assumed to be computationally optimal.

| Evidence | Design constraint to test | Metric | Ablation |
|---|---|---|---|
| Sparse biological connectivity and sparse connectome-constrained models | Sparse/event-driven communication | active edges, messages/step, memory traffic | dense/randomized connectivity |
| Recurrent and reciprocal connectome structure | Recurrent state + reciprocal pathways | reciprocal fraction, cycles, activity persistence | remove recurrence |
| Modules + connector hubs | Modular local processing + limited global integration | modularity, participation, path efficiency | flat graph |
| Human brain cost/efficiency trade-offs | Communication benefit under wiring/resource cost | path efficiency, wiring cost, memory/energy proxy | unconstrained efficiency |
| Small-world-like organization | Dense local modules + sparse long-range links | clustering, path length, shortcut fraction | degree-matched random |
| Spatial + topological generative work | Joint spatial/topological constraints | distance law, degree, graphlets | topology-only / spatial-only |
| 2026 human hierarchy studies | Nested hierarchy plus hierarchy-aware long-range edges | hierarchy depth, within-level vs cross-level edges | flat modularity |
| 2026 multiscale eigenmode work | Multiscale topology-to-dynamics operator | eigenmode/activity reconstruction error | single-scale operator |
| 2026 rich-club control study | Explicit integration/control backbone | rich-club density, control proxy, cost per transition | size-matched peripheral core |
| 2026 spatially diffuse control work | Distance-decaying influence/control | control energy vs radius, input count | point-input model |
| 2026 fly whole-brain imaging | Temporal constraints from fast activity | autocorrelation, latency, event statistics | static-only validation |
| 2026 FlyWire-constrained dynamics | Separate anatomical topology from learned dynamics | structural fit vs activity fit | fixed-weight topology |
| 2026 fly energy-information analysis | Explicit energy-information objective | information/task score per resource unit | performance-only objective |
| 2026 neuromorphic co-design | Fast event path + compact slow state | event throughput, memory traffic, latency, energy | dense memory path |
| 2026 fly visual pathway study | Parallel, shallow hierarchy with persistent fine spatial sampling | parallel pathway count, hierarchy depth, spatial-map preservation | forced deep serial hierarchy |
| 2026 fly brain-and-cord connectome | Distributed embodied control with local loops linked by long-range ascending/descending circuits | local-loop autonomy, cross-module control, communication cost | centralized controller |
| 2026 hierarchical reservoir study | Hierarchy can improve memory, multitasking and temporal range; reciprocal/cyclic motifs are implicated | memory capacity, multitask score, timescale diversity | flat modular / random matched controls |
| Cross-species spatial+topological maximum-entropy work | Joint geometry + topology can predict graphlets and weight-related structure beyond fitted constraints | held-out graphlets, edge-length distribution, weight proxy | topology-only / distance-only |


## New M5 implementation

The generator now has three explicit experimental components:

1. hierarchy.py
   - nested community labels;
   - hierarchy-aware edge probabilities;
   - exact target edge count;
   - deliberately transparent baseline, not a fitted biological model.

2. spatial.py
   - Euclidean wiring-cost proxy;
   - exponential distance-decay probability;
   - explicit long-range shortcut budget.

3. rich_club.py
   - explicit degree-threshold rich-club profile;
   - rich-core density;
   - optional normalization against an externally generated null;
   - rich-to-periphery edge fraction.

These components are intentionally separable so later ablations can distinguish
hierarchy, spatial embedding and hub structure.

| Quantum entanglement monogamy/shareability | Bounded relational strength/channel capacity | strength concentration, cross-module bandwidth, stability | equal-edge-count unrestricted-strength control |
| Quantum entanglement routing under fidelity/coherence/memory constraints | Stateful routing through finite interfaces | routing success, latency, communication cost, congestion | static shortest-path routing |
| Tensor-network multiscale representation | Compact effective state at module boundaries | information retention per communicated bit, task score, latency | raw-state communication |
| Holographic/QEC tensor-network models | Constrained boundary representation + structured redundancy | fault recovery, interface bandwidth, failure containment | full-state access / uniform replication |
| Emergent geometry from relational structure | Derive effective distance from interaction/communication structure | predictive power of effective distance for dynamics | Euclidean distance / graph distance |

| 2025 neural-module resource study | Structural modularity alone does not guarantee functional specialization; sparse communication can be sufficient for specific cross-module information | specialization, inter-module messages, task performance | dense communication and randomized sparse controls |
| 2025-2026 information-bottleneck communication | Transmit compact task-relevant representations under rate/latency constraints | task utility per communicated bit, compression ratio, robustness | raw-state/full-feature communication |
| Quantum/tensor-network synthesis | Treat module boundaries as finite information interfaces and test multiscale effective states | interface rate, retained task information, fault isolation | unrestricted cross-level state access |

## Rules for interpretation

1. Structural match is not functional match.
2. Functional match is not engineering advantage.
3. Engineering advantage must survive strong non-biological controls.
4. Spatial and topological constraints must be tested separately.
5. Human findings are reference constraints, not instructions to imitate every biological detail.
6. Biological neuron/synapse types must remain explicit where a tested mechanism depends on them.
7. Every claimed advantage must report resource cost as well as task performance.
8. A rich-club threshold is a measurement convention unless independently justified.
9. Long-range edges must be evaluated by function and cost, not treated as automatically beneficial.
10. Effective/dynamic hierarchy must not be conflated with static community hierarchy.

## Priority order

1. density + full degree distributions;
2. hubs + reciprocity;
3. hierarchy + modularity + short/long-range structure;
4. spatial distance/contact constraints;
5. rich-club/backbone and cost-efficiency;
6. motif/graphlet constraints;
7. typed inhibitory/excitatory dynamics;
8. multiscale dynamics and activity-derived constraints;
9. hardware/resource mapping.

This order moves from directly measurable structure toward increasingly mechanistic constraints.


| 2026 neuromorphic hierarchical-reservoir study | Prefer shallow/nested hierarchy search with explicit depth-saturation measurement | memory, multitasking, timescale diversity vs hierarchy depth | flat modular, random, and deeper hierarchy |
| 2026 community-aware sparse SNN topology | Jointly optimize sparse communication and module structure | active edges, events/step, communication-cost proxy | matched-degree sparse random topology |
| 2026 cortical microcircuit generative modeling | Explore compact latent representations only after structural validation | latent size vs held-out graphlets/degree/spatial statistics | direct high-dimensional parameterization |
| Cross-domain resource principle | Report task performance together with event, edge, wiring and memory proxies | task score per resource proxy | performance-only objective |


| 2025 Nature Communications modular-resource study | A narrow bottleneck can increase module specialization, but structural modularity alone does not guarantee it | specialization, interface dimension, inter-module communication | shared-readout, dense-interface, randomized sparse-interface controls |
| 2026 Conditional Rate–Utility communication-edge inference | Adaptive bottlenecks can trade task utility against communication rate under changing conditions | task utility/bit, interface rate, adaptation cost | fixed-bandwidth and unrestricted-rate controls |
| 2026 tensor-network bottleneck compression | Effective low-rank/MPO representations can compress large linear transformations without immediate task loss in studied image-classification settings | interface dimension, retained task information, compute/communication cost | dense linear layer and fixed pooling controls |
| 2026 hyperbolic temporal graph networks | Hyperbolic representations are established graph-learning machinery for hierarchical/dynamic graphs, not evidence for biological geometry | optional effective-geometry benchmark | Euclidean graph embedding and graph-distance controls |
| 2026 selective redundancy for fault tolerance | Targeted redundancy can trade reliability against hardware resource use in studied accelerators | recovery probability, redundancy cost, latency | no redundancy and uniform redundancy |
