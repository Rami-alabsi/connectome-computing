# Project Status

## Current position

**Stage: M6 — resource-constrained multiscale simulator + real-data validation**

**Prototype-phase note:** the current implementation phase was built in a single intensive session. Treat the repository as a research prototype scaffold until real-data execution, matched controls, ablations and reproducible artifacts have been completed.

Experimental spine:

**biological evidence → structural abstraction → bounded resources → effective state → relational coordination → dynamics → benchmark → ablation → scaling**

Biological structure is evidence used to generate falsifiable computational abstractions, not a specification to copy literally.

## Evidence state

- Software scaffolding and unit tests exist for M1–M6 components.
- Real FAFB v783 data have now been **successfully executed through the publication-aligned rich-club runner** in GitHub Actions Run `35962522090` on commit `9138d7280b4ca5219ed2f56560569751a6aafe99`.
- This is a real-data rich-club benchmark, not completion of the full ingestion/profile → reciprocity → motif → spatial chain. Those downstream biological gates remain open.
- The benchmark used v783, pair-level synapse aggregation, a 5-synapse threshold, 2 CFG-style degree-preserving nulls, and a total-degree sweep 20–120. It preserved edge count and directed in/out-degree sequences for both nulls.
- Therefore M1/M2 biological completion is now partially validated for this specific rich-club execution path, but the broader biological pipeline is still not validated.
- No RSS performance result is currently accepted as scientific evidence.

## Implemented prototype components

- [x] M0 research foundation and scientific guardrails
- [x] M1 FlyWire/Codex ingestion code
- [x] M2 graph-analysis code
- [x] M2b motif/null-model code
- [x] M3 biological annotation code
- [x] M4 architecture primitives
- [x] M5 modular/sparse/hierarchical/spatial generators and validation code
- [x] M5 capacity-triggered hierarchy prototype
- [x] M6 effective-state interface and communication accounting
- [x] M6 bounded higher-order coordination primitive
- [x] M6 stateful local-plus-interface simulator
- [x] M6 state-dependent routing primitive
- [x] M6 dynamic relational layering primitive
- [x] M6 field-mediated relational layer prototype
- [x] M6 controlled RSS benchmark implementation
- [x] M6 RSS information-flow semantics correction
- [x] M6 RSS matched-control runner
- [x] M6 shuffled-context null implementation
- [x] M6 shuffled-collective null implementation
- [x] Publication-aligned FAFB v783 rich-club execution path

## Active workstreams

### 1. Real biological anchor

The first real-data rich-club execution has now succeeded. The next step is to extend this to the complete streaming profile pipeline and measure directed degree,
reciprocity, hubs/rich-club, motifs, hierarchy/modularity, spatial/contact
constraints, long-range structure and multi-constraint interactions.

Current public Codex identifies FAFB v783 as 139,255 neurons and 3,732,460
directed connection pairs; BANC v888 is a newer 2026 brain-and-nerve-cord
snapshot. These published counts are reference checks, not yet a result from our
local ingestion pipeline.

This remains the main biological gate.

### 2. Dynamic Relational State Space (RSS)

**local state → effective module state → overlapping relational layers → selective direct routes → bounded collective relations**

A relation may carry endpoint pair, layer/type, context, order, strength/priority,
activation and cost. This is not a literal fourth spatial dimension.

### 3. M6-RSS benchmark

Current conditions:

- A: flat pairwise;
- B: fixed hierarchy;
- C: dynamic overlapping context layers;
- D: dynamic layers + bounded collective pooling;
- E: fixed overlap;
- F: random context-matched routing;
- G: stable core + flexible periphery;
- H: shuffled-context null;
- I: shuffled-collective null.

### 4. RSS semantic correction — critical

The earlier C/D implementation gave the correct context group as the candidate
pool. At budgets that covered that group, low error could arise from candidate
coverage rather than context-aware routing.

C/D now rank the **full candidate pool** under the same active-route budget,
with the current context group receiving priority. H uses a deterministic
same-cardinality shuffled priority group. This isolates contextual priority
from simple group coverage.

**All previous 6,720-row RSS results generated before this correction are
invalid for scientific interpretation and must not be reused as evidence.**

The runner is configured for seeds 0–4 and budgets 2/4/6/8 with matched module
count, state dimension, bytes per relation, contexts and sequence length.

D remains a bounded collective-pooling surrogate, not a general nonlinear
higher-order interaction model.

## Required controls before interpretation

