# CURRENT AUTHORITATIVE STATUS — 2026-10-07

> Compact first-read operational state. Historical entries below remain provenance, not current truth.

- Gate A / CFG: **CLOSED**.
- Gate B / NPC-like: **CLOSED**.
- C0/C1: **CLOSED**; spatial 8-null: **STABLE**.
- C2: **three independent full realizations #45/#46/#47 COMPLETE**; exact seven invariants passed in each.
- C2 max phi_norm: **1.0076221 / 1.0076660 / 1.0077486**; peaks 51 / 50 / 51; no >1.01.
- Three-seed stability audit: **PASSED as reproducibility/control**; correlations 0.9999321–0.9999503; max pointwise spread 0.0006645; pairwise final-edge Jaccard **0.2439655–0.2441324**.
- Formal mixing/convergence: **OPEN**.
- Gate C: **OPEN**.
- C3 prior-art/design gate: **OPEN**; generic canonical spatial max-entropy connectome modeling is prior art.
- C3-A synthetic validation: **not yet scientifically closed; FAFB C3 NOT AUTHORIZED**.
- Structure→function / RSS / architecture / scaling: **BLOCKED**.

**Compass:** C2 replication CLOSED → stability audit PASSED → formal mixing OPEN → C3 design/synthetic validation → spatial/max-entropy sensitivity → Gate C → structure→function → ablations → abstraction → benchmark → scaling.

---

# Project Status

## Current position

**Stage: C2 — artifact-complete realization #1 CLOSED; independent-seed ensemble/mixing OPEN**

**Prototype-phase note:** the current implementation phase was built in a single intensive session. Treat the repository as a research prototype scaffold until real-data execution, matched controls, ablations and reproducible artifacts have been completed.

Experimental spine:

**biological evidence → structural abstraction → bounded resources → effective state → relational coordination → dynamics → benchmark → ablation → scaling**

Biological structure is evidence used to generate falsifiable computational abstractions, not a specification to copy literally.

## Evidence state

- Software scaffolding and unit tests exist for M1–M6 components.
- Real FAFB v783 data have now been **successfully executed through the publication-aligned rich-club runner** in GitHub Actions Run `35962522090` on commit `9138d7280b4ca5219ed2f56560569751a6aafe99`.
- This is a real-data rich-club benchmark, not completion of the full ingestion/profile → reciprocity → motif → spatial chain. Those downstream biological gates remain open.
- The benchmark used v783, pair-level synapse aggregation, a 5-synapse threshold, 2 CFG-style degree-preserving nulls, and a total-degree sweep 20–120. It preserved edge count and directed in/out-degree sequences for both nulls.
- Therefore the FAFB v783 CFG rich-club gate is now closed for this defined analysis path. This is a method-aligned v783 replication/extension, not an exact reproduction of every detail of Lin et al. 2024. The broader biological control hierarchy remains open.
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
- [x] Sparse brokerage ablation (documented as non-general/task- and budget-dependent)
- [x] M6 shuffled-context null implementation
- [x] M6 shuffled-collective null implementation
- [x] Publication-aligned FAFB v783 rich-club execution path

## Active workstreams

### 1. Real biological anchor

The 100-null FAFB v783 CFG ensemble has now completed successfully. The next step is to extend the biological control hierarchy beyond degree-preserving nulls and measure directed degree,
reciprocity, hubs/rich-club, motifs, hierarchy/modularity, spatial/contact
constraints, long-range structure and multi-constraint interactions.

Current public Codex identifies FAFB v783 as 139,255 neurons and 3,732,460
directed connection pairs; BANC v888 is a newer 2026 brain-and-nerve-cord
snapshot. These published counts are reference checks, not yet a result from our
local ingestion pipeline.

This closes the defined CFG/rich-club gate. The next biological gates are neuropil-constrained and spatial/distance-constrained controls.

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

### FAFB v783 real-data anchor — 2026-09-24

Run `35962522090` completed successfully. Artifact: `fafb-v783-rich-club-publication-benchmark`, SHA-256 `3054b154f18dfd6bae821d084bbd159f1c1d2d5ee13dd90e1ab7b65bd297aea1`.

Measured execution:
- 3,732,460 unique directed pairs after pair-level synapse aggregation and the 5-synapse threshold;
- 2 degree-preserving nulls;
- 3,732,460 target swaps per null;
- wall time 16:11.20;
- maximum resident set size 1,900,488 kB (~1.81 GiB);
- exact edge-count, in-degree and out-degree preservation reported for both nulls.

The observed-to-null curve crosses the repository's descriptive `phi_norm > 1.01` flag at degree 27, is still above that flag at degree 120, and reaches its maximum in the 20–120 sweep at degree 97. This is a **2-null benchmark observation**, not the final 100-null publication-aligned result, and must not be presented as a replication conclusion.

### FAFB v783 100-null CFG ensemble — 2026-09-24

Run `35987597540` completed successfully on commit `f53f471de27f0c8cf58d496dcc0885ecfa6a8d4a`. Final artifact: `fafb-v783-rich-club-100null`, artifact ID `10807064530`, SHA-256 `5343abb81fe1cb1a19692e72c5b326fbed87814e99c1476a5bb303164954fae6`.

Measured validation:
- 100 deterministic CFG nulls;
- 3,732,460 requested and successful swaps per null;
- all 100 nulls fully reached the target;
- all 100 preserved edge count, in-degree and out-degree exactly;
- pair-level aggregation and 5-synapse threshold retained;
- `phi_norm > 1.01` is present continuously from degree 27 through 120 in the tested 20–120 sweep;
- `phi_norm` at degree 37 is 1.015363; at degree 75 is 1.047329; at degree 93 is 1.056247; and the sweep maximum is 1.057835 at degree 96;
- degree 120 remains enriched at `phi_norm = 1.041215`.

These values establish a stable CFG-controlled rich-club enrichment pattern under the repository's defined v783 method. They do **not** establish an exact reproduction of Lin et al. 2024 because the dataset version is v783 rather than v630 and the project's null implementation is degree-preserving edge swapping rather than the paper's exact null construction. The result therefore closes the defined CFG gate as a method-aligned replication/extension while leaving neuropil- and spatially constrained explanations open.

