# M5 Multi-Constraint Validation Protocol

## Objective

Determine whether a synthetic connectome can reproduce selected biological constraints without hiding which constraint caused each improvement.

## Constraint ladder

Run the same observed-data split and target edge budget through:

1. density only;
2. density + degree distribution;
3. + reciprocity;
4. + hierarchy/modularity;
5. + spatial distance law;
6. + explicit long-range budget;
7. + rich-club/backbone;
8. full multi-constraint model;
9. + typed cooperation/competition;
10. + dynamic/state-dependent hierarchy;
11. + bounded-capacity hierarchy / saturation-triggered expansion.

The new capacity branch is a computational hypothesis, not a claim that connectomes literally follow atomic shell rules.

## Capacity-triggered hierarchy experiment

Compare:

- A: uniform-density topology;
- B: capacity hierarchy;
- C: capacity hierarchy + sparse backbone;
- D: hierarchy control with capacity assignment randomized.

Match node count, directed edge count, degree distribution, approximate modularity, spatial/wiring-cost budget, parameter count, and event/compute budget as far as the generator permits.

Primary capacity metrics:

- module occupancy distribution;
- fraction of saturated modules;
- hierarchy depth;
- inter-module interface count;
- hierarchy-crossing fraction;
- communication events/messages;
- wiring cost;
- task performance and memory capacity in M6+;
- timescale diversity;
- fault tolerance.

### Required ablations

- remove capacity limit;
- change capacity while holding total edges fixed;
- disable saturation-triggered expansion;
- vary hierarchy depth;
- vary interface budget;
- remove sparse backbone;
- randomize module assignment;
- preserve degree sequence while rewiring.

A capacity result is only useful if it survives these controls.

## Metrics

### Structure
- node count;
- directed edge count and density;
- in/out degree quantiles and coefficient of variation;
- reciprocity;
- modularity and participation;
- rich-club density across multiple thresholds;
- motif/graphlet statistics;
- edge-length distribution;
- long-range edge fraction;
- within-level vs hierarchy-crossing edge fractions.

### Cost/resource proxies
- total wiring length;
- mean edge length;
- maximum and mean fan-in/fan-out;
- messages per simulated step;
- state memory per node;
- communication bytes/event when a simulator exists.

### Dynamics (M6+)
- activity autocorrelation;
- propagation latency;
- state-transition/control energy;
- multiscale mode reconstruction;
- effective hierarchy by state;
- cooperative vs competitive interaction effects;
- task performance after topology is fixed.

## Human-reference constraints

Human literature is used as a reference layer, not as a target to imitate literally.

Current hypotheses:

- nested hierarchy;
- within-level local connectivity;
- selective hierarchy-spanning connections;
- rich-club integration backbone;
- spatially constrained wiring;
- multiscale topology-to-dynamics coupling;
- state-dependent effective hierarchy;
- distributed spatial influence/control.

## Fly embodied-control constraint

The 2026 unified fly brain-and-nerve-cord connectome motivates a separate hypothesis: local sensory-to-effector feedback loops can remain relatively autonomous while long-range ascending/descending pathways coordinate behavior modules.

## Cooperation/competition constraint

A 2026 cross-species mammalian study motivates a typed interaction branch:

- local/modular cooperation;
- diffuse long-range competition.

The engineering hypothesis is not that mixed signs are universally beneficial; it is that mixed interaction signs may create a different stability/expressivity/resource trade-off.

## Novelty gate

No novelty claim is permitted from matching these properties individually.

## Reproducibility

Record dataset/version, preprocessing, node/edge sampling, random seed, generator parameters, null-model definition, metric definitions, software commit, and environment information.

Do not report real-data results until the experiment is actually executed.

## Quantum-information-inspired interface branch

This branch translates quantum-information and tensor-network ideas into classical, falsifiable constraints. It does not assume quantum computation or biological quantum effects.

### Q1 — Effective-state interface

For each module, preserve a detailed internal state but expose only a compact interface state to other modules.

Compare:
- full-state communication;
- fixed pooled state;
- learned compact state.

Match:
- topology;
- parameter count where possible;
- total communication budget;
- compute budget.

Measure:
- task performance;
- information retained by the interface;
- messages/bytes per step;
- latency;
- robustness to internal perturbations.

### Q2 — Interface capacity

Vary the maximum interface bandwidth/state dimension while holding node count and total edge budget fixed.

Test:
- unrestricted;
- fixed small interface;
- adaptive interface.

### Q3 — Structured redundancy

After establishing Q1/Q2, compare:
- no redundancy;
- uniform redundancy;
- targeted redundancy on high-value interfaces/backbone.

Measure failure recovery and redundancy cost.

### Q4 — Effective geometry

Derive an interaction/communication-based distance and compare it with Euclidean and graph distance as predictors of:
- communication load;
- activity propagation;
- task-relevant influence.

### Q5 — Relational-strength budget

Hold edge count fixed but constrain the number/strength of high-weight relationships per module. Compare with unconstrained and strength-shuffled controls.

### Interpretation gate

Quantum-inspired branches are only retained if the observed benefit survives equal-resource controls and can be explained without invoking quantum mechanics. No claim of quantum biological computation is made.


## M6 cross-link: bounded interfaces + higher-order coordination

The interface hypothesis now has a second layer. Pairwise module-to-module messages may
not capture all task-relevant collective interactions. Recent 2026 brain-network work
shows higher-order interaction measures can reveal redundancy, synergy and topological
scaffolds that are not reducible to pairwise connectivity; these measures also align
with cortical hierarchy. This motivates a controlled engineering branch rather than an
assumption that hyperedges are inherently superior.

### H1 — Pairwise vs higher-order interface

Compare:
- pairwise bounded interfaces only;
- bounded 3-module coordination simplices;
- unrestricted higher-order coordination.

Match:
- total transmitted state values;
- active relation count;
- compute budget;
- topology where possible.

Measure:
- task utility;
- communication volume;
- latency;
- redundancy vs synergy;
- robustness after module ablation.

The key question is whether a small number of higher-order relations provides
measurable benefit per resource unit over pairwise communication.

### H2 — State-dependent coordination

Candidate simplices should be activated only when the current module states make them
useful. Compare static relation sets against state-dependent activation under the same
maximum relation budget.

### H3 — Interface specialization

Measure whether narrowing the interface changes module specialization over time.
This directly connects M6 to the 2025 resource-constrained modularity result.

No novelty claim is permitted for higher-order interactions, hypergraphs, information
bottlenecks, or tensor-network compression individually. Any future claim must concern
a narrowly defined combination and survive matched-resource controls.
