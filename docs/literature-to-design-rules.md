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

| 2026 higher-order brain interaction study | Do not assume pairwise edges are sufficient; allow bounded collective module relations | synergy/redundancy, task utility per relation, communication cost | pairwise-only and unrestricted higher-order controls |
| 2025 resource-constrained specialization study | Interface bandwidth can dynamically alter functional specialization | specialization trajectory vs interface rate | fixed high-bandwidth and fixed low-bandwidth controls |
| 2026 naturalistic connectome backbone study | Separate conserved backbone from context-flexible hub recruitment | backbone stability, hub flexibility, state-dependent routing | static hub set and degree-matched controls |


## Dynamic relational layers across the life course

Human social networks provide a useful non-biological analogy for **state-dependent hierarchical interfaces**, not a specification for the architecture. Evidence shows that personal networks have layered structure associated with relationship closeness, while network composition and communication patterns change with age and life events. Population-scale work also finds overlapping relationship layers such as close family, extended family, household, work, school, and neighbors. citeturn0search2turn0search3turn0search0

A useful engineering abstraction is therefore:

> **The system should not require one permanent hierarchy of all relationships. It should maintain nested local groups with different interaction strengths and purposes, while allowing interfaces, memberships, and routing priorities to change with state, role, time, and context.**

Design rules:
- **DL1 — Nested relational layers:** represent local/core, group, community, and broader coordination layers without requiring every lower-level member to communicate directly with every upper-level entity.
- **DL2 — Typed relations:** distinguish relation purpose (e.g. local state exchange, coordination, support/control, external interface) instead of treating every edge as equivalent.
- **DL3 — Dynamic layer membership:** allow a node/module to participate in multiple overlapping groups when tasks or context require it.
- **DL4 — State-dependent routing:** prioritize different interfaces as the system state changes; avoid a permanently fixed communication hierarchy.
- **DL5 — Representative interfaces:** higher levels should receive compact effective states from lower levels rather than all microscopic states.
- **DL6 — Direct exception path:** an upper-level controller should be able to address a lower-level node/module directly when the task requires it, without making all communication permanently dense.
- **DL7 — Life-course analogue → adaptive topology:** use changing human relationships only as inspiration for adaptive topology; do not encode human age, family roles, or social norms as architectural requirements.
- **DL8 — Test hierarchy depth:** compare flat, two-level, deeper, and overlapping-layer architectures under equal communication/compute budgets; deeper hierarchy is not assumed to be beneficial.

This idea extends MCIA/ERG into a **Dynamic Relational Layering (DRL)** hypothesis:

> **Scalable systems may organize communication as overlapping, state-dependent relational layers whose interfaces are compact and whose direct links are selectively activated according to current context.**

Falsifiable predictions:
1. Adaptive relational layers can achieve comparable global coordination with fewer transmitted values than dense all-to-all communication on tasks with changing context.
2. Overlapping groups can outperform strictly tree-shaped hierarchies on tasks requiring cross-domain interactions, at equal communication budget.
3. A direct exception path can preserve pair-specific performance without requiring the full network to expose pairwise state.
4. Excessive layer depth will eventually saturate or reduce performance because additional interfaces add routing and communication overhead.
5. If adaptive routing is merely exploiting more parameters or more communication, matched-budget fixed-routing and random-routing controls should remove the apparent advantage.

Controls:
- flat all-to-all;
- fixed tree hierarchy;
- fixed overlapping groups;
- adaptive overlapping groups;
- random state-dependent routing with the same active-edge budget;
- matched-bandwidth fixed routing;
- matched-parameter pooling/compression.

The human evidence supports the **existence of layered, changing, overlapping relationships**, not the claim that such a structure is optimal for computation. citeturn0search0turn0search3turn0search4


### Additional human-network principles worth testing

Recent social-network literature suggests several abstractions beyond simple nested circles:

1. **Finite relational budget:** relationship layers reflect limited time/attention/resource allocation; continuous relationship-strength models fit phone, face-to-face and online data rather than requiring hard circle boundaries. See Tamarit et al. (2022): https://www.nature.com/articles/s41598-022-06066-1
2. **Churn with structural continuity:** individual ties can be replaced while the overall layered organization remains comparatively stable; life transitions can increase turnover. See Weiss et al. (2022): https://pmc.ncbi.nlm.nih.gov/articles/PMC9519061/ and Escribano et al. (2023): https://www.nature.com/articles/s41598-023-41787-x
3. **Multiplexity:** the same nodes can participate in distinct relation layers (social, health, economic, professional, etc.), and the layers can interact rather than simply being aggregated. A 2026 Nature Communications study modeled 176 multiplex networks and found layer-specific roles/trade-offs and interdependence. See https://www.nature.com/articles/s41467-026-68896-1
4. **Overlapping membership:** nodes can belong to multiple communities; overlapping nodes can have important routing/efficiency properties. Overlapping communities are also observed in human brain structural networks, making this relevant beyond social systems. See https://pmc.ncbi.nlm.nih.gov/articles/PMC3089616/
5. **Brokerage:** nodes or modules that bridge otherwise separated groups can change the permeability of group boundaries. This suggests testing sparse bridge resources separately from ordinary within-group connectivity. See Stovel & Shaw (2012): https://www.annualreviews.org/content/journals/10.1146/annurev-soc-081309-150054
6. **Context-sensitive continuity:** 2026 life-course work distinguishes stable core relationships from changing everyday interaction, warning against using current contact frequency as the sole proxy for long-term relational importance. See https://pmc.ncbi.nlm.nih.gov/articles/PMC12462710/

Engineering abstractions:
- **RL1 — relational budget:** every node/module has bounded communication/maintenance capacity; stronger or more important relations consume more budget.
- **RL2 — soft layers:** relationship strength should be continuous where possible; hard layer boundaries are an experimental simplification.
- **RL3 — churn without collapse:** allow individual routes to change while preserving higher-level organization.
- **RL4 — multiplex channels:** the same pair may have multiple typed relations with different routing priorities and costs.
- **RL5 — overlap:** allow modules to participate in multiple contexts instead of forcing a single tree membership.
- **RL6 — brokerage budget:** explicitly reserve a small number of bridge routes between otherwise separated modules.
- **RL7 — stable core + flexible periphery:** distinguish persistent high-value interfaces from rapidly changing low-priority routes.
- **RL8 — context-specific interaction:** a relation important for one task need not be important for another task.

These are hypotheses/engineering abstractions, not claims that human social organization is computationally optimal.


## 2026-09-24 refresh: spatial-control rule

**New design rule:** Before interpreting any residual rich-club or architectural signal after CFG and NPC-like controls, test whether the signal survives an explicit geometric null.

Rationale:
1. Péntek & Ercsey-Ravasz (2025) show that EDR can explain many Drosophila neuropil-projectome properties and use it as a null for separating geometric inevitabilities from potentially functional structure.
2. Cross-species connectome work (2025) indicates that degree/topology and spatial constraints capture different aspects of neural organization and that combined constraints can be necessary.
3. Therefore Gate C should not be a single arbitrary distance-preserving shuffle. It should compare at least:
   - C1: spatial/EDR-constrained null
   - C2: topology + spatial combined null where feasible
   - observed vs CFG vs NPC-like vs spatial/combined controls on the same metric grid.

**Status:** design requirement only; implementation pending completion and audit of Gate B.

## 2026-09-27 literature refresh — Gate B/C and computational relevance

### L1 — Spatial constraints are not a cosmetic control
**Source:** Salova & Kovács, *Network Neuroscience* 9(1), 181–206 (2025), DOI 10.1162/netn_a_00428.

The study compares fly, mouse and human connectomes and reports that spatial
constraints alone do not recover broad topological structure, while degree
sequence alone does not recover spatial structure. Combined maximum-entropy
models using topology and physical constraints reproduce additional properties
such as graphlets and weight-related structure.

**Project consequence:** Gate C must not be implemented as a single generic
"distance randomization" and then treated as a complete explanation. We should
separate:
1. topology-only CFG;
2. spatial/distance-only control where meaningful;
3. topology + spatial combined control;
4. observed network;
and compare the same rich-club metric grid across them.

**Evidence class:** NULL-CONTROLLED / CROSS-SPECIES.