The run also provides the first successful end-to-end real-data anchor across structural profile, reciprocity, spatial/neuropil inventory, rich-club, and directed-triad sampling. These artifacts are now inspected. They establish an executed multi-analysis anchor, but they do not by themselves close the CFG publication-alignment gate or justify biological generalization.

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

### Biological Gate A — CFG / FAFB v783

1. **Real-data rich-club benchmark:** completed successfully on Run `35962522090`.
2. **Artifact inspection:** completed at the implementation/runtime level; the benchmark artifact is recorded above. It is still a 2-null benchmark and therefore is not a publication-grade replication.
3. **Swap-quality audit:** verify realized successful swaps, attempts, and target completion in the next artifact. The runner now records these fields.
4. **100-null CFG ensemble:** completed successfully on Run `35987597540`; all 100 nulls reached the target and passed exact degree/edge-count preservation.
5. **Full real-data anchor:** Run `35984738032` completed successfully. All five artifacts were produced and inspected: `profile.json`, `reciprocity.json`, `spatial-profile.json`, `rich-club.json`, and `motif-sample.json`.
6. The anchor reports 138,584 nodes in the connection table and 3,732,460 unique directed pairs after pair-level deduplication; reciprocity is 0.1661585; the spatial inventory contains 79 neuropil labels and 1,002,488 multi-region unique pairs (26.8586%); and the directed-triad sample preserves exact degree/edge-count invariants in both generated nulls.
7. The rich-club nulls both reached the full target of 3,732,460 successful swaps. Null 0 required 3,764,742 attempts; null 1 required 3,764,495 attempts, so the realized swap rate was >99.4% in both runs. This removes the previously open concern about failure to reach the requested swap target for the 2-null benchmark.
8. The 100-null CFG ensemble now closes the defined degree-preserving rich-club gate. The spatial artifact remains descriptive rather than a spatially constrained null, so the broader biological control hierarchy remains open.

### Biological Gates B/C

9. Gate B is closed for the defined 100-null v783 NPC-like benchmark; retain its result as the matched-null source of record.
10. Define and preflight a genuine spatial/distance-constrained null; do not execute a large ensemble until coordinate coverage, units, and invariants are verified.

### RSS / M6

11. Keep RSS/M6 architecture interpretation frozen while the biological Gate A remains open.
12. Sparse brokerage ablation is already completed and documented as task- and budget-dependent; do not re-list it as an upcoming control.
13. Re-run M6-COSMIC only after the bounded-state correction, independently of the FAFB Gate A interpretation.

### Documentation rule

14. Whenever a scientific gate changes state, update `docs/PROJECT-STATUS.md` and the relevant experiment record in the same change window. `AI-CONTEXT.md` remains the pointer to this file; it is not an independent status source.

## Cross-domain rule

Quantum information, holography, cosmic web and social-network analogies are hypothesis generators only. They never substitute for connectome evidence or matched non-biological controls.

### Real-data anchor artifact notes

- `profile.json`: degree metrics are explicitly based on unique directed neuron pairs, not raw region-split rows; weighted synapse total is 50,666,648.
- `reciprocity.json`: 620,180 reciprocal directed edges across 102,757 nodes with reciprocal edges; reciprocity probability 0.1661585.
- `spatial-profile.json`: 5,342,446 raw connection-table rows collapse to 3,732,460 unique directed pairs; 26.8586% of unique pairs occur across multiple regional rows. The artifact explicitly makes no spatially constrained-null claim.
- `motif-sample.json`: one-million attempted samples produced 981,356 accepted observed wedges; the two degree-preserving nulls accepted 981,162 and 981,539. Their exact edge-count/in-degree/out-degree invariants passed. Because the sampler conditions on an outgoing two-neighbor wedge, these counts are a conditional triad-signature profile, not an unrestricted triad census.
- `rich-club.json`: both CFG nulls fully reached the requested 3,732,460 swaps. The 20–120 sweep has `phi_norm` from 1.0044 to 1.0580; the repository's descriptive >1.01 flag begins at degree 27 and remains above it through degree 120. Peak is degree 96 in this run. This remains a 2-null benchmark observation.

## Compass

**evidence → abstraction → falsifiable prediction → matched control → implementation → execution → ablation → scaling → prior-art recheck**



### Gate B first real-data benchmark

Run 36057032102 completed successfully on the corrected NPC runner. Artifact ID 10836101656; SHA-256 6b3181090608f453ad2fa38ed642d18c1b1efb93aebfc592a90a7f24a5dd354a.

- 8 deterministic NPC-like nulls;
- 3,732,460 successful swaps per null;
- exact edge-count, in-degree and out-degree preservation;
- exact preservation of 3,648 source-block -> target-block edge counts per null;
- phi_norm > 1.01 only across degrees 41–69 in this benchmark;
- peak phi_norm 1.015193 at degree 58;
- phi_norm falls below 1 by degree 93 and is 0.990386 at degree 96.

Interpretation status: Gate B remains OPEN. The first real-data NPC benchmark shows a substantial reduction of the CFG enrichment, with a smaller intermediate-degree residual. This is null-controlled benchmark evidence, not a formal significance result and not evidence for an additional topology-specific mechanism. A larger NPC ensemble is required before closure/rejection of Gate B.

## Gate B — NPC-like control execution hardening (2026-09-24)

Before interpreting Gate B, the NPC runner was audited again for data-model consistency. A material issue was corrected: the v783 connection table can contain multiple region rows for the same neuron pair. The NPC graph now aggregates pair-level synapse counts before applying the 5-synapse threshold, matching the project's publication-aligned CFG ingestion rule. The workflow explicitly pins `--min-synapses 5`, and a regression test covers this aggregation/threshold behavior.

The NPC result remains explicitly **NPC-like**, not an exact reproduction of the Lin et al. v630 software/data snapshot. Dominant outgoing-synapse neuropil assignment remains the documented block-definition choice. Gate B stays OPEN until the produced artifact is independently inspected for exact edge count, exact in/out degree, exact source-block→target-block counts, full swap realization, and the complete 20–120 curve.

## Gate B — NPC-like control preparation (2026-09-24)

