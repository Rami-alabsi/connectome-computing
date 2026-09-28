# AI HANDOFF — Connectome Computing

Purpose: operational compass for any future AI agent. Use Current State first; verify every referenced run/artifact before accepting a result.

## 1. Current State — 2026-09-27
Stage: M5 → M6. FAFB v783 structural analysis is in the spatial-control phase.

### Gate A — CLOSED
- Defined FAFB v783 CFG benchmark; 100 nulls.
- 3,732,460 accepted directed pairs; exact edge count and in/out-degree preservation.
- phi_norm peak ≈ 1.057835 at degree 96.
- Not an exact reproduction of Lin et al. v630; defined v783 implementation.

### Gate B — CLOSED
- Defined 100-null v783 NPC-like benchmark; workflow 36295429519; artifact 10925776875.
- 100/100 nulls; exact degree and source-block→target-block preservation.
- phi_norm peak ≈ 1.015171 at degree 57; descriptive >1.01 span 41–69.
- NPC-like v783 extension, not exact v630 reproduction and not a formal significance test.

### Gate C — ACTIVE
C0 is CLOSED at data-definition/coverage level.
Authoritative input: fafb_v783_princeton_synapse_table.csv.gz (~2.7 GB compressed).
Authoritative workflow: 36315995364. Authoritative artifact: 10930278435.
- 80,215,790 synapse-table rows.
- 138,584 graph nodes; 3,732,460 unique directed pairs after pair aggregation and 5-synapse threshold.
- 0 malformed rows.
- 100% outgoing, incoming, and both-centroid graph-node coverage.
- 100,000 observed-edge and 100,000 sampled non-edge distances.
- Observed-edge median ≈ 481.001 µm; non-edge median ≈ 2.282 mm.
- Distance uses 4/4/40 nm anisotropic voxel scaling.
- Source position = mean outgoing synapse pre-site coordinates; target position = mean incoming synapse post-site coordinates.
- Synapse-derived arbor proxy, not axon length, dendrite length, or soma distance.
- C0 produces no spatial-null conclusion.

Secondary lightweight C0: synapse_coordinates.csv.gz. It produced 34,156,320 rows and 86.86% both-centroid coverage; observed-edge median ≈464.205 µm. Retain only as sensitivity/data-product comparison.

## 2. Critical provenance correction
C1 feasibility run 36317314664 / artifact 10930429115 consumed the lightweight C0 centroid artifact. Its covered-subgraph invariants are historical evidence only and it is SUPERSEDED for the primary scientific path. Do not quote its 95.78% edge coverage as the authoritative C1 result.
The C1 workflow has been redirected to consume the artifact produced by the Princeton C0 workflow. A fresh C0 run is required to materialize an unambiguous C0→C1 artifact chain.

## 3. C1 definition
Current candidate: FAFB v783 frozen-edge, hard-binned arbor-distance, degree-preserving spatial sensitivity null.
- Full graph remains 3,732,460 directed edges.
- Only covered edges are eligible for rewiring; uncovered edges remain frozen.
- Directed double-edge swap: (a,b),(c,d) → (a,d),(c,b).
- Reject self-loops, duplicate edges, and conflicts with frozen edges.
- Preserve the multiset of coarse arbor-distance bins.
- Verify full edge count, in-degree, out-degree, frozen-edge set, and distance-bin histogram.
This is a defined sensitivity/null extension, not the true spatial null, not an exact Lin et al. NND implementation, and not the Salova & Kovács model.

## 4. Required next sequence
1. Produce a fresh authoritative C0 run from the Princeton 2.7GB table.
2. Let corrected C1 automatically consume that exact C0 artifact.
3. Run full covered-edge swap feasibility before any spatial rich-club ensemble.
4. If full-target feasibility succeeds with all invariants, start with 4–8 spatial nulls.
5. Inspect runtime and stability; only then consider scaling to 16/100 if justified.
6. Compute spatial rich-club curve only after null generation is validated.
7. Compare observed vs CFG vs NPC-like vs spatial; later, if tractable, NPC + spatial.
8. Do not claim architecture or novelty from structural enrichment alone; functional/computational validation remains downstream.

## 5. Scientific labels
- OBSERVED: directly measured from FAFB.
- NULL-CONTROLLED: survives a specified null comparison.
- EXTENSION: project-defined model/control not directly reproduced from literature.
- HYPOTHESIS: interpretation to be tested.
Biology is evidence, not specification.

