# Atomic-Structure Analogy for Connectome Architecture

## Status
**Hypothesis / cross-domain design analogy — not a biological claim and not evidence that neural systems obey atomic rules.**

Atomic structure motivates a useful abstraction: discrete levels, bounded occupancy, ordered resource costs, saturation, and transitions between levels. Electron configurations are governed by quantum mechanics; their exact shell/subshell capacities are not an architectural recipe.

## Architectural hypothesis
Test whether scalable computation benefits from:

**bounded local capacity -> saturation -> structured expansion -> sparse interfaces**

This is deliberately more abstract than copying atomic numbers.

## Candidate computational rules

- R1 — Bounded local occupancy: modules have explicit node/state/edge/event/interface budgets.
- R2 — Saturation-triggered expansion: once a module reaches capacity, add a peer or higher-order module rather than densifying the saturated module indefinitely.
- R3 — Cost ordering: prefer local/cheap routes until capacity or performance saturates, then recruit more expensive long-range coordination.
- R4 — Sparse interfaces: modules may be internally dense while exposing only a limited number of external module interfaces.
- R5 — Discrete hierarchy depth: test where additional hierarchy levels stop improving memory, multitasking, temporal diversity, robustness, or communication efficiency.

## Prototype implementation

src/generator/capacity.py now provides:

- build_capacity_hierarchy() — fills modules to module_capacity before creating the next peer module;
- capacity_hierarchy_graph() — adds hierarchy-aware directed connectivity with an explicit external interface budget;
- deterministic seeds and exact edge targets when the interface budget permits.

This is a generator prototype, not a validated biological model.

## Strong controls

The intended benchmark is:

A. uniform-density network;
B. bounded-capacity hierarchy;
C. bounded-capacity hierarchy + sparse control backbone;
D. hierarchy with the same levels but randomized capacity/assignment.

Controls must match node count, edge count, degree distribution, approximate modularity, wiring cost, parameter count, and event/compute budget where feasible.

## Falsification

The capacity hypothesis is weakened if its benefit disappears after these controls. It is also weakened if increasing hierarchy depth monotonically improves results without a reproducible saturation point.

## Prior-art warning

Capacity-triggered modular growth is not new in isolation. Earlier network-growth models explicitly divide modules when they reach a size threshold and thereby generate modular/hierarchical structure. Therefore the project must not claim novelty for "saturation creates modules" alone.

The narrower research question is whether a resource-matched, connectome-constrained capacity rule plus sparse interfaces/backbone produces a measurable computational advantage that survives strong controls.

## Scientific gate

No novelty claim until the combined mechanism has:

1. exact method specification;
2. targeted prior-art search;
3. reproducible experiments;
4. ablations;
5. uncertainty estimates;
6. held-out validation;
7. resource-matched controls.
