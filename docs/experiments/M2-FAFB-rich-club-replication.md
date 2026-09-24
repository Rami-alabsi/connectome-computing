# M2 — FAFB Rich-Club Replication Record

Status: CFG gate CLOSED for the defined FAFB v783 method-aligned analysis path; neuropil/spatial controls remain OPEN
Last updated: 2026-09-24

## Objective
Test whether the rich-club organization reported by Lin et al. remains observable in FAFB v783 when matching the principal methodological choices: 5-synapse threshold, total degree, directed rich-club coefficient, degree-preserving CFG null, explicit degree sweep, and ultimately a 100-null ensemble.

This is a method-aligned v783 extension, not an exact v630 reproduction.

## Reference target
Published v630 result: rich-club onset around total degree 37; preferential enrichment fades around approximately 100; 100 CFG samples used for normalization.
These are reference observations, not values to be forced onto v783.

## Benchmark command
Minimum synapses: 5.
Nulls: 2 for runtime benchmark only.
Swaps per edge: 1.0.
Thresholds: 20 through 120, step 1.

## Critical data-table rule

Codex documents that connection tables may contain multiple rows for the same neuron pair when synapses occur in multiple regions/neuropils. Therefore the 5-synapse connection threshold must be applied to the **sum of synapses across all rows for the same directed neuron pair**, not independently to each row. The runner now aggregates pair-level synapse counts before thresholding. This rule is tested in `tests/test_fafb_rich_club.py`.

## Acceptance criteria
- input and five-synapse filtering verified;
- unique directed pairs verified;
- edge count, in-degree and out-degree preserved for every null;
- no self-loops or duplicate directed pairs;
- total-degree definition verified;
- Phi(d) verified;
- threshold 37 explicitly included;
- complete 20–120 curve inspected;
- runtime benchmark measured;
- 100-null final CFG run completed, or limitation documented;
- final artifact and provenance inspected;
- interpretation written only after artifact inspection.

## Final 100-null CFG ensemble — 2026-09-24

Run `35987597540` completed successfully on commit `f53f471de27f0c8cf58d496dcc0885ecfa6a8d4a`.

Artifact: `fafb-v783-rich-club-100null` (ID `10807064530`), SHA-256 `5343abb81fe1cb1a19692e72c5b326fbed87814e99c1476a5bb303164954fae6`.

Parameters: FAFB v783; pair-level synapse aggregation; minimum 5 synapses per directed pair; 100 independent deterministic CFG nulls; 3,732,460 successful swaps targeted per null; total-degree sweep 20–120.

Validation: all 100 nulls reached the requested swap target and preserved edge count, in-degree and out-degree exactly. The observed `phi_norm > 1.01` interval is continuous from degree 27 through degree 120 in the tested sweep. Selected values are 1.015363 at degree 37, 1.047329 at degree 75, 1.056247 at degree 93, 1.057835 at degree 96 (peak), and 1.041215 at degree 120.

Interpretation: this is a stable CFG-controlled rich-club enrichment pattern under the repository-defined FAFB v783 method. It is a **method-aligned replication/extension**, not an exact reproduction of Lin et al. because the published analysis used v630 and the repository implementation does not reproduce every detail of the paper's null construction. The next tests are therefore the neuropil-constrained/NPC-like and spatial/distance-constrained controls.

## Run history

- **35962189226 — FAILED:** workflow syntax error; `/usr/bin/time` attempted to execute `PYTHONPATH=.` as a binary. No scientific computation ran.
- **35962219553 — SUPERSEDED:** corrected benchmark workflow from the pre-aggregation implementation. Do not use as scientific evidence.
- **35962522090 — SUCCESS:** first successful real-data publication-aligned v783 rich-club benchmark on commit `9138d7280b4ca5219ed2f56560569751a6aafe99`. Artifact `fafb-v783-rich-club-publication-benchmark`, ID `10792907968`.
- **Current combined anchor — Run 35984738032 — SUCCESS:** completed successfully on commit `285f7746c123f50f35558bb84718ef78dfa0b756`. All profile, reciprocity, spatial, rich-club, motif, and artifact-upload steps succeeded. Artifact `fafb-v783-real-data-anchor`, ID `10802343443`, SHA-256 `41f65e07f11cd0445db2339598a722a8ea2db06f24e08faee26f8c2f3755f2b6`.

### Scientific gate status

**Gate A is CLOSED for the defined CFG/rich-club method-aligned path.**

The 100-null ensemble provides the required null count for this project protocol, and all nulls reached the requested swap target with exact edge-count/in-degree/out-degree preservation. The result is therefore sufficient to close the defined CFG gate. It does not close the broader biological control hierarchy: the paper's NPC comparison is a separate control, and the project must still test neuropil-constrained and spatial/distance-constrained explanations.

The combined real-data anchor is operationally complete; its profile, reciprocity, spatial inventory, rich-club and conditional triad artifacts remain useful as baseline evidence.

## Gate B — NPC-like control preparation

The repository already contains an NPC-constrained implementation in `scripts/run_fafb_npc_rich_club.py`. An audit against the published Methods confirms the key construction: each neuron is assigned to one of the neuropil blocks using the neuropil with the most outgoing synapses, while degree sequences and inter-/intra-block edge counts are preserved during rewiring. This is the published NPC construction at the model-definition level, but the project implementation remains an **NPC-like v783 extension**, not an exact reproduction of the paper's v630 dataset/software snapshot. citeturn3search3

