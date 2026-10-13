# MASTER COMPASS — Connectome Computing
## Operational handoff snapshot — 2026-10-13

This is the current operational source of truth. The detailed historical experiment ledger remains in `docs/PROJECT-STATUS.md`; run-specific evidence lives under `docs/experiments/`. Preserve older records; supersede them with dated notes rather than rewriting history.

## Latest milestone — 2026-10-13: C2 same-chain 128E complete

C2 experiment Run #57 ([GitHub Actions workflow run #58 / ID 38244237906](https://github.com/Rami-alabsi/connectome-computing/actions/runs/38244237906), job 114794049385) reached **477,754,880 accepted swaps** after 8,280,080,824 attempts. All seven declared invariants are true in the result JSON. The artifact was independently downloaded and its ZIP SHA-256 matches GitHub. Full record: [C2 Run #57 completion audit](experiments/C2-RUN-57-128E-COMPLETION-AUDIT-2026-10-13.md).

Interpretation remains bounded: the 101-point curve is a **single-null descriptive feasibility result** (peak phi_norm 1.0126376258 at k=51; >1.01 over k=38–59; <0.99 over k=86–120). This does not prove significance, formal mixing/convergence, a biological mechanism, computational advantage, novelty, or commercial value. Gate C remains OPEN. Run #56's partial audit below is historical and is superseded operationally by Run #57; preserve it as provenance.

## 1. Mission and non-negotiable interpretation rule

Determine whether connectome structure contains residual organization that survives increasingly realistic null models, and only then test whether a well-defined abstraction yields a useful computational principle.

**Biology is evidence, not specification.**

Required chain: evidence → constraint → null/control → artifact verification → sensitivity → functional hypothesis → matched ablation → benchmark → scaling → prior-art recheck.

A repeated curve is not automatically convergence; an unusual result is a discovery signal, not an established discovery. No architecture, mechanism, novelty, or commercial-advantage claim is currently established.

## 2. Canonical biological data

- Dataset: FlyWire FAFB v783; authoritative Princeton synapse table.
- Main pair graph: 138,584 nodes; 3,732,460 unique directed pairs after pair aggregation and minimum 5 synapses.
- Authoritative spatial path: C0 Princeton arbor centroids; anisotropic voxel scaling 4/4/40 nm; full outgoing/incoming centroid coverage.
- C2 keeps 9,869 edges without complete dominant block assignment frozen (not deleted); all edges remain represented in the global distance-bin histogram.

## 3. Gate state as of 2026-10-12