The repository NPC implementation has been audited against Lin et al. Methods. The published NPC is a degree-corrected stochastic block model: each neuron is assigned to one of 78 neuropil blocks according to the neuropil with the most outgoing synapses; rewiring preserves degree sequences and inter-/intra-neuropil connection probabilities. The project implementation uses the same construction logic on FAFB v783, so it should be described as an **NPC-like v783 extension**, not as an exact v630 reproduction.

The NPC workflow has been aligned to the CFG benchmark's explicit total-degree sweep (20–120, step 1). The current 8-null workflow is an implementation benchmark only. Gate B remains OPEN pending artifact inspection and, if warranted, a larger null ensemble. Required invariants are: exact edge count, exact in-degree, exact out-degree, exact source-block→target-block edge counts, full swap realization, and complete 20–120 rich-club curve.

## State synchronization — 2026-09-27

The master handoff compass is now recorded in `docs/PROJECT-MAP.md`. This section
supersedes older statements in this file that still described CFG as the immediate
blocking gate.

### Current authoritative gate state — 2026-09-28

This section supersedes older Gate C wording below in this historical status file.

- Gate A — FAFB v783 CFG/rich-club: **CLOSED** for the defined method-aligned path.
- Gate B — FAFB v783 NPC-like/neuropil-constrained rich-club: **CLOSED** for the defined 100-null v783 benchmark.
- Gate C0 — authoritative Princeton spatial data definition/coverage: **CLOSED**.
- Gate C1 — spatial-null feasibility: **CLOSED**.
- Spatial 4-null: **VALIDATED**.
- Spatial 8-null: **STABLE** across the expanded seed ensemble.
- C2 — joint NPC-like + arbor-distance-bin: **artifact-complete realization #1 CLOSED; ensemble/mixing OPEN**.
- Computational architecture interpretation remains downstream of the biological control hierarchy.
- No Gate C closure is claimed until the joint C2 control is executable at the required ensemble scale and the stronger spatial/max-entropy controls are addressed.

### Current Gate C execution

Gate B is closed for the defined 100-null v783 NPC-like benchmark.

Gate C0 is complete at the authoritative data-definition/coverage level using the
full FAFB v783 Princeton synapse table:
- workflow: `.github/workflows/m2-fafb-princeton-arbor-spatial-preflight.yml`;
- run: `36315995364`;
- artifact: `10930278435`;
- 80,215,790 synapse-table rows;
- 138,584 graph nodes and 3,732,460 accepted directed pairs;
- 100% outgoing/incoming/both-centroid node coverage;
- observed-edge median arbor distance 481,001 nm;
- sampled non-edge median 2,281,970 nm;
- no scientific spatial-null conclusion yet.

The lighter `synapse_coordinates.csv.gz` path is retained only as a secondary
sensitivity/data-product comparison. Its 86.86% both-centroid coverage is not the
authoritative Gate C0.

A later C1 feasibility run consumed the lighter C0 centroid artifact. Run
`36317314664` / artifact `10930429115` is therefore **superseded** for primary
Gate C1 purposes. Its covered-subgraph invariants remain historical execution
evidence only.

The C1 workflow is now redirected to consume the authoritative Princeton C0 artifact.
No spatial rich-club ensemble has been accepted yet.

### C2 — joint NPC-like + arbor-distance-bin control — runtime/sampler optimization (2026-09-28)

The current C2 constraint surface is:
- exact directed edge count;
- exact in-degree sequence;
- exact out-degree sequence;
- exact source-block → target-block edge counts for edges with complete dominant-block assignment;
- exact global arbor-distance-bin histogram;
- no self-loops;
- no duplicate directed edges;
- edges lacking a complete dominant NPC-like block assignment remain frozen, not removed.

Authoritative feasibility baseline:
- Run 36396525136;
- seed 20260935;
- 100,000 attempts;
- 1,168 accepted swaps (1.168%);
- ~78.1 s runtime;
- exact invariants passed;
- linear extrapolation was ~69.3 h/null.

Block-pair-stratified proposal kernel:
- commit 8fd9f6ad8ca6765a5ed1d60d602ff131a86a7f1c;
- 100,000 attempts;
- 9,789 accepted swaps (9.789%);
- block rejection 0;
- ~86.6 s;
- exact invariants passed;
- linear extrapolation ~9.2 h/null.

Bucket-key lookup optimization:
- commit d12c4ca05310f6ab41fca94237afcd2c461c98af;
- 100,000 attempts;
- 9,789 accepted swaps (9.789%);
- ~55.2 s;
- exact invariants passed;
- linear extrapolation ~5.85 h/null.

The 100k pilots are feasibility/runtime evidence only. They are not null replicates and must not be aggregated as scientific ensemble samples.

The next authorized experiment is a 1,000,000-attempt feasibility benchmark, same seed 20260935, same constraint surface, with checkpoints every 100,000 attempts. The benchmark workflow was prepared in commit a2ec1dfdaa0f721da94230892c2c7a2428e27a21; the sampler was instrumented for acceptance/time checkpoints in commit e650ad8e849cc19b33f63fde861f485eee759cdb.

Execution status at this documentation update: prepared but not executed. No 1M result is claimed.

Do not launch the full C2 null ensemble until this benchmark establishes whether the acceptance rate remains sufficiently stable over 1M attempts. Do not change the primary constraint surface by adding joint block-pair × distance-bin preservation; that would be a separately documented stronger sensitivity null.

### Implementation integrity

The pair-level synapse aggregation boundary has been centralized in
`src/graph/connections.py` and reused by CFG, NPC and motif loaders. The
aggregation/threshold boundary is covered by a regression test. The latest Python
CI run on commit `bbd0fa1ea2b5c4ef06788808e20597bebb0483bf` completed successfully.

### Documentation rule

Every substantive experiment must record provenance, parameters, invariants,
artifact/checksum, interpretation and limitations. Failed or superseded runs are
retained in the history. New AI agents should read `docs/RESEARCH_PROTOCOL.md`
and `docs/PROJECT-MAP.md` before changing the pipeline.

### Commercialization status

Commercialization is a downstream possibility, not an established result. The
project currently has no demonstrated benchmark advantage, patentability result,
or product-market validation. The potential commercial path is based on a future
measurable technical advantage or reusable software/IP rather than on the biological
connectome itself. FlyWire's public FAFB v783 data are released under CC BY-NC 4.0,
so any commercial distribution must keep third-party data licensing separate from
our original software and algorithms.


