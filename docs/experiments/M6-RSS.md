# M6-RSS — Dynamic Relational State Space benchmark

## Purpose

This experiment operationalizes the **Relational State Space (RSS)** hypothesis:
hierarchy is one relational coordinate alongside overlapping layers, context,
temporal activation, and bounded collective relations.

This is a classical engineering benchmark. It is not a model of human social
behavior, brain physics, quantum gravity, or a literal fourth spatial dimension.

## Conditions

| Condition | Representation | Routing | Collective relation |
|---|---|---|---:|
| A | flat pairwise | state-ranked | no |
| B | fixed hierarchy | fixed | no |
| C | overlapping context layers | dynamic | no |
| D | overlapping context layers | dynamic | bounded collective |
| E | fixed overlapping | fixed | no |
| F | random context-matched | random | no |
| G | stable core + flexible periphery | state/context priority | no |
| H | shuffled-context null | dynamic, wrong context priority | no |
| I | shuffled-collective null | same dynamic priority, wrong collective membership | bounded collective |

D's current collective operation is deliberately a **bounded group pooling
surrogate**. It is not yet a general nonlinear higher-order interaction model.
Any stronger higher-order claim requires a separate interaction function and
null model.

## Information-flow boundary

The benchmark enforces:

**hidden source states → selected communication routes → visible source subset → prediction**

The evaluator may compute the hidden target from the complete fixture only for
measurement. A condition cannot use untransmitted source states to form its
prediction.

For pair-sensitive tasks, the prediction is exact only when both target
endpoints are actually transmitted.

## Candidate-pool correction

An earlier RSS implementation gave C/D the correct context group as the
candidate set. At budgets large enough to cover that group, near-zero error
could therefore arise from **candidate coverage alone**, not from routing
intelligence.

This has been corrected. C/D now rank the **full module candidate pool** under
the same active-route budget, with the context group receiving priority. H uses
a deterministic same-cardinality shuffled priority group while keeping the
same full candidate pool and budget.

This is the required first null for separating context-aware routing from
budget-sized group coverage.

## Tasks

- **global** — aggregate over all hidden modules;
- **pair** — a specific ordered module pair;
- **context** — aggregate over the active overlapping group;
- **temporal** — context-dependent state channel over a sequence.

## Matched-resource protocol

The runner evaluates:

- seeds: 0–4;
- active relation budgets: 2, 4, 6, 8;
- identical module count and state dimension;
- identical bytes per transmitted relation;
- identical sequence length and contexts.

The benchmark records error, active relations, transmitted bytes, routing churn
and collective-relation activation. No single scalar score is used.

## Controls

E is a fixed-overlap control. It separates overlap itself from state-dependent
routing.

F is a random context-dependent routing control with the same active-route
budget. It tests whether route churn alone explains an effect.

G is a stable-core/flexible-periphery control. It tests whether a small
persistent coordination core explains an apparent dynamic-routing benefit.

H is the **shuffled-context null**. It preserves candidate-pool size, group
cardinality, route budget and byte budget, but breaks the mapping between the
current context and the prioritized group.

I is the **shuffled-collective null**. It keeps the dynamic route-selection
mechanism and the same-size collective operation, but replaces the true
context group used by the collective pooling operation with a deterministic
same-cardinality shuffled group. This isolates the contribution of correct
collective membership from the contribution of dynamic route priority.

Required future controls remain:

- parameter/interface-dimension matching;
- shuffled collective-relation null — **implemented**;
- sparse brokerage ablation;
- explicit stable-core removal;
- candidate-topology matching where appropriate.

## Interpretation gate

A dynamic condition is not considered advantageous merely because its raw error
is lower. An effect must survive matched active-relation, transmitted-byte,
parameter/interface and topology controls, and should be stable across seeds
and budgets.

The current benchmark is now ready for a fresh execution. Previous 6,720-row
results must **not** be used as evidence for C/D because they were generated
before the candidate-pool correction.

CI success demonstrates implementation/test correctness only. It is not
scientific validation.

## Prior-art boundary

Dynamic routing, multipath routing, multilayer networks and higher-order
networks are established fields. Recent work continues to study adaptive
routing under resource constraints, so the benchmark does not treat dynamic
routing itself as novel. citeturn0search0turn0search1

The research question remains whether this particular combination of
resource-bounded effective interfaces, overlapping relational contexts, sparse
coordination and later delayed path commitment yields an independently
measurable engineering trade-off.

## Biological gate

The architecture is not considered connectome-supported until it is compared
against real FlyWire structure. Current public Codex data identify FAFB v783 as
139,255 neurons and 3,732,460 directed connection pairs; BANC v888 is the newer
2026 brain-and-nerve-cord snapshot. citeturn0search0turn0search1

FAFB profiling remains a separate validation stage; synthetic benchmark results
must not be presented as biological evidence.

## Current status

The information-flow semantics, candidate-pool correction, shuffled-context null,
shuffled-collective null, matched controls and multi-seed/multi-budget runner are implemented.
The next gate is CI execution plus inspection of the regenerated CSV artifact.
No benchmark advantage or novelty claim is made yet.


## Corrected sweep execution record (2026-09-23)

The corrected 9-condition sweep completed successfully in GitHub Actions Run #17 at commit `af62dc88b640fd7e25bab7780344f0d311c66b79`. The artifact contains 8,640 rows (5 seeds × 4 budgets × 9 conditions × 4 tasks × 12 timesteps). Artifact SHA-256: `337823ce9be4e89cf0c015448cc58a4a4dd5e44e3daff721c0fbdb00a391cca`.

Initial inspection shows an important pattern: D (dynamic higher-order collective pooling) and I (shuffled-collective null) are identical on the global and pair tasks at all budgets, while D has lower error on context/temporal tasks at budgets 6 and 8. This is an implementation-level observation from the synthetic fixture, not yet a scientific claim. It also means the next gate should test whether the D-vs-I separation survives parameter/interface matching, multiple task generators, and topology-matched controls rather than treating the current result as evidence for higher-order superiority.
