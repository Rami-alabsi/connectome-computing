# System Synthesis

## Current architecture

The current experimental architecture is:

**local node dynamics → module effective state → bounded interface → state-dependent routing → active cross-module communication → optional higher-order coordination**

The architecture is intentionally classical and resource-accounted. It is a testbed for falsifiable comparisons, not a claim that biological, quantum, holographic, or particle-physics mechanisms are literally implemented.

## Why these layers are separated

A central risk in connectome-inspired architecture research is changing several variables at once. The simulator therefore keeps:

- **topology**: which candidate module relations exist;
- **effective-state mapping**: how local detailed states are compressed;
- **routing**: which candidate relations are active at a given state;
- **bandwidth**: how many relations and values may cross interfaces;
- **dynamics**: how local states respond to local recurrence and received messages;
- **higher-order coordination**: whether bounded multi-module relations are allowed.

This separation permits matched-resource controls and ablations.

## Scientific motivation

Recent work strengthens several independent ingredients without establishing the combined architecture as novel.

1. Resource-constrained neural modules show that inter-module communication bandwidth can influence functional specialization, and that high-bandwidth coupling can reduce specialization. This motivates treating interface capacity as a first-class experimental variable rather than merely counting parameters. See the 2025 *Nature Communications* study on neural-module specialization under resource constraints.
2. Recent higher-order connectomics reports redundancy and synergy that are not fully captured by pairwise connectivity. This motivates an optional bounded higher-order branch, while requiring pairwise controls.
3. Recent naturalistic connectome work reports a conserved degree-based backbone with context-dependent hub recruitment. This motivates stable infrastructure plus flexible routing rather than either a completely fixed or completely unconstrained topology.
4. Dynamic-routing work in machine learning shows that state-dependent expert selection is an established engineering idea and also exposes load-imbalance/data-movement costs. Therefore dynamic routing itself is not a novelty claim.
5. Tensor-network work demonstrates that large transformations can be represented through compact structured forms. In this project, this is only an engineering abstraction for multiscale effective states, not evidence that connectomes implement tensor networks.

## Falsifiable mechanism family

The narrow mechanism being tested is:

> Keep detailed computation local, expose only a bounded effective state across module boundaries, and activate only a resource-limited subset of candidate relations according to current module state.

Primary comparisons:

1. full cross-module communication;
2. fixed sparse communication;
3. state-dependent sparse routing;
4. bounded effective-state + fixed routing;
5. bounded effective-state + state-dependent routing.

All variants should be matched where practical for node count, candidate topology, active relation budget, transmitted values, parameters, and compute.

## Higher-order branch

Higher-order coordination is not assumed to improve performance. It should be introduced only as an additional controlled resource:

- pairwise-only;
- bounded third-order relations;
- state-dependent third-order activation;
- matched relation/communication budget.

The key question is whether collective relations provide measurable utility after accounting for their resource cost and after pairwise controls.

## Capacity hypothesis

The capacity branch tests:

**bounded local capacity → saturation → structured expansion**

Possible responses to saturation are:

- add a peer module;
- create a higher-order module;
- recruit a sparse long-range route;
- increase local density.

The project does not assume which response is optimal. It will be selected by experiments.

## Novelty gate

No novelty claim is warranted from the combination alone. Dynamic routing, modular specialization, compressed representations, tensor-network representations, higher-order interactions, and sparse coordination all have substantial prior art.

A novelty claim requires:

1. exact prior-art search for the narrow mechanism;
2. reproducible implementation;
3. strong matched-resource baselines;
4. ablations isolating each mechanism;
5. independent replication or held-out evaluation;
6. a measurable advantage that survives those controls.

## Next empirical gate

The next major scientific gate is real-data anchoring with FAFB v783. Synthetic experiments should not be interpreted as biological validation until the structural and spatial constraints are measured from the selected connectome snapshot.


## Cosmic-scale extension

The project now includes a separate cosmic-scale abstraction branch: **Field-Mediated Relational Layer (FMRL)**. The cosmic web is treated as an independent physical example of multiscale spatial organization produced by gravitational dynamics, not as evidence that gravity is equivalent to computation. The proposed computational test is to compare explicit pairwise communication with a bounded latent relational field and a hybrid field + sparse explicit backbone under matched communication budgets. See `docs/cross-domain-synthesis-cosmic-web.md`.


## Dynamic Relational Layering (DRL)

A new cross-domain engineering hypothesis is motivated by human social-network structure across the life course. Human relationships are not a single flat graph: they form nested layers of closeness and purpose, overlap across family/work/community domains, and change with life events and context. citeturn0search2turn0search3turn0search0

For Connectome Computing, the abstraction is **not** "copy human society." Instead:

**microscopic state → local group → overlapping relational layers → compact effective interfaces → selective direct routing**

The proposed DRL principle is:

> **Scale by changing which relational layer carries information, rather than requiring every entity to maintain every relationship at every scale.**

This gives a concrete extension to MCIA and ERG:
- local modules retain detailed state;
- modules may belong to multiple overlapping groups;
- each group exposes a compact effective state;
- state-dependent routing selects which layer/interface is active;
- sparse direct links handle exceptions requiring precise pair identity;
- the active hierarchy can change with task/context.

The key engineering question is whether this adaptive layering provides a measurable communication/robustness benefit under matched resource budgets. It remains a hypothesis until controlled experiments are completed.