### Gate B — 100-null NPC ensemble completed — 2026-09-27

The 100-null NPC-like ensemble has now completed successfully.

- workflow run: `36295429519`;
- source commit: `bbd0fa1ea2b5c4ef06788808e20597bebb0483bf`;
- 100/100 NPC null jobs completed successfully; no failed null job;
- aggregate job completed successfully;
- final artifact: `fafb-v783-rich-club-npc-100null`, artifact ID `10925776875`;
- 100 source null artifacts are recorded in the aggregate;
- dataset/version: FAFB v783;
- unique directed pairs: 3,732,460;
- threshold: 5 aggregated synapses per directed neuron pair;
- degree and block-preservation checks: all passed;
- descriptive rich-club criterion: `phi_norm > 1.01`;
- descriptive onset: degree 41;
- descriptive offset: degree 69;
- peak: degree 57, `phi_norm = 1.015171`;
- selected values: degree 37 = 1.008936; degree 58 = 1.015154; degree 75 = 1.006069; degree 93 = 0.993676; degree 96 = 0.990313; degree 120 = 0.975243.

Compared with the 100-null CFG ensemble, the NPC-like constraint substantially reduces the rich-club enrichment: the CFG peak was 1.057835 at degree 96, while the NPC-like peak is 1.015171 at degree 57. The descriptive >1.01 span contracts from degrees 27–120 under CFG to 41–69 under NPC. This is a matched-null comparison, not a formal significance test and not evidence by itself for a distinct biological mechanism.

The result closes the **defined NPC-like v783 Gate B benchmark**: the complete 100-null execution and all specified invariants have been validated. It does **not** close the broader biological-control question: the NPC implementation is a v783 NPC-like extension, not an exact v630 reproduction, and spatial/distance constraints remain untested.

Immediate next step: design Gate C as a genuine spatial/distance-constrained control before any computational architecture interpretation.

### Literature checkpoint — 2026-09-27

A targeted practical-literature refresh was completed while Gate B is running. New
evidence was recorded in the science ledger and design-rules document:

- A 2026 Nature brain-and-cord connectome study reports distributed, parallelized,
  embodied control modules linked by ascending/descending circuits. This is kept
  as a future scope/observable, not as an architecture specification.
- A 2026 connectome-constrained whole-brain dynamics preprint links FlyWire wiring
  to spontaneous activity through a fitted dynamical model and perturbation tests,
  reinforcing the structural-vs-functional evidence boundary.
- A 2025 peer-reviewed reservoir study provides direct computational prior art for
  using Drosophila topology and synaptic weights in task benchmarks, including
  topology/weight randomization controls.

These findings do not change the immediate order:
**complete NPC 100-null -> inspect artifact -> close defined Gate B -> design Gate C -> computational abstraction**.

The completed aggregate artifact is now the source of record for the defined Gate B benchmark.

The Gate C design/preflight artifact is now the source of record for the next biological-control stage; it contains no scientific Gate C conclusion.


## 2026-09-28 — Gate C1 Princeton feasibility CLOSED

The authoritative Princeton-based Gate C1 feasibility benchmark has now completed successfully.

- Workflow run: `36320329317`
- Commit: `ad1005f4974048957b05e8eb21697fd495816fac`
- Artifact: `10932471526`
- Artifact SHA-256: `efa3b9837ece2920e37fde31383ea0e40f4787d5d1da6da61fc897850882ea45`
- C0 source run: `36318477728`
- C0 artifact: `10931780910`
- C0 artifact SHA-256: `7265e20db3721f6b438a93227180eb0d0b8d3ad3fd9894bcbbe4a14a81dd5f36`
- 3,732,460/3,732,460 directed edges covered; node coverage 100%.
- 100,000 swap attempts produced 4,156 accepted swaps (4.156% acceptance).
- Distance-bin histogram preserved exactly.
- Edge count, in-degree and out-degree preserved exactly.
- No observed rich-club edges were dropped at thresholds 37, 75, 93 or 120.
- Distance definition: anisotropic Euclidean distance from outgoing source arbor-proxy centroid to incoming target arbor-proxy centroid, with 4/4/40 nm scaling.
- This closes the **feasibility sub-gate**, not Gate C as a whole.

The lightweight-C0 C1 run `36317314664` remains superseded. The Princeton result is now the primary C1 feasibility evidence.

A four-null spatial rich-club ensemble has been launched from the same authoritative C0 artifact (Run `36378473388`, bootstrap commit `e15e635c46bca67692abebc0e6931c6953902aa5`). It is not yet accepted as scientific evidence; each null must reach 3,732,460 swaps and pass all invariants before aggregation.


## 2026-09-28 — Gate C spatial ensemble first result validated

The first authoritative Princeton-based spatial rich-club ensemble has completed and passed the comparison audit.

- Workflow run: 36381489805
- Commit: 6eb894d6e0b0cdf8d25cf3151fb0103e4f54b403
- Aggregate artifact: 10952943175
- Aggregate SHA-256: d3749483435b6b49cd1b3594748376355fa0dcd492f4734acb9f73088d60b2f4
- Nulls: 4; seeds 20260927–20260930
- 3,732,460 directed pairs; min_synapses=5 after pair aggregation
- Degree sweep: 20–120, step 1
- All nulls reached 3,732,460 successful swaps and preserved edge count, exact in-degree, exact out-degree and the complete coarse arbor-distance-bin histogram.
- Spatial acceptance rate was about 3.37% per null.
- Descriptive >1.01 interval: degrees 51–71.
- Peak: degree 62, phi_norm = 1.0121585.

A direct artifact audit against the 100-null CFG and 100-null NPC-like aggregates found that the observed rich-club curve is identical across all three families: same 3,732,460 directed pairs, same 5-synapse threshold, same 20–120 grid, and same observed rich-node/edge/density curve. Therefore the attenuation in phi_norm is attributable to the null constraints rather than a change in the observed graph.

Current interpretation: the rich-club profile retains a small residual enrichment under this project-defined degree-preserving, coarse arbor-distance-constrained null. This does not establish a spatial mechanism, statistical significance, computational function, or architectural novelty.