## 6. Key prior-art anchors
- Lin et al., Nature 2024: whole-brain Drosophila network statistics; CFG/NPC controls; arbor-aware distance based on incoming/outgoing synapse positions.
- Lin & Murthy, Nature Methods 2025: structure→function bridge.
- Salova & Kovács, Network Neuroscience 2025: combined topology + spatial constraints; supports spatial sensitivity controls, while our hard-bin swap is an extension.
- Péntek & Ercsey-Ravasz, Network Neuroscience 2025: exponential distance rule projectome model; later sensitivity, not neuron-level replacement.
- Zhang et al., Fundamental Research 2026: network structure/function modeling; downstream structure→dynamics evidence.

## 7. Implementation contracts
- Graph source: FAFB v783 connections_princeton.csv.gz.
- Shared parser: src/graph/connections.py.
- Pair aggregation happens BEFORE min_synapses=5.
- Authoritative C0 script: scripts/run_fafb_princeton_arbor_spatial_preflight.py.
- Authoritative C0 workflow: .github/workflows/m2-fafb-princeton-arbor-spatial-preflight.yml.
- C0 outputs: princeton-arbor-spatial-preflight.json and arbor-centroids.csv.gz.
- C1 script: scripts/run_fafb_spatial_swap_benchmark.py.
- C1 workflow: .github/workflows/m2-fafb-c1-spatial-benchmark.yml.
- C1 must consume the triggering C0 artifact; never substitute a stale artifact ID manually.

## 8. Historical runs
- CFG 100-null final: run 35987597540, artifact 10807064530.
- NPC 100-null final: run 36295429519, artifact 10925776875.
- Lightweight C0: run 36317178168; secondary only.
- Lightweight-C0 C1: run 36317314664, artifact 10930429115; SUPERSEDED.
- Princeton C0: run 36315995364, artifact 10930278435; authoritative C0.

## 9. Documentation rule
Whenever a gate advances, update PROJECT-STATUS.md, PROJECT-MAP.md, GATE-C-SPATIAL-DESIGN.md, science-evidence-ledger.md, and this AI-HANDOFF.md. For every accepted result record commit SHA, workflow run, artifact ID, input filenames/checksums, parameters, seed, invariants, what it does NOT prove, and next gate.

## 10. Stop conditions
Stop and document if schema changes, pair count changes unexpectedly, root-ID normalization changes, artifact provenance is ambiguous, degree/edge/frozen-edge/bin invariants fail, target swaps cannot be reached, a null definition changes materially, or literature conflicts with a novelty/mechanism claim.

## 11. One-line compass
Gate A CLOSED → Gate B CLOSED → authoritative Gate C0 CLOSED → corrected Princeton-based C1 feasibility OPEN → spatial null ensemble → cross-null comparison → functional/computational validation → architectural abstraction.

## 2026-09-28 LIVE STATE — C1 feasibility passed; ensemble running

### Gate C1 feasibility — CLOSED
Authoritative provenance chain:
- C0 Run `36318477728`
- C0 artifact `10931780910`, SHA-256 `7265e20db3721f6b438a93227180eb0d0b8d3ad3fd9894bcbbe4a14a81dd5f36`
- C1 Run `36320329317`
- C1 artifact `10932471526`, SHA-256 `efa3b9837ece2920e37fde31383ea0e40f4787d5d1da6da61fc897850882ea45`
- Commit `ad1005f4974048957b05e8eb21697fd495816fac`

C1 result:
- 3,732,460/3,732,460 edges covered; 100% node coverage.
- 4,156 accepted swaps / 100,000 attempts.
- Exact edge count, in-degree, out-degree and coarse distance-bin preservation.
- Zero rich-edge exclusions at thresholds 37, 75, 93, 120.

### Current active run
Four-null spatial rich-club ensemble: Run `36378473388`, bootstrap commit `e15e635c46bca67692abebc0e6931c6953902aa5`.
Seeds: 20260927, 20260928, 20260929, 20260930.
Each null targets 3,732,460 successful swaps and sweeps total degree 20–120.

Do not accept the ensemble until every null reaches target and all preservation invariants pass. Do not call the resulting curve mechanistic evidence. The spatial null is a project-defined hard-bin sensitivity control, not exact Lin NND and not Salova & Kovács.

### Updated compass
Gate A CLOSED → Gate B CLOSED → authoritative C0 CLOSED → C1 feasibility CLOSED → four-null spatial ensemble RUNNING → validated spatial comparison → later combined constraints / functional validation.


## 2026-09-28 LIVE STATE — spatial ensemble first result validated

The first authoritative Princeton-based spatial rich-club ensemble has completed successfully.

- Workflow: 36381489805
- Commit: 6eb894d6e0b0cdf8d25cf3151fb0103e4f54b403
- Aggregate artifact: 10952943175
- Aggregate SHA-256: d3749483435b6b49cd1b3594748376355fa0dcd492f4734acb9f73088d60b2f4
- Seeds: 20260927–20260930
- Null count: 4
- All four reached 3,732,460 successful swaps and passed all invariants.
- Spatial acceptance: about 3.37%.
- Descriptive >1.01: 51–71.
- Peak: degree 62, phi_norm 1.0121585.

