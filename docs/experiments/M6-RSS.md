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
- sparse brokerage ablation — **implemented**;
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


## Control refinement (2026-09-23)

The fixed-overlap baseline was refined in commit `d42867e950f3a9ece4813dc33af61cba460070e0`.
Its fixed route order now prioritizes modules by **context-membership count** and then
stable module ID. This keeps the baseline explicitly overlapping while avoiding an
arbitrary preference for the union of contexts 0 and 1.

The regression suite was strengthened in commit `33b71fd48a078a46920d179141a25b8033c18c3e`:
- fixed-overlap source sets must be identical across contexts;
- shuffled-context null must preserve group cardinality while changing the
  context-to-group mapping.

This refinement matters because the benchmark is intended to distinguish overlap
from adaptive context routing, not to give a fixed baseline an accidental
context-specific advantage.

## Updated prior-art gate (2026-09-23)

Recent 2026 work reinforces a stricter interpretation of the RSS higher-order
branch. Lucas et al. formalize **functional reducibility** of higher-order
networks and report that some empirical systems retain essential higher-order
information while others can be reduced to pairwise structure; they also find that
no single simple structural metric explains reducibility. citeturn0search0

Milisav et al. report that hierarchical modular reservoirs can improve memory and
multitasking, but performance saturates rapidly with additional hierarchy and a
third level rarely adds further improvement over the second. citeturn0search1

Accordingly, this project will not interpret either hierarchy depth or higher-order
relations as intrinsically beneficial. The next scientific gate is to measure
**when** a relation order is functionally irreducible under matched communication,
interface and computation budgets.


## Corrected control sweep result (2026-09-23)

M6 RSS Run #19 completed successfully on commit `33b71fd48a078a46920d179141a25b8033c18c3e`.
The artifact contains 8,640 rows; artifact SHA-256:
`158de25af4d0fb42a720f76b5d1b29f897c88814743ff8a2e296cfaf31049c52`.

The balanced fixed-overlap control changed its numerical profile as expected,
confirming that the previous fixed-overlap result depended partly on its
arbitrary Context-0/Context-1 union. The corrected control now uses
context-membership count rather than context labels.

The D-vs-I paired observation remains qualitatively present in this synthetic
fixture:
- budgets 2: D and I are identical;
- budget 4: D is modestly lower-error than I on context and temporal tasks;
- budgets 6 and 8: D and I remain identical on global and pair tasks, while D
  reaches approximately zero error on context and temporal tasks and I does not.

This does **not** establish a higher-order advantage. The zero errors arise from
the current synthetic target construction plus bounded group pooling, and the
global/pair equality shows that the collective operation is only exercised on
selected task classes. The result therefore remains a hypothesis-generating
observation.

The next required gate is now explicit:
1. replace the single deterministic task fixture with independently generated
   task families;
2. match interface dimension, pooling compute and transmitted representation;
3. construct topology-matched collective nulls preserving overlap and
   participation statistics;
4. test paired seed effects and uncertainty rather than raw mean error only;
5. test whether the observed D-vs-I separation survives when the collective
   function is not simply the same mean used to define the target.

Only if the separation survives those controls should it be compared with real
connectome-derived structure.


## Sparse brokerage ablation (2026-09-24)

A new control, J_dynamic_layered_no_brokerage, was added. It uses the same full
candidate pool, active-route budget, state ranking and byte budget as C, but
removes multi-context overlap nodes from the context-priority set. The purpose
is to test whether any context-routing effect depends on a small set of
brokerage/overlap nodes rather than on dynamic routing alone.

This is an ablation of the synthetic relational fixture, not a biological claim.
The expected comparison is C versus J under identical seeds and budgets. No
advantage is inferred until the regenerated sweep and uncertainty analysis are
inspected.


### Sparse brokerage ablation — Run #23 result (2026-09-24)

The regenerated sweep includes **J_dynamic_layered_no_brokerage** under the same five seeds, budgets, candidate pool, and byte budget as C. The CI workflow completed successfully and produced 8,640 result rows.

The seed-level summary shows that removing overlap/broker nodes changes error differently by task and budget rather than producing a uniform effect. For example, C minus J mean seed error differences were:
- budget 2: context +0.312, global +0.052, pair 0.000, temporal -0.225;
- budget 4: context -0.091, global +0.091, pair -0.075, temporal -0.161;
- budget 6: context -0.002, global -0.079, pair -0.075, temporal -0.129;
- budget 8: context -0.056, global -0.032, pair -0.075, temporal -0.026.

These are descriptive paired differences, not an overall ranking. They indicate that the contribution of overlap/brokerage is **task- and budget-dependent** in this synthetic fixture. The result does not establish a general brokerage advantage.

The current experiment is also limited by the synthetic task generator and five seeds. The next gate is therefore to preserve the same resource accounting while introducing independent task generators and a topology-matched brokerage null before making a mechanistic claim.