Runtime record: the four-null ensemble took about 21 minutes wall-clock with four null jobs in parallel. Estimated 8-null runtime is 40–45 minutes; 16-null runtime is 80–90 minutes. These are planning estimates only.

**Next decision:** expand the spatial ensemble to 8 nulls for stability before attempting the more expensive combined NPC + spatial control. C2 should first receive a 100,000-attempt feasibility pilot; no rich-club interpretation should be taken from that pilot.

### 2026-09-28 literature refresh

A fresh literature check was completed. Salova & Kovács (Network Neuroscience, 2025) support treating topology and spatial constraints jointly rather than assuming either alone is sufficient. Lin & Murthy (Nature Methods, 2025) reinforce the structure→function bridge. Zhang et al. (Fundamental Research, 2026) provide a structure-constrained Drosophila dynamics study, while Li et al. (bioRxiv, 2026) provide a recent FlyWire-v783 whole-brain spontaneous-activity modeling preprint. These sources reinforce the project order but do not change the current Gate C decision. 


## 2026-09-28 — 8-null spatial stability run active

The planned stability expansion has been launched.

- Workflow: 36386665317
- Purpose: spatial ensemble stability only
- Seeds: 20260927–20260934
- Target: 3,732,460 successful swaps per null
- Parallelism: 4 jobs
- Timeout: 90 minutes/job
- Expected wall-clock: about 40–45 minutes
- Source C0 run: 36318477728
- The workflow was temporarily bootstrapped by push only to launch this explicit run, then immediately restored to manual-dispatch-only. No future code push will automatically launch the ensemble.

Scientific interpretation is blocked until all 8 nulls reach target and all invariants pass.


## 2026-09-28 — 8-null spatial stability validated; C2 pilot active

The 8-null spatial stability ensemble completed successfully.

- Workflow: 36386665317
- Nulls: 8; seeds 20260927–20260934
- All 8 reached 3,732,460 successful swaps
- All invariants preserved
- Descriptive >1.01 interval: degrees 51–71
- Peak: degree 62, phi_norm = 1.0120821
- 4-null comparison: peak 1.0121585 at degree 62, same 51–71 interval
- Re-aggregation of the original four null artifacts reproduces the original peak 1.0121585 exactly.

This is a stability result, not a significance test.

C2 feasibility pilot is now active:
- Run: 36393368885
- 100,000 attempted swaps
- combines NPC-like block-pair preservation with arbor-distance-bin preservation
- no rich-club curve is interpreted from this pilot
- expected runtime: usually a few minutes after the ~2.7 GB graph download; hard timeout 20 minutes.

The C2 workflow is now manual-dispatch-only after its temporary bootstrap launch.


## 2026-09-28 — C2 pilot correction and rerun

The first C2 pilot (run 36393368885) stopped before sampling because the pilot incorrectly required every accepted graph edge to have an NPC block assignment. It found 9,869 such edges. This was an implementation/coverage issue, not a scientific result.

The C2 pilot was corrected to match the existing NPC-like implementation semantics: edges whose endpoints lack a dominant outgoing-neuropil block are frozen and cannot participate in NPC-constrained swaps; centroid coverage remains mandatory and is complete.

Corrected pilot run: 36394370209
- 100,000 attempts
- seed 20260935
- authoritative C0: 36318477728
- currently running at the time of this update
- no scientific interpretation permitted until completion.

The temporary push bootstrap used to launch this corrected pilot has already been removed; the workflow is manual-dispatch-only.


## 2026-09-28 — C2 feasibility pilot completed; first kernel rejected on runtime grounds

The corrected frozen-edge C2 pilot completed successfully in Run `36396525136` after the original implementation failure. The pilot used the authoritative Princeton C0 artifact `36318477728`, FAFB v783, seed `20260935`, and 100,000 attempted swaps.

Baseline global-pair proposal result:
- accepted swaps: 1,168 / 100,000
- acceptance rate: 1.168%
- frozen edges without complete NPC block assignment: 9,869
- exact edge count, in-degree, out-degree, NPC block-pair counts, distance-bin histogram, no-self-loop and no-duplicate invariants: all passed
- artifact: `10958119130`
- artifact SHA-256: `2e840e102cfddcccc7da3baa8b051543be63fadfd0c4dafd9ca319e4e4921a0a`
- execution time of the 100k pilot step: approximately 78.1 s.

This established joint-constraint feasibility but made a full 3,732,460-successful-swap null impractical with the original proposal kernel: a stationary extrapolation is roughly 319.6 million attempts, about 69 hours per null on the observed runner rate. Therefore no full C2 null was launched.

## 2026-09-28 — C2 proposal-kernel optimization pilot

The C2 implementation was then optimized without changing the declared constraints. The proposal is now stratified by fixed source-neuropil -> target-neuropil block-pair class; distance-bin preservation remains an exact acceptance condition. This removes proposal attempts that can never satisfy the NPC block constraint while retaining the global distance-bin constraint.

Optimized pilot Run `36396805573`:
- commit: `8fd9f6ad8ca6765a5ed1d60d602ff131a86a7f1c`
- seed: `20260935`
- attempts: 100,000
- accepted swaps: 9,789
- acceptance rate: **9.789%**
- block rejections: 0
- distance-bin rejections: 86,453
- invalid/duplicate/self-loop rejections: 3,758
- 3,732,460 unique directed pairs
- 3,648 block-pair classes
- 9,869 frozen edges without complete block assignment
- all seven invariants passed
- artifact: `10958720816`
- artifact SHA-256: `9d831b88f75c919b8161608b1b603506173b57590b41f22b2fb2773dd33c6681`
- pilot step runtime: approximately 86.6 s.

The optimized kernel improves acceptance by about 8.4x versus the baseline pilot. A naive stationary extrapolation is still about 9.2 hours per full null, so **C2 is feasible as a move set but not yet operationally efficient enough for an ensemble on the current Python runner**.

### Decision

Do not launch a full C2 ensemble yet. The next engineering step is to benchmark a faster implementation of the same proposal kernel (or a rigorously equivalent exact sampler) before committing to multi-null execution. The scientific constraint set must not be weakened merely to obtain a shorter runtime.

