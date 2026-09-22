# Project Status

## Current position

**Stage: M6 — resource-constrained multiscale simulator + real-data validation**

Experimental spine:

**biological evidence → structural abstraction → bounded resources → effective state → relational coordination → dynamics → benchmark → ablation → scaling**

The project does not attempt to reproduce a fly or human brain literally. Biological structure is evidence used to generate falsifiable computational abstractions.

### Completed

- [x] M0 Research foundation
- [x] M1 FlyWire/Codex ingestion layer
- [x] M2 structural graph analysis
- [x] M2b motif/null-model foundation
- [x] M3 biological annotation layer
- [x] M4 architecture primitives
- [x] M5 modular/sparse/hierarchical/spatial generators and validation
- [x] M5 capacity-triggered hierarchy prototype
- [x] M6 effective-state interface and communication accounting
- [x] M6 bounded higher-order coordination primitive
- [x] M6 stateful local-plus-interface simulator
- [x] M6 state-dependent routing primitive
- [x] M6 dynamic relational layering primitive
- [x] M6 field-mediated relational layer prototype
- [x] M6 controlled RSS benchmark implementation + tests

## Active workstreams

### 1. Real biological anchor

Run FAFB v783 through a streaming profile pipeline and measure directed degree,
reciprocity, hubs/rich-club, motifs, hierarchy/modularity, spatial/contact
constraints, long-range structure and multi-constraint interactions.

This remains the main biological gate.

### 2. Dynamic Relational State Space (RSS)

The current abstraction moves beyond a single tree:

**local state → effective module state → overlapping relational layers → selective direct routes → bounded higher-order relations**

A relation may be represented by endpoint pair, layer/type, context, order,
strength/priority, activation and cost.

This is **not** a claim of a literal fourth spatial dimension. It is an engineering
representation of time-varying multiplex/higher-order relational structure.

### 3. M6-RSS benchmark

Implemented four controlled conditions:

- A: flat pairwise;
- B: fixed hierarchy;
- C: dynamic overlapping context layers;
- D: dynamic layers + bounded higher-order relation.

Tasks include global aggregation, pair-sensitive information, context-selected
group information and temporal context switching.

Measured resources include active relations, transmitted bytes, routing churn
and higher-order relation activation. Results are not yet interpreted
scientifically until the CI artifact is inspected.

### 4. Required next controls

Before any performance interpretation, add:

- fixed overlapping groups;
- random context-dependent routing with the same active-route budget;
- parameter/interface-dimension matching;
- matched active-relation count;
- shuffled higher-order relation null;
- stable-core + flexible-periphery ablation;
- sparse brokerage ablation.

### 5. Multiscale and cosmic branches

M6-COSMIC compares explicit sparse communication, bounded latent-field
coordination and hybrid field + sparse backbone. Its scaling signal must be
rechecked after the bounded-state correction before any scientific claim.

Hierarchy depth must not be interpreted until parent grouping is genuinely
multilevel rather than a one-level prototype.

## Scientific evidence boundary

Current network science establishes multilayer, temporal and higher-order
representations; recent reviews explicitly call for deeper integration of these
structures. Higher-order brain analyses also show that collective interaction
metrics can expose information beyond pairwise connectivity. These are prior-art
constraints and motivation, not evidence that the project combination is novel.

## Scientific status

**No benchmark advantage or novelty claim yet.**

CI passing means implementation correctness for the tested fixture, not scientific
validation. Any scientific result requires executed data, matched-resource
controls, ablations and reproducible artifacts.

## Immediate sequence

1. Inspect the M6-RSS CI artifact after completion.
2. Fix implementation issues before adding more mechanisms.
3. Add the required RSS controls.
4. Execute the RSS matrix across multiple seeds and budgets.
5. Analyze error/resource tradeoffs without collapsing them into one score.
6. Re-run M6-COSMIC after the bounded-state correction.
7. Complete FAFB v783 profiling.
8. Only then consider scaling and exact prior-art recheck.

## Cross-domain rule

Quantum information, holography, cosmic web and social-network analogies are
hypothesis generators and mathematical/engineering abstractions only. They do not
override the biological anchor and never substitute for non-biological controls.

## Compass

**evidence → abstraction → falsifiable prediction → matched control → implementation → execution → ablation → scaling → prior-art recheck**

