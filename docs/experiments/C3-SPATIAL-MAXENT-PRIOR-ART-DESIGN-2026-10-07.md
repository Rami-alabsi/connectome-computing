# C3 — Spatial / Maximum-Entropy Sensitivity Prior-Art and Design Gate

Date: 2026-10-07

## Purpose

This record prevents the next spatial sensitivity experiment from being invented without checking the strongest directly relevant prior art.

The primary C2 null is unchanged. This document defines a design gate before implementing any new spatial/max-entropy null.

## Current project state

C2 artifact-complete realizations #45, #46, and #47 are complete under the same primary constraint surface:

- FAFB v783
- 3,732,460 unique directed pairs
- exact in-degree and out-degree
- exact source-block -> target-block counts
- exact global arbor-distance-bin histogram
- no self-loops
- no duplicate directed edges
- 9,869 edges without complete dominant block assignment frozen

All three independent seeds produced a maximum phi_norm around 1.00762–1.00775 and no phi_norm > 1.01. The full curves are highly reproducible, but formal mixing/convergence is still open.

## New prior-art finding

Salova & Kovács, Network Neuroscience 2025, "Combined topological and spatial constraints are required to capture the structure of neural connectomes", explicitly develops scalable canonical maximum-entropy models for neural connectomes.

The paper considers models including:

- d: binned edge probability as a function of distance
- k: degree sequence
- k + L: degree sequence + total wiring length
- c: hard physical-contact constraint
- d + c: distance dependence + contact constraint
- k + c: degree sequence + hard contact constraint

The paper reports analyses on fruit fly, mouse, and human connectomes and states that combined topological/spatial constraints capture additional network properties.

Important scope distinction:

- The fly dataset used in that paper has 16,804 nodes in the reported network table, not the project's 138,584-node FAFB v783 graph.
- Their framework is a canonical maximum-entropy ensemble with soft expected constraints and/or hard contact constraints.
- The current project's C2 is a directed, exact, microcanonical-style swap ensemble preserving the exact degree sequence, exact NPC-like block-pair counts, and exact global arbor-distance-bin histogram.
- Therefore "maximum-entropy spatial null for neural connectomes" is not itself novel project territory.

## Consequence for the project

Do NOT implement a generic "maximum entropy spatial null" and present it as a novel method.

The prior-art question must instead be:

1. What does a canonical maximum-entropy distance/degree model predict for the project's exact FAFB v783 graph?
2. How does that prediction compare with the existing hard-binned spatial null and C2?
3. Does adding the project's NPC-like mesoscale block constraint produce an ensemble that is materially different from the published degree/spatial maximum-entropy families?
4. Does any residual survive all three families?

## Proposed C3 sensitivity families

### C3-A — Canonical spatial maximum-entropy baseline

A literature-aligned canonical model should be treated as a prior-art replication/sensitivity control, not as a novelty claim.

Candidate constraints to evaluate separately:

- node-level degree constraints with spatial dependence;
- degree + total wiring length;
- where feasible, a directed adaptation must be explicitly justified rather than silently copied from an undirected model.

The exact mathematical ensemble must be written before implementation.

### C3-B — NPC-aware maximum-entropy extension

If and only if C3-A is validated, evaluate whether the project-specific mesoscale block structure can be added as an explicit constraint.

This must be treated as a new hypothesis/control construction, not as an established literature method.

Potential formulation:

- node-level directed degree constraints;
- source-block -> target-block expected edge counts;
- spatial distance statistic(s), either expected total wiring cost or a justified distance kernel;
- entropy maximized subject to those constraints.

The resulting ensemble must be defined mathematically before code is written.

## Critical methodological boundary

Do not silently replace the primary C2 hard constraints with a stronger joint block-pair × distance-bin hard histogram.

That would define a different null surface.

If such a model is useful, it must be labeled as a separate sensitivity null and compared against C2.

## Validation requirements before FAFB-scale execution

Any new sampler/model must first pass:

1. exact mathematical definition of the target ensemble;
2. synthetic-graph validation;
3. parameter-recovery or constraint-recovery test;
4. symmetry/detailed-balance proof for MCMC, or direct independent sampling justification for a canonical model;
5. exact or quantified constraint error;
6. duplicate/self-loop handling;
7. reproducibility under independent seeds;
8. comparison against known limiting cases;
9. artifact schema and provenance;
10. runtime/memory benchmark on a smaller FAFB subset.

No FAFB full-scale scientific run should begin before these gates pass.

## Scientific decision rule

The goal is not to maximize or minimize phi_norm.

The goal is to determine whether the C2 structural-control observation remains stable when compared with an independently justified maximum-entropy spatial family.

Interpretation:

- residual disappears across independent model families -> stronger evidence that simpler residuals were explained by known structural/spatial constraints;
- residual persists -> higher-priority candidate for mechanistic investigation;
- model families disagree materially -> investigate the difference between their ensemble definitions before interpreting biology;
- unexpected result -> preserve it as a discovery/control signal and audit before interpretation.

## Current status

Primary C2: CLOSED as three-seed artifact-complete replication.

C2 formal mixing/convergence: OPEN.

Gate C: OPEN.

C3 spatial/max-entropy sensitivity: DESIGN GATE OPEN.

Structure -> function: BLOCKED until Gate C.

## References

Salova, A. & Kovács, I. A. (2025). Combined topological and spatial constraints are required to capture the structure of neural connectomes. Network Neuroscience, 9(1), 181–206. DOI: 10.1162/netn_a_00428.

The paper is open access and reports scalable canonical maximum-entropy connectome models, including degree and spatial/contact constraints.

