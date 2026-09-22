# Human Brain Reference Constraints

Updated: 2026-09-22

## Purpose

The human nervous system is treated as a high-scale biological reference and source of
constraints, not as a simple target obtained by scaling the fly connectome.

The project should ask:

> Which organizational mechanisms survive across biological scales, and which are
> specific to a species, anatomical scale, or measurement modality?

## Mechanisms to track

### 1. Economic organization

Human brain networks balance communication efficiency against physical, metabolic,
and wiring costs. High-efficiency structures can be expensive rather than free.

**Engineering hypothesis:** optimize useful communication per unit of resource cost,
rather than maximizing connectivity or shortest paths alone.

Metrics:
- edge count
- total wiring/distance proxy
- communication cost
- path efficiency
- memory traffic
- event/message count
- energy proxy

### 2. Modules + connector hubs

Human brain networks show modular organization with distributed high-degree connector
hubs. Rich-club connections can act as costly long-range bridges between modules.

**Engineering hypothesis:** most computation should remain local, while a limited
integration layer provides controlled global communication.

Metrics:
- modularity
- intra/inter-module traffic
- hub participation
- rich-club coefficient
- long-range edge fraction
- path efficiency

### 3. Hierarchical organization

Brain organization is studied across multiple scales, from neurons and local
circuits to regions and whole-brain networks.

**Engineering hypothesis:** use nested modules rather than one flat graph.

Metrics:
- hierarchy depth
- community structure at multiple resolutions
- cross-level communication
- local/global traffic ratio

### 4. Spatial embedding

The brain operates inside a physical body with finite space, material and metabolic
resources. Distance therefore matters.

**Engineering hypothesis:** communication probability should depend partly on physical
distance, while selected long-range links are retained when their integration value
justifies their cost.

Metrics:
- distance distribution
- wiring length
- long-range shortcut fraction
- distance-dependent connection probability

### 5. Rich-club cost/benefit

Human rich-club organization is associated with high wiring and metabolic costs, but
also with global integration and communication capacity.

**Engineering hypothesis:** a small expensive backbone may be more useful than making
the entire network globally dense.

This must be tested against degree-preserving and cost-matched controls.

### 6. Dynamics on topology

Human connectome topology can shape dynamic phenomena such as traveling waves and
frequency gradients. Therefore topology and dynamics must not be treated as identical
problems.

**Engineering hypothesis:** a useful architecture may emerge from the interaction
between sparse topology, recurrent state, delays, and local dynamics.

Future metrics:
- propagation speed
- latency
- oscillatory stability
- activity persistence
- synchronization
- task performance

## Cross-species rule

A candidate rule becomes a stronger biological design principle only when evidence
supports it across multiple scales/species or when a mechanism has a clear causal
and measurable explanation.

We explicitly avoid the statement "human brain is the peak of evolution" as a
scientific premise. Human brain complexity is an important reference for this project,
but evolutionary optimality is not established by complexity alone.

## Experimental ladder

1. Fly structural constraints.
2. Fly topology + spatial constraints.
3. Fly dynamics.
4. Human connectome constraints.
5. Cross-species invariants.
6. Architecture benchmark.
7. Hardware/resource benchmark.

## Key references

- Kulkarni & Bassett (2025), *Toward Principles of Brain Network Organization and Function*.
- Bullmore & Sporns, *The economy of brain network organization*.
- Human rich-club and modular-network literature.
- Koller et al. (2024), *Human connectome topology directs cortical traveling waves and shapes frequency gradients*.

This document is a research constraint map, not a claim that any listed biological
property automatically improves computation.
