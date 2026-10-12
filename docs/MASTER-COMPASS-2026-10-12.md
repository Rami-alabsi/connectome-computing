# MASTER COMPASS — Connectome Computing
## Operational handoff snapshot — 2026-10-12

This is the current operational source of truth. The detailed historical experiment ledger remains in `docs/PROJECT-STATUS.md`; run-specific evidence lives under `docs/experiments/`. Preserve older records; supersede them with dated notes rather than rewriting history.

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
| C2 same-chain 64E diagnostic (#55) | COMPLETE | Exact cumulative target and all seven invariants verified in workflow log |
| Formal C2 mixing / convergence | OPEN | 64E curve still drifts; no stationarity/ESS proof |
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

### A. Preserve/review Run #55 evidence before dispatch
- Recheck the merged 128E continuation protocol in PR #9 and the source artifact/checkpoint lineage.
- The artifact is identified and verified in the Actions log, but independent ZIP unpacking/re-hashing has not been done in this environment.
- Check current Actions capacity and ensure no conflicting long run is active.
- Do not claim that the artifact has been independently parsed unless that actually happens.

### B. If the checkpoint audit is accepted, run the predeclared 128E diagnostic
Protocol merged via PR #9:
- source run 38122390361; artifact `fafb-v783-c2-feasibility-5000000000` (ID 11702767144);
- seed 20261002;
- cumulative target 477,754,880 accepted swaps (128E);
- proposal-attempt cap 9,000,000,000;
- C0 source run 36318477728.
Before launch, verify resumed attempt/accepted counters and matching input/constraint fingerprints. Require all seven invariants and full curve output. Report pointwise drift, mean delta, RMSE, max absolute delta, overlap and acceptance trajectory—not correlation alone. This is a diagnostic, not a convergence certificate. Workflow dispatch is manual; do not imply it was dispatched unless verified.

### C. Keep the synthetic sensitivity ladder separate
Draft PR #7 defines +0, +1, +2, +5, +10, +50 planted-edge increments, independent synthetic base seeds, invariant checks and finite-sample reporting. It has **not** been executed and does not establish calibrated 5% testing. Do not run it concurrently with a long C2 continuation before capacity/artifact review.

### D. Then validate C3-A; no full FAFB C3 yet
C3-A is a different canonical family, provisionally p_ij = sigmoid(alpha_i + beta_j − lambda d_ij), with degree and wiring cost matched in expectation, not exact C2 constraints. Draft PR #1 contains synthetic validation work; still required are exact small-graph checks, parameter/moment recovery, support/self-loop policy, scalability audit, and external reproduction of the published Salova & Kovács k+L family on released hemibrain/Zenodo data. The published model is not the same directed equation. Full FAFB C3 is not authorized until these gates pass.

### E. Cross-family comparison remains blocked
CFG/NPC-like/spatial historical aggregate artifacts lack final edge sets/original-edge overlap. Do not infer missing overlap from acceptance rates or rounded prose. Add prospective, non-invasive turnover records to future runs and keep the CFG→NPC→spatial→C2 causal interpretation descriptive until comparable evidence exists.

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

**One-line compass:** C2's 64E run is complete, but its curve is still drifting; next is a carefully audited same-chain 128E diagnostic, then independent sensitivity/model validation, while Gate C remains open.