Cross-null audit against CFG 100-null and NPC-like 100-null confirms the observed curve is identical across the three families. The differences are therefore null-model effects, not different observed graphs.

Do not call this a mechanism or significance result. The model is a project-defined hard-binned arbor-distance sensitivity null.

### Runtime rule

Record an estimate before every large run. Current empirical anchor:
- 4 spatial nulls: ~21 min wall-clock.
- 8 spatial nulls: estimated 40–45 min.
- 16 spatial nulls: estimated 80–90 min.
- C2 100k-attempt pilot: runtime not yet known; estimate only after implementation benchmark.

### Next sequence

1. Expand spatial ensemble from 4 to 8 nulls for stability.
2. If stable, run a 100,000-attempt C2 NPC+spatial feasibility pilot.
3. Only if C2 is computationally feasible and invariants hold, design the combined ensemble.
4. Continue literature refresh before any new scientific interpretation.

The workflow .github/workflows/m2-fafb-spatial-rich-club-4null.yml is now manual-dispatch only. The earlier push-bootstrap trigger was removed after the validated run so future code changes cannot silently launch a costly scientific ensemble.


## 2026-09-28 LIVE — 8-null stability run active

Run 36386665317 is the planned spatial stability expansion.

- Seeds: 20260927–20260934
- Target: 3,732,460 successful swaps/null
- Four-way parallelism
- Expected wall-clock: ~40–45 minutes
- Authoritative C0: run 36318477728

Do not interpret partial jobs. Accept the aggregate only if all eight nulls reach target and preserve edge count, in-degree, out-degree and distance-bin histogram.

The 8-null workflow is manual-dispatch-only in the repository after a temporary push bootstrap was removed immediately after launch.


## 2026-09-28 LIVE — Gate C stability and C2

Spatial 8-null stability is validated:
- run 36386665317
- 8/8 valid
- >1.01 = degrees 51–71
- peak degree = 62
- peak phi_norm = 1.0120821

The original 4-null aggregate was independently re-aggregated from its four null artifacts and reproduced peak degree 62 / phi_norm 1.0121585.

C2 feasibility pilot is active as run 36393368885:
- 100,000 attempts
- NPC-like block-pair + arbor-distance-bin preservation
- no rich-club interpretation

After the pilot, do not immediately launch a full C2 ensemble. First assess acceptance rate and whether the move set is sufficiently ergodic/connected for a meaningful null.


## 2026-09-28 — C2 correction live state

C2 first attempt 36393368885 was invalid as a scientific feasibility test because the implementation incorrectly required block assignments on every edge. It stopped with 9,869 edges lacking NPC blocks.

The code was corrected to freeze those edges, matching the existing NPC-like implementation semantics. Centroid coverage remains mandatory and is complete.

Corrected C2 pilot:
- run 36394370209
- 100,000 attempts
- seed 20260935
- status: running at this checkpoint

Do not interpret the failed pilot's 9,869 figure as biological evidence. It is an implementation coverage diagnostic.


## 2026-09-28 LIVE — C2 feasibility validated; runtime optimization is now the active gate

Spatial 8-null stability is validated:
- Run `36386665317`
- 8/8 nulls reached 3,732,460 successful swaps
- >1.01 interval = 51–71
- peak degree = 62
- peak phi_norm = 1.0120821
- original 4-null re-aggregation reproduces peak 62 / 1.0121585.

C2 joint NPC-like + arbor-distance feasibility has now been executed successfully.

Baseline corrected kernel:
- Run `36396525136`
- 100k attempts
- 1,168 accepted = 1.168%
- 9,869 edges frozen because complete NPC block assignment is unavailable
- all invariants passed
- artifact `10958119130`.

Optimized kernel:
- Run `36396805573`
- commit `8fd9f6ad8ca6765a5ed1d60d602ff131a86a7f1c`
- 100k attempts
- 9,789 accepted = **9.789%**
- fixed block-pair-stratified proposal; exact distance-bin acceptance
- all invariants passed
- artifact `10958720816`.

The optimized kernel is still estimated at ~8 h per full null on the current Python runner. **Do not launch the ensemble yet.** First benchmark a faster implementation of the same constraint set. Preserve the distinction between proposal-kernel optimization and null-model definition.

No C2 rich-club curve or scientific mechanism inference is allowed from the pilot.

Updated compass:
Gate A CLOSED → Gate B CLOSED → C0 CLOSED → C1 CLOSED → spatial 8-null STABLE → C2 FEASIBILITY CLOSED → **C2 RUNTIME/SAMPLER OPTIMIZATION OPEN** → C2 ensemble → stronger spatial model → structure→function → computational abstraction.