### L2 — EDR is a literature-backed candidate for the Drosophila spatial null
**Source:** Péntek & Ercsey-Ravasz, *Network Neuroscience* 9(3), 869–895 (2025), DOI 10.1162/netn_a_00455.

The study revisits the exponential distance rule and reports that an EDR-based
model explains numerous binary and weighted properties of the Drosophila
neuropil projectome. It explicitly presents EDR as a useful null model for
separating geometric consequences from properties of functional interest.

**Project consequence:** EDR should be evaluated as one candidate Gate C null,
but its level is important: the published analysis is primarily a neuropil /
projectome model, whereas our current rich-club question is neuron-level.
Therefore we must not silently substitute projectome EDR for a neuron-level
spatial null. We need explicit distance semantics first.

**Evidence class:** OBSERVED / NULL-CONTROLLED in the cited study.

### L3 — Structure-to-function needs an explicit dynamical bridge
**Source:** Wang et al., bioRxiv 2026, *Connectome-constrained modeling identifies
neurons and synapses that sustain spontaneous activity in Drosophila*.

The work fits a whole-brain dynamical model to spontaneous calcium activity while
constraining it with the FlyWire connectome, then uses perturbations to identify
candidate hubs and synapses sustaining resting dynamics. The important
methodological point for this project is that wiring is a constraint on the
model, while activity is an independently validated target.

**Project consequence:** even if a structural feature survives Gate A–C, it must
not be described as functionally important until an explicit activity/task model
or benchmark establishes the bridge.

**Evidence class:** PROMISING / MODEL-CONSTRAINED PREPRINT.

### L4 — Network structure can affect modeled fly activity, but this is not yet
an architecture specification
**Source:** Zhang et al., *Fundamental Research* 6(3), 1859–1868 (2026),
DOI 10.1016/j.fmre.2025.01.017.

The study reports that simplified neuronal activation models built on real
Drosophila network structure reproduce activation patterns across several
neuronal dynamics models, and reports a distinction between network distance
and physical distance in the studied activation patterns.

**Project consequence:** network distance is a useful candidate metric for a
future structure-to-dynamics branch, but it should remain separate from Gate C's
physical-distance null. Physical distance and graph distance answer different
questions.

**Evidence class:** ESTABLISHED FOR THE STUDIED MODEL / HYPOTHESIS FOR OUR USE.

### L5 — Whole-connectome computation is already prior art
**Sources:** Wang et al., *Neuromorphic Simulation of Drosophila melanogaster
Brain Connectome on Loihi 2* (2025); Yu et al., *Biological Processing Units*
(2025); Drosophila connectome reservoir-computing work (2025).

These studies demonstrate that full or partial fly connectomes can already be
mapped to neuromorphic hardware, fixed recurrent processing units, or reservoir
computing systems, with task-level benchmarks.

**Project consequence:** "connectome-derived computation" is not itself a
novelty claim. Any eventual project novelty must be narrower and evidence-based,
for example a validated structural constraint, abstraction, generator,
runtime, scaling law, or resource/performance advantage not already demonstrated
by close prior art.

**Evidence class:** ESTABLISHED PRIOR ART.

### L6 — A recent fly study directly reinforces the separation between topology
and dynamics
**Source:** Lin & Murthy, *Nature Methods* (2025), "Linking structure and
function: biological insights from fly connectomes."

The review emphasizes that connectomes provide a structural foundation for
linking wiring to neural activity and behavior, while connectome-based models
remain a route to testing structure-function relationships.

**Project consequence:** keep the evidence ladder explicit: structural
observation -> null-controlled residual -> dynamical validation -> computational
benchmark. Do not collapse these into one claim.

**Evidence class:** REVIEW / CONTEXT.

### Literature decision for the current project
The new literature does **not** change the immediate order:

**Finish NPC 100-null -> decide Gate B -> design Gate C -> only then derive a
computational primitive.**

It does sharpen Gate C substantially: the spatial branch should include a
literature-backed EDR candidate where the data semantics permit it, plus a
combined topology+spatial condition. It also strengthens the prohibition on
calling a surviving structural feature "functional" without an explicit
validated dynamics/task bridge.
