# C2 128E Continuation Protocol — 2026-10-11

## Purpose

Define the next same-chain diagnostic after C2 Run #55 reached cumulative 64E. The full-curve audit shows continuing aggregate drift, so another milestone is useful; it is not a convergence test and must not be presented as one.

## Frozen chain and target

- Source run: [Run #55, ID 38122390361](https://github.com/Rami-alabsi/connectome-computing/actions/runs/38122390361)
- Resume artifact name: `fafb-v783-c2-feasibility-5000000000`
- Resume artifact ID: `11702767144`
- Seed: `20261002`
- Current cumulative target: `238877440` accepted swaps (64E)
- Next cumulative target: **`477754880` accepted swaps (128E)**
- Additional accepted swaps required from the 64E result: `238877440`
- C0 source run ID: `36318477728`
- Expected unchanged constraint fingerprint: `b330c16977c084434c129086112cf75710f95b8c39af7fd4df57ab16a87d76e3`
- Expected unchanged input fingerprint: `b43e3aa79c14f5338b4d0dd66ec5c0db88d68b02281facfd2a28941093072a8e`
- Expected unchanged sampler code fingerprint: `890a73d18a8e3d4e006233b45d9dd2c5771fa849f69dc3d462ed7588af6ef076`

## Manual workflow-dispatch inputs

Use the existing workflow [FAFB v783 C2 NPC-spatial feasibility benchmark](https://github.com/Rami-alabsi/connectome-computing/actions/workflows/m2-fafb-c2-feasibility.yml). The following are the exact proposed inputs; this protocol does **not** claim the workflow has been dispatched.

| Input | Value |
|---|---|
| `c0_run_id` | `36318477728` |
| `seed` | `20261002` |
| `attempts` | `9000000000` |
| `target_accepted` | `477754880` |
| `resume_run_id` | `38122390361` |
| `resume_artifact_name` | `fafb-v783-c2-feasibility-5000000000` |
| `trace_attempts` | `0` |
| `skip_finalization` | `false` |
| `mixing_milestones` | `477754880` |

The attempt cap is deliberately above the estimated cumulative requirement; it is not an ETA guarantee. The workflow timeout remains 350 minutes. The previous 64E continuation took about five hours of sampler time and cumulative acceptance has declined slowly. If the run times out before the target, treat it as an incomplete execution, retain its artifact/checkpoint if uploaded, and resume from that verified checkpoint; do not relabel it as a completed 128E result.

## Mandatory preflight and stop conditions

Before interpreting progress, inspect the new run log and verify:
1. The resume artifact download succeeded and a `c2-state.pkl.gz` file was found.
2. The logged resume seed is `20261002`.
3. Resume counters are consistent with the source checkpoint. Record the exact `resumed_from_attempt` and `accepted_swaps`; do not assume the artifact checkpoint is identical to the final summary without checking.
4. `edge_list_len`, `edge_set_len`, and `edge_bins_len` are each `3732460`.
5. `bucket_count=3648`, and constraint/input fingerprints match the frozen values above.
6. The seven C2 invariants are all true at completion.
7. `target_reached=true` and cumulative accepted swaps equal `477754880`.
8. The result and checkpoint artifacts upload successfully; record artifact ID, size, and ZIP digest.
9. Extract the full 101-point `phi_norm` curve and compare it with 8E/16E/32E/64E using the same thresholds and formulas.
10. Record original-edge overlap as turnover diagnostics only; do not use it as proof of mixing.

If the seed, input fingerprint, constraint fingerprint, kernel, graph definition, or any of the seven invariants differ, stop the comparison and investigate before scientific interpretation. Do not relax the constraints or change the proposal kernel to meet the target.

## Predeclared comparisons

Primary descriptive comparison: 64E versus 128E, across all 101 common degree thresholds. Report:
- Pearson curve correlation **and** mean, RMSE, minimum, maximum, and maximum absolute pointwise delta (128E minus 64E);
- peak `phi_norm` and its threshold;
- intervals above 1.01 and below 0.99;
- original-edge overlap;
- attempts, acceptance rate, wall time, memory diagnostics, and exact resume counters.

A high correlation alone is not a plateau. A further uniform shift, continued threshold-boundary movement, or changing depletion profile is evidence of ongoing observable drift. Even a numerically small change over one additional milestone does not by itself prove Markov-chain convergence; formal mixing requires a defensible diagnostic strategy and more than one scalar summary.

## Decision boundary

- C2 64E execution: complete.
- C2 128E execution: **not dispatched / not yet run**.
- Formal mixing/convergence: OPEN.
- Matched-turnover cross-family audit: PARTIAL/BLOCKED.
- Gate C: OPEN.
- C3-A external reproduction/scalability: OPEN.
- Structure→function, RSS/architecture claims, ablations, benchmark, and scaling: BLOCKED.

The small-effect synthetic sensitivity ladder remains a separate preregistered task and should not be run concurrently until Actions capacity and the C2 continuation outcome are reviewed.


## Outcome update — 2026-10-12

The planned continuation was dispatched and completed as [Run #58, ID 38244237906](https://github.com/Rami-alabsi/connectome-computing/actions/runs/38244237906), job [114794049385](https://github.com/Rami-alabsi/connectome-computing/actions/runs/38244237906/job/114794049385). It reached **477,754,880 accepted swaps (128E)** at **8,280,080,824 attempts**; all seven invariants passed and `target_reached=true`. Artifact ID **11761653312**, ZIP SHA-256 `cae38791987a8f5fb7f00e380e12342d789c6f643794f2bc3c736ea9fea9b674`.

The full-curve comparison with 64E shows Pearson r=**0.9999298210**, mean delta=**+0.0001459177**, RMSE=**0.0002613567**, peak rising from **1.0119603674** to **1.0126376258** at k=51, and the `>1.01` interval expanding from k=39–59 to k=38–59. This is high correlation with continued observable drift, not a demonstrated plateau or convergence proof. The result still states `scientific_conclusion=null` and `feasibility only; no rich-club inference`.

The current outcome and limitations supersede the protocol's earlier “not dispatched / not yet run” status snapshot. See [Run #58 completion audit](C2-RUN-58-128E-COMPLETION-AUDIT-2026-10-12.md). Formal mixing/convergence and Gate C remain OPEN; structure→function remains BLOCKED.