No rich-club curve, significance claim, mechanism claim, or architectural inference is attached to either C2 pilot.

## 2026-09-28 — C2 1M benchmark dispatch failed before execution; syntax repaired

The manually dispatched 1,000,000-attempt C2 benchmark was **not scientifically executed**.

- workflow run: `36401960078`
- head commit at dispatch: `ef8dd440556470f33f7d848b24808b977527fdb3`
- C0 source run: `36318477728`
- the 65.2 MB compressed Princeton graph download succeeded;
- the authoritative C0 artifact download succeeded (artifact `10931780910`, SHA-256 `7265e20db3721f6b438a93227180eb0d8b0d3ad3fd9894bcbbe4a14a81dd5f36`);
- execution stopped at the Python parser before any C2 sampling;
- no 1M acceptance trajectory, runtime, or null result exists from this run.

The immediate cause was a literal `\\n` embedded in `run_fafb_npc_spatial_feasibility.py`. The file has now been repaired and checkpoint instrumentation is active.

CI guardrails added:
- `python -m compileall -q scripts src tests` before test execution;
- `python -m pytest --collect-only -q` before the full pytest suite;
- C2 runs perform both checks **before** downloading the large graph/C0 artifact.

A first CI run after adding the guardrail (`36406934053`) correctly caught a remaining output-string syntax defect before tests ran. The subsequent source repair is now on `main`; the next push-triggered test run must be green before treating the C2 workflow as executable.

**Next authorized C2 action:** after the current test CI passes, manually dispatch the same 1M benchmark again with `c0_run_id=36318477728` and `attempts=1000000`. Do not aggregate or interpret run `36401960078` as a scientific experiment.

**Parallel work authorized without waiting for C2:** compute FAFB structural bridge observables (neuropil participation, cross-module bridge proxies, rich-club overlap, degree-based integrator/broadcaster proxies, and arbor-distance cost) without making any RSS mechanism claim.

## Current compass

Gate A CLOSED → Gate B CLOSED → C0 CLOSED → C1 feasibility CLOSED → spatial 8-null stability VALIDATED → **C2 joint-constraint feasibility VALIDATED but runtime optimization OPEN** → C2 full ensemble only after sampler/runtime validation → stronger spatial model / structure→function → computational abstraction.


### C2 runtime refinement — latest optimized commit benchmark

The follow-up code fix `d12c4ca05310f6ab41fca94237afcd2c461c98af` removed per-attempt bucket-key lookup overhead. Run `36396814001` executed that corrected optimized kernel with the same seed and 100,000 attempts:
- accepted swaps: 9,789 (9.789%);
- all invariants passed;
- pilot step runtime: approximately **55.2 s**.

This is now the preferred runtime benchmark for the current Python proposal kernel. Simple linear extrapolation is approximately 5.85 hours (about 6 hours) per full null, still too large for the present workflow and not an acceptable reason to relax constraints. The next gate remains faster exact implementation/sampler validation.


## 2026-09-28 — C2 1M feasibility benchmark completed

The repaired C2 workflow was manually dispatched and completed successfully:

- workflow run: `36412132062`;
- run number: 13;
- commit: `ef6784d3d0c81fb5deff92b8cf0abca4f985c2bc`;
- authoritative C0 source run: `36318477728`;
- attempts: **1,000,000**;
- seed: **20260935**;
- accepted swaps: **94,751**;
- acceptance rate: **9.4751%**;
- invalid/duplicate/self-loop proposals: **38,055**;
- block rejections: **0**;
- distance-bin rejections: **867,194**;
- unique directed pairs: **3,732,460**;
- block-pair classes: **3,648**;
- eligible pair choices: **213,055,629,164**;
- frozen edges without complete block assignment: **9,869**;
- all declared invariants: **true**;
- artifact: `fafb-v783-c2-feasibility-1000000`, ID `10964334557`;
- uploaded artifact SHA-256: `59542077648956b8922746e10c585d7ed46aa554beed8ed5a44f419e5da4c15d`;
- wall-clock workflow sampling interval from the Actions log: approximately **90.86 s**.

The benchmark therefore closes the **C2 move-set feasibility/runtime calibration checkpoint**: one million proposals can now be executed successfully on the authoritative C0 graph while preserving the exact joint constraint surface.

A useful provisional throughput calculation is approximately 9.475% accepted proposals in this 1M pilot. If that rate remained constant, reaching 3,732,460 successful swaps would require about 39.4 million attempts, or roughly 1 hour of sampler time at the observed wall-clock rate. This is **only a linear feasibility estimate**; acceptance may change as the chain moves, so it is not a runtime guarantee for a full null.

The Actions log contains an internal checkpoint-timing anomaly: the emitted JSON reports a single checkpoint at 400,000 attempts with 3.86 s elapsed despite `checkpoint_every=100000`, which is inconsistent with the final wall-clock interval. Therefore checkpoint-derived throughput is not used for scientific/runtime conclusions; the 90.86 s wall-clock interval and final counts are retained as the reliable execution evidence.

**Scientific interpretation remains feasibility-only.** This run did not generate a rich-club curve, did not generate a full C2 null ensemble, and does not support a significance, mechanism, or computational-architecture claim.

**Decision:** the previous Python-runtime blocker is substantially reduced. Do not weaken the C2 constraints. The next authorized experiment is a full C2 null to the existing target of 3,732,460 successful swaps, followed by multiple independent seeds if that run reaches the target with exact invariants. The stronger spatial/max-entropy sensitivity remains downstream of this joint-control result.



## Master audit — 2026-09-28

This repository was re-audited against current GitHub state, executed workflow records, primary literature, recent connectome-computing prior art, and the project's own provenance rules. The scientific route remains coherent, but several navigation documents had stale Gate-C wording; they are now being synchronized to the C2 state.

### Verified current state
- Gate A CFG: CLOSED for the defined FAFB v783 method-aligned path.
- Gate B NPC-like: CLOSED for the defined 100-null v783 benchmark.
- C0 spatial data definition/coverage: CLOSED.
- Spatial 8-null stability: VALIDATED as an ensemble-stability observation, not a significance claim.
- C2 1M feasibility: SUCCESSFUL; exact joint invariants preserved.
- C2 full biological null: NOT YET EXECUTED; this is the current blocking artifact.
- Python test workflow run 36397212756: SUCCESS.
- C2 feasibility workflow run 36412132062: SUCCESS; artifact 10964334557.

