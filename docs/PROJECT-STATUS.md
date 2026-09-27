# Project Status

## Current position

**Stage: M5 → M6 — FAFB CFG and defined NPC-like gates closed; Gate C spatial control preflight active**

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

### Current gate state

- Gate A — FAFB v783 CFG/rich-club: **CLOSED** for the defined method-aligned path.
- Gate B — FAFB v783 NPC-like/neuropil-constrained rich-club: **CLOSED** for the defined 100-null v783 benchmark; broader biological control remains open.
- Gate C — spatial/distance-constrained null: **OPEN; not started**.
- Computational architecture interpretation remains downstream of the biological
  control hierarchy.

### Current Gate C execution

Gate B is closed for the defined 100-null v783 NPC-like benchmark. The complete
artifact was retrieved and inspected; the broader biological-control question
remains open because the implementation is an NPC-like v783 extension.

Gate C is now in design/preflight:
- coordinate source: FAFB v783 `coordinates.csv.gz`;
- primary first-pass distance: anisotropic Euclidean node-position distance;
- first preflight: `scripts/run_fafb_spatial_preflight.py`;
- workflow: `.github/workflows/m2-fafb-spatial-preflight.yml`;
- no Gate C scientific result exists yet.

The preflight must be completed before any spatial randomization. It records
coordinate checksum/schema, node coverage, voxel scaling, sampled edge/non-edge
distances, and the declared null hierarchy.

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
