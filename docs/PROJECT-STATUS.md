# Project Status

## Current position

**Stage: M5 → M6 transition — Real-data validation + resource-constrained multiscale simulator**

The project is now organized around a single experimental chain:

**biological evidence → structural abstraction → bounded resources → effective state → coordination → dynamics → benchmark → ablation → scaling**

The goal is not to reproduce a fly or human brain literally. The goal is to identify computational principles that remain useful after biological details are abstracted away and strong non-biological controls are applied.

### Completed

- [x] M0 Research foundation
- [x] M1 FlyWire/Codex ingestion layer
- [x] M2 Structural graph analysis
- [x] M2b Motif/null-model foundation
- [x] M3 Biological annotation layer
- [x] M4 Architecture primitives
- [x] M5 modular directed synthetic generator
- [x] M5 structural profile and first-order calibration
- [x] M5 sparse, hierarchical, spatial and rich-club baselines
- [x] M5 multi-constraint validation framework
- [x] M5 capacity-triggered hierarchy prototype
- [x] M5 quantum-information/tensor-network synthesis as a classical hypothesis branch
- [x] M6 effective-state interface skeleton
- [x] M6 communication accounting
- [x] M6 bounded higher-order coordination primitive
- [x] M6 higher-order and dynamic-backbone literature synthesis

### Active workstreams

#### 1. Real biological anchor
Run FAFB v783 through the streaming profile pipeline and measure:
- directed degree distributions
- reciprocity
- hubs/rich-club
- motifs
- hierarchy/modularity
- spatial/contact constraints where data permit
- long-range structure
- multi-constraint interactions

This remains the main empirical anchor before claiming that synthetic rules reproduce biological organization.

#### 2. Multiscale effective-state simulator
Build a minimal stateful simulator in which:
- detailed node states remain local;
- modules expose bounded effective states;
- cross-module bandwidth is explicit;
- interface dimension is explicit;
- communication cost is measured;
- routing can become state-dependent;
- higher-order module relations can be activated under a budget.

The simulator must keep topology, interface compression and dynamics as separable factors.

#### 3. Sparse control architecture
Test the emerging architecture:

**local parallel modules → bounded interfaces → sparse conserved backbone → flexible hubs/routing → optional higher-order coordination → state-dependent integration**

This is a hypothesis, not a biological conclusion.

#### 4. Capacity and hierarchy
Treat capacity as multiple independent resources:
- node occupancy
- internal edge density
- interface bandwidth
- interface state dimension
- active relational strength
- dynamic/event rate

Test whether saturation should trigger new modules, higher-order aggregation, or alternative routing rather than indiscriminate densification.

#### 5. Higher-order coordination
Compare pairwise-only interfaces with bounded third-order module relations. Measure:
- task utility
- communication volume
- latency
- redundancy/synergy proxies
- robustness under module ablation

Keep fourth-order and higher relations optional until lower-order evidence justifies them.

#### 6. Dynamic backbone
Test a dual architecture:
- stable infrastructure/backbone
- context-dependent hub recruitment

Compare against fixed hubs, fully dynamic routing and degree-matched controls.

#### 7. Strong-control benchmark suite
Every proposed mechanism should be compared under matched:
- node count
- edge count
- degree distribution
- modularity
- parameter count
- communication budget
- compute budget
- latency where applicable

Primary controls include random, degree-preserving, hierarchy-preserving, cost-matched and sign/routing-shuffled variants.

### Scientific checkpoint

The 2026 literature strengthens several links in the project but also narrows the claims we can make.

Hierarchical modular reservoirs improve memory, multitasking and temporal diversity, while performance rapidly saturates with additional hierarchy; this supports testing shallow/optimal hierarchy rather than assuming unlimited depth. citeturn0search0

Recent higher-order brain analyses show that third-order interactions reveal redundancy and synergy that pairwise connectivity does not capture fully, while remaining task- and hierarchy-dependent. This supports a controlled higher-order coordination branch, not a claim that hypergraphs are inherently superior. citeturn0search2

Naturalistic connectome work reports a conserved degree-based backbone together with context-dependent hub recruitment, motivating the project's stable-infrastructure/flexible-routing hypothesis. This is an empirical reference constraint, not yet an engineering result. citeturn0search1turn0search4

### Core synthesis

The strongest common thread currently running through the project is:

> **A scalable system may grow by adding higher-order effective units while keeping detailed computation local, restricting cross-scale interfaces, and allocating scarce global coordination resources only where they provide measurable value.**

This unifies the previously separate threads:

- **Fly connectome:** modular, sparse, recurrent, distributed organization.
- **Human connectome:** hierarchy, rich-club/control structure, spatial cost and state-dependent organization.
- **Capacity hypothesis:** bounded local resources can force structured expansion.
- **Effective-state hypothesis:** higher levels need not expose every microscopic variable.
- **Quantum/tensor-network inspiration:** use multiscale compression and constrained relational resources as mathematical/engineering abstractions, not physical claims.
- **Higher-order interactions:** allow collective module relations when pairwise interfaces are insufficient.
- **Dynamic backbone:** preserve stable infrastructure while allowing context-dependent recruitment.
- **Neuromorphic constraints:** communication, memory, sparsity and event-driven cost become first-class resources.

### Important scientific boundaries

The project does **not** claim:
- neurons are quantum objects or strings;
- connectome edges are entanglement;
- holography is a brain mechanism;
- quarks have demonstrated substructure;
- biological evolution implies a single optimal architecture;
- any proposed combination is novel before targeted prior-art search and controlled experiments.

### Immediate sequence

1. Repair and keep CI green after every change.
2. Complete real FAFB v783 profiling.
3. Finish the minimal stateful effective-state simulator.
4. Add explicit interface bandwidth and state-dimension sweeps.
5. Add state-dependent routing and sparse-backbone controls.
6. Add bounded higher-order coordination.
7. Run matched-resource experiments.
8. Compare all mechanisms independently and jointly.
9. Perform exact prior-art search on any surviving combined mechanism.
10. Scale only after the small controlled system is reproducible.

## Scientific status

No biological or computational benchmark result is claimed until the corresponding data and experiment have actually been executed.

## Novelty status

**No novelty claim yet.**

Any future novelty statement must identify a narrow mechanism, document exact prior art searched, provide reproducible implementation, and show an advantage that survives matched-resource controls and ablations.