### External prior-art constraint
A September 2026 preprint, FlyCNS, uses the Drosophila brain-and-nerve-cord connectome as a weak prior for communication allocation in embodied control under restricted communication. This materially narrows future novelty claims around connectome-informed communication/routing. A granted US patent, US12050991B1, also covers connectomics-based neural architecture search constrained by connectivity and motifs. Broad claims in either area must therefore be treated as prior art.

### Commercial route
Potential commercial value remains possible through software/tooling, architecture/IP licensing, specialized communication-constrained inference/control, or scientific infrastructure. None is currently a business result. Commercialization remains evidence-gated: measurable technical advantage, clean data/provenance rights, targeted freedom-to-operate review, and reproducible benchmarks are prerequisites.

### Discovery priority
Do not optimize the project only to confirm rich-club enrichment. Current discovery candidates are spatial-null narrow variance/constraint geometry, C2 acceptance structure, and any qualitative change in the residual under joint NPC+spatial constraints. Unexpected results remain hypotheses until independently controlled.


## 2026-09-28 — C2 full-null #1 completed

**Authoritative current C2 state: one complete full null has now been executed successfully.**

- Workflow run: `36418874492` (run #15)
- Commit: `ecac77ad658905e24990f35d1a5a34f389fe983d`
- Seed: `20260935`
- Attempts: **55,361,441**
- Accepted swaps: **3,732,460 / 3,732,460**
- Final acceptance rate: **6.7419849%**
- Target reached: **true**
- Distance-bin rejections: **49,122,517**
- Invalid/duplicate/self-loop proposals: **2,506,464**
- Block rejections: **0**
- Frozen incomplete-block edges: **9,869**
- All declared invariants: **true**
- Artifact: `fafb-v783-c2-feasibility-60000000`
- Artifact ID: `10968562956`
- Artifact ZIP SHA-256: `70549dbe9e0082e710c0b4521b7c94cc01714e842c17b787cee2cbef5b0f8093`

The run reached the full target before the 60M attempt cap. The cumulative acceptance rate declined from 9.674% at 0.4M attempts to 6.742% at completion. This is retained as a sampler/execution diagnostic only; it is not a biological or convergence claim.

**Interpretation boundary:** this artifact establishes one complete C2 null realization under the declared joint constraint surface. It does not yet establish a C2 rich-club result, statistical significance, mixing/convergence, biological mechanism, or computational advantage.

**Next authorized sequence:** artifact audit → C2 rich-club observable → non-invasive mixing diagnostics → independent C2 seeds → compare the C2 ensemble with CFG/NPC/spatial controls → stronger spatial/max-entropy sensitivity → Gate C decision.

See `docs/experiments/C2-FULL-NULL-2026-09-28.md` for the source-of-record experiment record.


## C2 runtime anomaly / checkpoint hardening — 2026-09-29

- C2 artifact-complete rerun `36523442690` was cancelled at the workflow's 180-minute self-imposed timeout; this is an execution/infrastructure event, not a scientific result.
- Audit confirmed the prior `--checkpoint-every` mechanism stored checkpoints only in memory and wrote the final artifact only after normal completion.
- Hardened C2 workflow/sampler commits now use a 350-minute workflow timeout, persist compressed resumable state (edge list, bins, counters, RNG state), validate resumed state, support optional prior checkpoint artifacts, and upload result/checkpoint artifacts with `if: always()` as best effort.
- Current status remains: C2 full-null #1 is a valid feasibility realization; Gate C remains OPEN because its artifact lacks the final graph needed for the intended C2 rich-club comparison.
- Next: verify CI → short runtime calibration → artifact-complete C2 realization → independent C2 seeds → Gate C decision.


## C2 checkpoint performance gate — 2026-09-29 (latest)

A real-scale implementation audit identified that the first resumable-checkpoint design would have imposed excessive I/O overhead: serializing the 3,732,460-edge state with default gzip level 9 was measured at approximately 26 s per checkpoint, versus approximately 2.3 s at gzip level 1.

The implementation is now hardened as follows:

- `save_c2_state()` defaults to `compresslevel=1`.
- C2 workflow checkpoint interval is `5,000,000` attempts.
- Workflow timeout remains `350` minutes.
- Resume validation still requires seed, code-version SHA-256, constraint fingerprint, edge-count/uniqueness, degree maps, distance-bin histogram, and block-pair counts to match.
- Ordinary CI passed after the checkpoint changes.
- An opt-in scale benchmark now exists for `373,246` edges under `RUN_C2_PERF_TESTS=1`; it is deliberately excluded from ordinary CI.
- The detailed record is `docs/C2-CHECKPOINT-PERFORMANCE-AUDIT-2026-09-29.md`.

**Important state correction:** the completed C2 #1 run remains a valid joint-constraint feasibility realization, but its artifact contains metadata/checkpoints rather than the final edge graph. Therefore it cannot supply the intended C2 rich-club observable. The cancelled artifact-complete rerun is not a scientific result.

**Current gate:** performance/recovery infrastructure is hardened and ordinary CI is green. The next scientific execution is an artifact-complete C2 full null using the current code, followed by rich-club extraction and non-invasive mixing diagnostics. Do not treat checkpoint-performance measurements as biological evidence.


## 2026-10-07 — C2 Run #45 artifact-complete realization

## 2026-10-07 — C2 independent-seed phase prepared

The next scientific phase is now explicitly documented as an independent C2 seed ensemble rather than a new null definition.

- experiment record: `docs/experiments/C2-INDEPENDENT-SEED-ENSEMBLE-2026-10-07.md`
- workflow seed parameterization commit: `0c8debaf121e1207ee90246b9e674f6d27b7f545`
- documentation commit for the experiment record: `191887637392710151f72f00e3ffd1bd30633c4f`
- reference seed: `20260935` (Run #45)
- planned independent seeds: `20261001`, `20261002`
- the workflow remains manual-dispatch-only; parameterizing the seed did not launch a run
- no independent-seed scientific result exists yet

The primary C2 constraint surface, proposal kernel, dataset, min_synapses, target accepted swaps, and provenance requirements are frozen for this ensemble. Any unexpected persistence, disappearance, shape shift, or reversal of the rich-club residual must be preserved and independently audited rather than selectively discarded.


Run #45 (37573133004) is the first clean artifact-complete C2 realization under the joint NPC-like + arbor-distance-bin constraint surface.

Provenance:
- job: 112636019092
- commit: 59db12b97023e4e8258b4a9948e810ac0895c66c
- seed: 20260935
- C0 source: 36318477728
- artifact ID: 11461697865
- artifact SHA-256: cb185da57f64467ecb1197f77062c510fd6f3e0c94a6c8e46689090709b9c97a

Execution:
- resumed from attempt 55,300,000 / accepted 3,728,657;
- final attempts: **55,361,441**;
- accepted swaps: **3,732,460**;
- acceptance rate: **6.7419849%**;
- target reached: **true**.

Exact invariants:
- same edge count: true;
- same in-degree: true;
- same out-degree: true;
- same source-block → target-block counts: true;
- same global distance-bin histogram: true;
- no self-loops: true;
- no duplicate edges: true;
- all invariants preserved: **true**;
- frozen edges without complete block assignment: 9,869;
- block-pair classes: 3,648.

Artifact-complete C2 rich-club observable:
- threshold range: 20–120;
- maximum phi_norm: **1.0076220771931181** at threshold **51**;
- no threshold exceeded phi_norm > 1.01;
- onset/offset above 1.01: none;
- original-edge overlap fraction: **0.47913761969317825** (~47.91%);
- null_count=1;
- interpretation remains descriptive single-null comparison, not a significance test.

Scientific reading:
The joint NPC-like + spatial C2 constraints remove the >1.01 descriptive rich-club region in this first realization and reduce the maximum normalized residual to ~0.762%. This is a potentially important structural-control signal because the earlier spatial-only null had a >1.01 descriptive region. It is **not** yet evidence of a biological mechanism, statistical significance, convergence, or a computational advantage. One C2 realization cannot characterize the constrained ensemble.

Decision:
- **C2 artifact-complete realization #1: CLOSED as an artifact/provenance milestone.**
- **C2 ensemble/mixing: OPEN.**
- **Gate C: OPEN.**
- Structure→function remains blocked until independent C2 seeds and mixing/sensitivity checks are complete.

Next authorized experiment:
Run independent C2 seeds with the **same** constraint surface, proposal kernel, dataset, and target. Prefer at least two additional seeds before Gate-C interpretation. Record the complete rich-club curve, acceptance trajectory, overlap/turnover, and non-invasive mixing diagnostics. Do not change the C2 definition to improve runtime. Treat any persistence, disappearance, shape shift, or reversal as a discovery/control signal requiring replication.


## 2026-10-07 — C2 Run #46 independent-seed replication

A second artifact-complete C2 realization was verified from GitHub Actions Run #46.

- workflow run: **37582335296**
- job: **112664615048**
- seed: **20261001**
- C0 source: **36318477728**
- artifact: **11466140681**
- artifact SHA-256: **d19aa6383818d30c4cd40d01e1cbc00db8d42af028c021052a5111d2edaec213**
- attempts: **55,237,500**
- accepted: **3,732,460 / 3,732,460**
- acceptance: **6.7571125%**
- target reached: **true**

All seven declared C2 invariants passed. Frozen edges remained 9,869 and block-pair classes remained 3,648.

The full rich-club curve has maximum phi_norm **1.0076660261640915** at threshold **50**, with **no >1.01 threshold**. Original-edge overlap is **0.47912877833921863** (~47.9129%).

Compared with Run #45 (seed 20260935), the qualitative result replicates: the >1.01 region remains absent. The maximum phi differs by only ~0.00004395 and the peak threshold shifts by one degree. This is strong replication evidence for the descriptive C2 observation, but not a significance test, mixing proof, mechanism, or computational advantage.

**Decision:** C2 artifact-complete realization #2 is closed as an artifact/provenance milestone; C2 ensemble/mixing and Gate C remain OPEN.

**Next:** run seed **20261002** with the unchanged C2 definition and no resume from another seed, then perform the planned three-seed comparison and non-invasive mixing/stability audit.


## 2026-10-07 — C2 Run #47 completes the three-seed replication set

Run #47 was independently verified as artifact-complete.

- workflow run **37617681244**; job **112779897382**
- seed **20261002**
- C0 source **36318477728**
- artifact **11481125143**
- artifact SHA-256 **4850e27dcb285dcfa258a594241bb5c843d9bf295f65d807a77c55a51c47ce64**
- attempts **55,264,717**; accepted **3,732,460**; target reached **true**
- acceptance **6.7537847%**
- max phi_norm **1.0077486180432564** at threshold **51**
- no >1.01 threshold
- overlap **0.4792729192007416**
- all seven invariants preserved; frozen edges 9,869; block-pair classes 3,648.

Together with #45 and #46, three independent C2 realizations now reproduce the same qualitative result. Maxima remain tightly clustered near 1.0077 and no realization crosses 1.01.

**Decision:** the three-seed C2 replication set is complete, but C2 ensemble/mixing remains OPEN and Gate C is not yet closed. The next step is the planned non-invasive three-seed stability/mixing audit followed by stronger spatial/max-entropy sensitivity. Structure→function remains blocked.


## 2026-10-07 — Three-seed C2 stability audit

A non-invasive audit of Runs #45–#47 compared their complete rich-club curves. Pairwise Pearson correlations are **0.9999346–0.9999503**, with maximum pointwise phi_norm difference **0.0006645**. The three maxima are **1.0076221, 1.0076660, 1.0077486**, with peak thresholds 51, 50, 51 and no >1.01 region.

Acceptance rates are also tightly clustered at 6.74198%, 6.75711%, and 6.75378%. Run #47 shows smooth late-stage acceptance decline without a computational stall.

**Decision:** the non-invasive stability/reproducibility check passes. Formal Markov-chain mixing/convergence remains unproven. Gate C remains OPEN pending the stronger spatial/max-entropy sensitivity family.