| Workstream | State | Boundary |
|---|---|---|
| Gate A / CFG | CLOSED | Defined 100-null degree-preserving control completed |
| Gate B / NPC-like | CLOSED | Defined 100-null block-pair control completed |
| C0 / C1 | CLOSED | Authoritative spatial measurement and feasibility validated |
| Spatial 8-null | STABLE | Descriptive curve landmarks stable; not a significance claim |
| C2 independent 1E seeds #45–#47 | COMPLETE | Seven invariants passed; full curves highly correlated |
| C2 synthetic positive control | PASS | Demonstrates power for a planted synthetic signal only |
| C2 same-chain 128E diagnostic (#57) | COMPLETE | Exact cumulative target and all seven invariants verified; artifact and full curve independently inspected |
| Formal C2 mixing / convergence | OPEN | 128E curve still drifts; no stationarity/ESS proof |
| Cross-family matched-turnover audit | PARTIAL / BLOCKED | Historical CFG/NPC/spatial artifacts lack overlap/final edge sets |
| C2 smaller-effect sensitivity ladder | PLAN ONLY | Draft PR #7; not executed; do not claim power calibration |
| C3-A canonical spatial sensitivity | OPEN | Synthetic tests exist on draft PR #1; external reproduction and FAFB scalability remain open |
| Gate C | OPEN | Not closed |
| Structure→function, RSS/architecture, benchmark, scaling | BLOCKED | Intentionally downstream |
| Commercialization | RESEARCH ONLY | No validated product/IP advantage |

## 4. C2 evidence and what changed in Run #55

Primary C2 constraint surface remains frozen:
1. exact directed edge count;
2. exact in-degree sequence;
3. exact out-degree sequence;
4. exact source-block → target-block counts;
5. exact global arbor-distance-bin histogram;
6. no self-loops;
7. no duplicate directed edges.

Proposal kernel is stratified within fixed block-pair classes and checks distance-bin equality. Do not silently replace this microcanonical null with a block-pair × distance-bin ensemble; that would be a different sensitivity family.

### Independent 1E ensemble (#45–#47)
Max phi_norm: 1.0076221, 1.0076660, 1.0077486 at k≈50–51; none exceeded 1.01. Full-curve correlations were 0.9999321–0.9999503. This is reproducibility across independent starting realizations, not a formal convergence proof.

### Same-chain extended diagnostic through 64E
- Run #52 / ID 37772800694: 8E = 29,859,680 accepted; 500,418,411 attempts; overlap 24.8152%.
- Run #53 / ID 37774000742: 16E = 59,719,360 accepted; 1,016,885,788 attempts; overlap 19.8354%.
- Run #54 / ID 38112364771: 32E = 119,438,720 accepted; 2,053,048,908 attempts; overlap 16.1910%.
- Run #55 / ID 38122390361, job 114419636270: 64E = 238,877,440 accepted; 4,128,211,946 attempts; acceptance 5.7864626%; overlap 13.6984%.
- Run #55 resumed the same seed-20261002 chain from attempt 2,053,048,908 / 119,438,720 accepted swaps. Seed, code fingerprint, input fingerprint, and constraint fingerprint are recorded in `docs/experiments/C2-RUN-55-64E-COMPLETION-AUDIT-2026-10-11.md`.
- All seven declared invariants and `target_reached=true` are present in the final Actions log.
- Artifact ID 11702767144, name `fafb-v783-c2-feasibility-5000000000`, ZIP SHA-256 `2febb9ec29918ca811a4139076e6caf7342d34fc664f44c8677d9511847493ac`. It is reported as not expired. The ZIP was not independently downloaded/unpacked in the audit; claims about artifact contents are based on Actions logs and the recorded digest.

Run #55's single-null descriptive curve:
- max phi_norm = 1.0119603674 at k=51;
- phi_norm > 1.01 interval k=39–59;
- phi_norm < 0.99 interval k=86–120;
- selected: k=32 1.0083879; k=50 1.0119289; k=60 1.0096962; k=100 0.9727512; k=120 0.9572528.
- `scientific_conclusion=null`; explicitly labelled feasibility-only, not a significance test.

Full-curve comparisons use 101 shared thresholds:
- 8E→16E correlation 0.9999372; mean delta −0.00017435.
- 16E→32E correlation 0.9998992; all 101 values increased; mean delta +0.00067267.
- 32E→64E correlation 0.9999118; all 101 values increased; mean delta +0.00041453; RMSE 0.00048474.
- 8E→64E correlation 0.9996261; mean delta +0.00091285.
The shape is highly correlated, but systematic upward movement and falling overlap do not support a plateau claim. Overlap is a memory/turnover diagnostic, not a convergence statistic. One chain is not an independent ensemble.

## 5. Next actions — ordered, no shortcut

The detailed gated decision tree is maintained in `docs/POST-RUN56-PRIORITIZED-PLAN-2026-10-12.md`; use it together with this compass.

### A. Historical Run #56 (128E continuation) — PARTIAL / CANCELLED (superseded by Run #57)
As of the 2026-10-12 review, workflow Run #56 (ID `38204750622`, job `114665646123`) was cancelled short of target on commit `c06ef737a5a45d41dbfd062e54ed9f1fe9d75ab7`. Its syntax preflight, pytest collection, graph download, authoritative C0 download, and optional resume-artifact download have succeeded; the C2 sampling step was cancelled; artifact upload succeeded, but the ZIP contains only `c2-state.pkl.gz`, not the final result JSON. The job-log endpoint temporarily returned a BlobNotFound response while the job was active, so do not infer failure or progress counters from that response.

**Do not dispatch another C2 run or the sensitivity ladder concurrently.** The ZIP SHA-256 was independently verified. The saved checkpoint is at attempt 6,200,000,000 / 358,099,863 accepted; the last log probe reached 6,202,800,000 / 358,260,480 accepted. The target was not reached. Full audit: `docs/experiments/C2-RUN-56-128E-PARTIAL-AUDIT-2026-10-12.md`. The 128E protocol was merged in PR #9. Expected target is cumulative 477,754,880 accepted swaps, seed 20261002, attempts cap 9,000,000,000, source Run #55 artifact ID 11702767144, C0 source 36318477728. The checkpoint was independently parsed and basic edge-list consistency verified; the final JSON and full curve are absent, so do not claim 128E completion or independent validation of all seven invariants against the original graph.

The Run #55 artifact was subsequently downloaded and independently SHA-256 verified on 2026-10-13; its ZIP digest matches GitHub, and its result JSON was extracted and compared pointwise with 128E. See `docs/experiments/C2-128E-CURVE-DRIFT-COMPARISON-2026-10-13.md`. The full checkpoint graph state was not independently regenerated from the authoritative graph.

### B. Completion checks now satisfied by Run #57; remaining cross-family work is still open
Verify resumed attempt/accepted counters and matching input/constraint fingerprints; require all seven invariants and full curve output. Compare full curves at common thresholds and report pointwise drift, mean delta, RMSE, maximum absolute delta, overlap and acceptance trajectory—not correlation alone. This is a diagnostic, not a convergence certificate.

### C. Measure cross-family turnover before spending on another long C2 chain
CFG/NPC-like/spatial historical aggregate artifacts lack final edge sets/original-edge overlap. Do not infer missing overlap from acceptance rates or rounded prose. Add prospective edge-set and overlap accounting to future runners, with one bounded representative null per family first (CFG short; NPC-like/spatial around 20–25 minutes each, subject to available budget). Record original-edge overlap, changed-edge counts, accepted/attempted proposals, fingerprints, and invariants. Do not fabricate historical turnover. See `docs/POST-RUN56-PRIORITIZED-PLAN-2026-10-12.md` for decision rules and caveats.

### D. Redesign PR #7 before running the sensitivity ladder
Draft PR #7 is **not executed** and its small-graph +1/+2/+5/+10/+50 edge ladder does not establish 1% FAFB-scale detection power. Revise it to include 1%, 2%, and 3% effects relative to a pre-defined rich-club edge-count denominator, a matched negative/sham control, repeated independent seeds, invariant/fingerprint checks, and predeclared threshold/multiple-testing handling. Define planting as a constraint-aware intervention (for example, edge replacement under fixed edge count), not unconstrained edge addition. Report empirical detection and false-positive rates with uncertainty. Run synthetic calibration first; only consider bounded FAFB-scale calibration after Run #56 audit and compute-budget review.

### E. C3-A external reproduction before full FAFB
C3-A is a different canonical family, provisionally p_ij = sigmoid(alpha_i + beta_j − lambda d_ij), with degree and wiring cost matched in expectation, not exact C2 constraints. Keep the gate closed to full FAFB. First reproduce the published k+L spatial model on released hemibrain/Zenodo data using the paper's original undirected graph and preprocessing; record the exact data record, equations, objective, parameters and reference outputs, and ensure NumPy is declared in the reproducible environment. The published model is not the same as the project's provisional directed equation. Require small-graph checks, parameter/moment recovery where applicable, support/self-loop policy, external reproduction, and measured runtime/memory profiling before any scale-up. The rough 12-minute-per-pass FAFB estimate is not a benchmark.

### F. Methods-paper hypothesis — only after comparable evidence
A possible methodological contribution is that null-family comparisons may be confounded by unequal state-space turnover or memory of the initial edge set, and that constrained samplers should report turnover and provenance alongside structural metrics. This remains a hypothesis, not a finding or novelty claim. Require comparable prospective measurements, independent seeds, controlled synthetic graphs, and a targeted prior-art review before drafting conclusions. Seek qualified IP advice before public disclosure of any potentially protectable implementation.

### G. Low-cost parallel descriptive branch
Inventory cross-neuropil participation and inter-hemisphere edges from the authoritative graph as a separate observational branch. Document region/block mapping, missing labels, denominators and uncertainty. Do not infer function, mechanism or computational value from these counts alone, and do not launch a costly workflow that competes with Run #56.

## 6. Discovery, computation and commercial guardrails

- Unexpected curve drift, threshold movement, depletion, or narrow null variance must be retained and investigated as possible sampler, constraint, data, or scientific signals.
- `phi_norm > 1.01` and `phi_norm < 0.99` are descriptive flags, not p-values.
- C2 synthetic positive control passed: planted fixed-club edges 36→86; three nulls returned 36/41/34 while preserving the seven statistics. Synthetic power only.
- RSS/M6 remains a separate computational branch; pre-correction 6,720-row RSS results are invalid for scientific interpretation.
- No biological mechanism, new computational architecture, benchmark advantage, novelty, patentability, or commercial value has been established.
- Preserve the evidence chain: run → job/log → artifact/digest → code/data/constraint fingerprints → curve/invariants → limitations → decision.

## 7. First-read instructions for any future agent

1. Read this file.
2. Read `AI-CONTEXT.md` and the top status block in `docs/PROJECT-STATUS.md`.
3. Read the relevant run-specific record before changing code or launching work.
4. Never invent run status, results, artifacts or checks.
5. Keep C2 definition/kernel fixed; sensitivity models are separate families.
6. Do not close Gate C or unblock structure→function from curve correlation or edge overlap alone.
7. Update this compass and the experiment ledger when a gate or milestone changes.

**One-line compass:** same-chain C2 128E Run #57 completed at 477,754,880 accepted swaps; artifact ZIP and JSON were independently inspected and the ZIP hash matches GitHub; all seven declared invariants report true. The single-null curve is descriptive only and still drifts versus 64E; formal mixing/convergence and Gate C remain OPEN. The 8E–128E full-curve comparison is complete; next prioritize cross-family turnover evidence before another expensive run.

## 2026-10-13 — Independent Run #57 artifact re-audit

Re-downloaded artifact `11761653312` for workflow run `38244237906` and independently inspected the ZIP and result JSON. ZIP SHA-256 matches GitHub: `cae38791987a8f5fb7f00e380e12342d789c6f643794f2bc3c736ea9fea9b674`. Result JSON SHA-256: `4c1c9691d2c73f739a9c937c7b4775bd6b9f2112a7ddaeb31dd4ef72f946e902`; checkpoint SHA-256: `4196fdc9dfa1a92b01aad9a815a375e795360718841e3b22d14a4181047ee32a`.

Direct JSON checks: 1,669 checkpoint records, 101 rich-club thresholds, all seven declared invariants report true, target reached at 477,754,880 accepted swaps after 8,280,080,824 attempts, acceptance 5.7699302%, peak `phi_norm=1.0126376258` at k=51, descriptive >1.01 interval k=38–59, and <0.99 interval k=86–120. Saved milestone overlap declines from 12.6766% to 12.0973%; selected `phi_norm(k=50)` rises from 1.0122339 to 1.0126168 across the five milestones. This supports continued drift/turnover, not a convergence plateau.

Boundary: artifact hash and JSON were independently checked, but the checkpoint graph was not independently re-derived from the authoritative graph. The workflow's pytest step was collection-only, not a full test-suite execution. The run remains a same-chain, single-null feasibility/descriptive result. Formal mixing, significance, biological mechanism and Gate C remain OPEN.

## 2026-10-13 — Cross-family turnover code audit

A static code audit confirmed that the current CFG (`scripts/run_fafb_rich_club.py`), NPC-like (`scripts/run_fafb_npc_rich_club.py`), and spatial (`scripts/run_fafb_spatial_rich_club.py`) runners do not report observed-edge overlap or a canonical final-edge fingerprint in their result JSON. C2 already reports observed-edge overlap and input/constraint fingerprints. This confirms the instrumentation gap described by the historical aggregate-artifact audit; no missing historical overlap has been inferred.

Implementation contract and validation gates are recorded in `docs/experiments/CROSS-FAMILY-TURNOVER-INSTRUMENTATION-PLAN-2026-10-13.md`. The next authorized action is to add deterministic edge-state fingerprints and comparable overlap/turnover fields to CFG/NPC-like/spatial outputs, add synthetic unit tests, validate without changing scientific constraints, and only then dispatch bounded representative diagnostics. Do not start another long C2 chain or full C3-A run instead of this gap-closing work.

Gate C remains OPEN; formal mixing/convergence remains OPEN. Turnover is a state-memory descriptor, not a convergence statistic.