The benchmark has now been aligned to the same explicit total-degree sweep used for the CFG gate: degrees 20–120, step 1. The workflow currently uses 8 nulls as an execution/implementation benchmark. No NPC scientific conclusion is recorded until the artifact is inspected for complete swap realization, exact degree preservation, exact block-pair preservation, and the resulting rich-club curve.

The connection-table `neuropil` field is a synapse-location field. This does not conflict with the published NPC definition because the NPC neuron block is assigned from the neuropil receiving the neuron's outgoing synapses, rather than by soma location. citeturn3search0turn3search2

## Expected artifact
artifacts/fafb-v783/rich-club.json

## Interpretation categories
Consistent with published regime: v783 shows a comparable qualitative pattern after matching the major method choices.
Different from published regime: v783 materially differs.
Inconclusive: implementation, dataset, or null-ensemble limitations prevent a conclusion.

No outcome should be described as a failure of the project.
## Real-data benchmark execution — 2026-09-24

Run 35962522090 completed successfully on commit 9138d7280b4ca5219ed2f56560569751a6aafe99.

Artifact:
- name: fafb-v783-rich-club-publication-benchmark
- artifact ID: 10792907968
- SHA-256: 3054b154f18dfd6bae821d084bbd159f1c1d2d5ee13dd90e1ab7b65bd297aea1

Execution parameters:
- FAFB v783;
- pair-level synapse aggregation before thresholding;
- minimum synapses = 5;
- nulls = 2;
- target swaps per null = 3,732,460;
- total-degree sweep = 20–120, step 1.

Measured graph:
- unique directed pairs = 3,732,460.

Null integrity:
- null 0: edge count preserved; in-degree preserved; out-degree preserved.
- null 1: edge count preserved; in-degree preserved; out-degree preserved.

Runtime:
- wall time = 16:11.20;
- maximum resident set size = 1,900,488 kB.

Preliminary curve observation:
- first phi_norm > 1.01 occurs at degree 27;
- degree 37: phi_norm = 1.0152909340573695;
- degree 75: phi_norm = 1.04715818882749;
- peak in the 20–120 sweep: degree 97, phi_norm = 1.0581033995668143;
- phi_norm > 1.01 remains true at degree 120 (1.0420106013590444), so the current descriptive offset is beyond the tested range.

Interpretation status:

Benchmark evidence only. This establishes that the real v783 rich-club path executes successfully and that the observed curve is enriched relative to the two generated degree-preserving nulls. It does not yet establish publication replication because the paper used 100 CFG samples and v630, while this run used v783 and 2 nulls.

The measured runtime suggests approximately 13.5 hours for 100 nulls under naive linear scaling. This is only a planning estimate; actual scaling must be measured. Before the 100-null run, record realized successful swaps and failed attempts so the null-randomization quality is auditable.

The result also does not close the broader FAFB biological gate. Reciprocity, motif, spatial/contact and complete profile artifacts still require real-data execution.

## Combined real-data anchor inspection — Run 35984738032

The end-to-end FAFB v783 anchor completed successfully.

### Profile
- nodes in connection table: 138,584
- unique directed pairs: 3,732,460
- maximum in-degree: 6,261
- maximum out-degree: 6,523
- mean in/out degree in the degree-profile summary: 26.9328
- weighted synapse total: 50,666,648
- degree semantics: unique directed neuron pairs after pair-level deduplication

### Reciprocity
- reciprocal directed edge count: 620,180
- nodes with reciprocal edges: 102,757
- reciprocity probability: 0.1661585121

### Spatial / neuropil inventory
- raw rows: 5,342,446
- unique directed pairs: 3,732,460
- unique pairs represented in multiple regional rows: 1,002,488
- multi-region pair fraction: 0.2685864015
- neuropil labels observed: 79
- status: descriptive inventory only; no spatially constrained null is claimed

### Rich-club
Both 2 CFG nulls reached the full target:
- target/requested swaps per null: 3,732,460
- null 0: 3,764,742 attempts; 3,732,460 successful
- null 1: 3,764,495 attempts; 3,732,460 successful
- both nulls preserved edge count, in-degree and out-degree exactly

For the 20–120 sweep:
- degree 27: phi_norm ≈ 1.010002
- degree 37: phi_norm ≈ 1.015287
- degree 75: phi_norm ≈ 1.047477
- peak: degree 96, phi_norm ≈ 1.057996
- degree 120: phi_norm ≈ 1.041405
- descriptive criterion phi_norm > 1.01: first at 27 and still true at 120

This is still a **2-null benchmark observation**, not the final 100-null publication-aligned result.

### Directed triad sample
The sampler attempted 1,000,000 wedge samples:
- observed accepted: 981,356
- null 0 accepted: 981,162
- null 1 accepted: 981,539
- both nulls preserved edge count and directed in/out-degree exactly

Important interpretation constraint: the sampler selects a node with at least two outgoing neighbors and samples two of those neighbors. Therefore this artifact is a **conditional directed triad-signature profile**, not an unrestricted triad census. Its signature definition explicitly documents this as a transparent six-bit signature rather than a general isomorphism-class census.

### Gate decision
**Gate A is CLOSED for the defined CFG/rich-club method-aligned path.**

The combined anchor demonstrates that the real-data execution chain is operational and that the current CFG randomizer reaches its requested swap target with high realization efficiency. It does not replace the required 100-null CFG ensemble. The 100-null decision/run is now complete; provenance and validation are recorded above. The next controlled step is the neuropil-constrained/NPC-like null, followed by a spatial/distance-constrained null if the data support it.