- shuffled-context null — **implemented**;
- parameter/interface-dimension matching;
- shuffled collective-relation null — **implemented**;
- seed-level variance/95% CI summary — **implemented** (replication unit is seed, not timestep);
- sparse brokerage ablation;
- explicit stable-core removal;
- candidate-topology matching where appropriate.

## Potential-path branch

Future classical hypothesis:

**candidate paths → state/context evolution → selective activation/suppression → delayed commitment**

Dynamic routing, candidate-path and multipath mechanisms already have substantial
prior art. Therefore no novelty is assumed. The branch remains blocked until RSS
controls and artifacts are validated.

## M6-COSMIC and multiscale branches

Re-run M6-COSMIC after the bounded-state correction before interpreting scaling.
Do not interpret hierarchy depth until parent grouping is genuinely multilevel.

## Scientific status

**No benchmark advantage or novelty claim yet.**

### FAFB v783 rich-club benchmark — 2026-09-24

Run `35962522090` completed successfully. Artifact: `fafb-v783-rich-club-publication-benchmark`, SHA-256 `3054b154f18dfd6bae821d084bbd159f1c1d2d5ee13dd90e1ab7b65bd297aea1`.

Measured execution:
- 3,732,460 unique directed pairs after pair-level synapse aggregation and the 5-synapse threshold;
- 2 degree-preserving nulls;
- 3,732,460 target swaps per null;
- wall time 16:11.20;
- maximum resident set size 1,900,488 kB (~1.81 GiB);
- exact edge-count, in-degree and out-degree preservation reported for both nulls.

The observed-to-null curve crosses the repository's descriptive `phi_norm > 1.01` flag at degree 27, is still above that flag at degree 120, and reaches its maximum in the 20–120 sweep at degree 97. This is a **2-null benchmark observation**, not the final 100-null publication-aligned result, and must not be presented as a replication conclusion.

The run also provides the first successful real-data execution of the rich-club path. Reciprocity, motif, spatial/profile execution and the full multi-analysis artifact chain remain open gates.

The RSS workflow now emits a seed-level uncertainty summary (mean, sample SD and
normal-approximation 95% CI) so timestep count cannot be mistaken for replication.
A Codex static-download smoke-test workflow has also been added for the FAFB v783
connection resource. It now streams the public `connections_princeton` resource,
checks the header/first row, and validates the streamed node/pair counts against
Codex's published FAFB reference (139,255 neurons; 3,732,460 directed connection
pairs). The workflow has been pushed, but its artifact/result has not yet been
inspected here, so no downloaded-data result is being claimed.

CI success is implementation evidence only. Scientific claims require executed
artifacts, matched-resource controls, ablations, multiple seeds and reproducible
analysis.

## Immediate sequence

1. Keep the repaired rich-club test green; current main test run `35964684034` is successful.
2. Add/verify swap-attempt and successful-swap accounting before the 100-null CFG run; the current artifact records the requested swap target but not the realized successful-swap count.
3. The CFG implementation now records requested swaps, realized successful swaps, attempts, and whether the target was fully reached. Verify these fields in the next artifact before scaling to 100 nulls.
4. Decide whether to optimize the pure-Python CFG implementation before scaling from 2 to 100 nulls; the measured 16:11 for 2 nulls implies roughly 13.5 hours at strictly linear scaling, so this should be measured/optimized rather than assumed.
4. Run the publication-grade CFG ensemble only after the null randomization accounting is explicit.
5. Extend the real FAFB execution to the complete streaming profile pipeline: download → profile → rich-club → reciprocity → motif → spatial.
6. Re-run the corrected RSS matrix and inspect the CSV plus seed-level uncertainty summary.
2. Determine whether C/D retain any advantage against H/F and whether D retains any advantage against I at matched budgets.
3. Add sparse-brokerage and stable-core-removal ablations, then parameter/interface and topology matching.
4. Execute the FAFB v783 download smoke test, then run the real ingestion/profile pipeline and compare its counts with the published reference counts.
5. Re-run M6-COSMIC after the bounded-state correction.
7. Only then reassess the potential-path branch.
8. Scale only after mechanisms survive controls.

## Cross-domain rule

Quantum information, holography, cosmic web and social-network analogies are hypothesis generators only. They never substitute for connectome evidence or matched non-biological controls.

## Compass

**evidence → abstraction → falsifiable prediction → matched control → implementation → execution → ablation → scaling → prior-art recheck**
