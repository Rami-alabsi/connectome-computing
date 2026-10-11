# C2 Run #55 — 64E Completion and Evidence Audit (2026-10-11)

## Executive result

Run #55 completed successfully. GitHub Actions run `38122390361`, job `114419636270`, ended with conclusion `success`. The workflow reached the cumulative 64E target exactly; all seven declared C2 invariants were true in the final result log. This closes the **64E execution milestone only**. It does not establish formal Markov-chain mixing/convergence, statistical significance, mechanism, or Gate C.

- Run: https://github.com/Rami-alabsi/connectome-computing/actions/runs/38122390361
- Job: https://github.com/Rami-alabsi/connectome-computing/actions/runs/38122390361/job/114419636270
- Artifact: [fafb-v783-c2-feasibility-5000000000, ID 11702767144](https://github.com/Rami-alabsi/connectome-computing/actions/runs/38122390361/artifacts/11702767144)
- Artifact size: 46,300,016 bytes
- Uploaded ZIP SHA-256: `2febb9ec29918ca811a4139076e6caf7342d34fc664f44c8677d9511847493ac`
- Artifact retention: GitHub reports `expired=false`, 90-day retention requested by workflow.

## Exact execution facts

| Field | Verified value |
|---|---:|
| Seed | `20261002` |
| Cumulative accepted swaps | 238,877,440 |
| Target accepted swaps | 238,877,440 |
| Target reached | `true` |
| Total proposal attempts | 4,128,211,946 |
| Final cumulative acceptance rate | 5.7864625927% |
| Original-edge overlap fraction | 0.1369839195 (~13.6984%) |
| Frozen edges with incomplete block assignment | 9,869 |
| Block-pair classes | 3,648 |
| Eligible pair choices | 213,055,629,164 |
| Sampler elapsed telemetry | ~18,230.6 seconds |
| Workflow conclusion | `success` |

### Resume provenance

The process log explicitly reports:
- `resumed_from_attempt=2053048908`
- `accepted_swaps=119438720`
- `edge_list_len=3732460`, `edge_set_len=3732460`, `edge_bins_len=3732460`
- `resume_state_released=true`
- `bucket_count=3648`
- `eligible_pair_choices=213055629164`

The run therefore continued the same seed-20261002 chain from the verified 32E checkpoint. The additional accepted swaps were exactly 119,438,720, bringing the cumulative total to 238,877,440.

### Provenance fingerprints

- Code-version SHA-256: `890a73d18a8e3d4e006233b45d9dd2c5771fa849f69dc3d462ed7588af6ef076`
- Constraint fingerprint: `b330c16977c084434c129086112cf75710f95b8c39af7fd4df57ab16a87d76e3`
- Input fingerprint: `b43e3aa79c14f5338b4d0dd66ec5c0db88d68b02281facfd2a28941093072a8e`
- Seed: `20261002`
- Workflow head SHA: `2f60b9681e9e3d822f684dbfbb79a6cd7c6a7c70`

## Invariant audit

All seven declared invariants are explicitly `true` in the final JSON emitted in the Actions log:

1. Exact directed edge count preserved.
2. In-degree sequence preserved.
3. Out-degree sequence preserved.
4. Source-block → target-block counts preserved.
5. Global arbor-distance-bin histogram preserved.
6. No self-loops.
7. No duplicate directed edges.

The run reports `all_invariants_preserved=true`. This verifies the implementation's declared constraint checks for this run; it is not a proof of chain mixing.

## Observable audit

The run log reports a descriptive single-null rich-club comparison, with `null_count=1` and interpretation explicitly marked as not a significance test.

- Peak `phi_norm=1.011960367439216` at degree threshold `k=51`.
- Descriptive `phi_norm > 1.01` interval: onset `k=39`, offset `k=59`.
- Descriptive `phi_norm < 0.99` interval: onset `k=86`, offset `k=120`.
- Selected values: `k=32: 1.0083878903`; `k=50: 1.0119288540`; `k=60: 1.0096961566`; `k=100: 0.9727512261`; `k=120: 0.9572527508`.
- `scientific_conclusion=null`; the run's stated interpretation is `feasibility only; no rich-club inference`.

## Comparison with 32E Run #54

| Observable | 32E Run #54 | 64E Run #55 | Reading |
|---|---:|---:|---|
| Max `phi_norm` | 1.0117177 at k=51 | 1.0119604 at k=51 | Small upward drift (~0.000243) |
| >1.01 interval | k=42–58 | k=39–59 | Descriptive interval broadens slightly |
| <0.99 interval | k=85–120 | k=86–120 | Depletion onset shifts by one degree |
| Original-edge overlap | 16.1910% | 13.6984% | Further turnover, not a convergence proof |
| Cumulative accepted swaps | 119,438,720 | 238,877,440 | Target doubled exactly |

The overall curve remains qualitatively similar but is not numerically frozen: the peak residual increased slightly, the >1.01 interval changed, and edge overlap continued to decline. Two points on one chain are not enough to declare a plateau or non-convergence. Overlap alone is not a mixing statistic.

## Fifteen review passes recorded

These are distinct evidence checks, not fifteen experiments:

1. Confirmed run #55 status and final workflow conclusion from the Actions run endpoint.
2. Confirmed the named feasibility job completed successfully.
3. Checked all preflight, data-download, benchmark, and artifact-upload steps completed successfully.
4. Retrieved and filtered the final job log rather than relying on the run title alone.
5. Verified the cumulative accepted-swap target equals the requested 64E target.
6. Verified the final attempt count and acceptance rate in the result log.
7. Verified the resume checkpoint counters and edge-array lengths.
8. Verified seed and code-version fingerprint.
9. Verified constraint and input fingerprints.
10. Checked each of the seven invariant booleans individually.
11. Checked target-reached and aggregate invariant flags.
12. Checked artifact identity, size, upload completion, and ZIP digest.
13. Extracted the peak degree, threshold intervals, and selected `phi_norm` values.
14. Compared 32E versus 64E peak, threshold intervals, and edge overlap without calling them convergence evidence.
15. Rechecked the project compass and downstream authorization boundaries before deciding next actions.

## Current scientific decisions

- **C2 64E execution milestone:** CLOSED.
- **C2 formal mixing/convergence:** OPEN.
- **Matched-turnover comparison across CFG/NPC-like/spatial/C2 families:** PARTIAL/BLOCKED because historical edge-overlap/final-edge-set evidence is missing for earlier families.
- **Positive-control small-effect sensitivity ladder:** preregistered in draft PR #7; not executed.
- **C3-A external reproduction and scalability validation:** OPEN; full FAFB C3 is not authorized.
- **Gate C:** OPEN.
- **Structure→function, RSS/architecture claims, ablations, benchmark and scaling:** BLOCKED pending the relevant gates.

## Recommended next step

First preserve this result and compare the full 32E and 64E curves point-by-point using the archived outputs. Then decide whether to continue the same chain to a predeclared 128E target (`477,754,880` accepted swaps) as another **diagnostic**, while keeping all code, seed, data, proposal kernel, and constraints unchanged. A 128E run could characterize further drift; it cannot by itself prove convergence. Do not dispatch the synthetic sensitivity ladder concurrently until artifact auditing and available Actions capacity are checked.

## Evidence boundary

This audit is based on GitHub Actions metadata and the decoded job log. The uploaded artifact is identified by its run, artifact ID, size, and ZIP digest above. The artifact ZIP itself has not been independently downloaded and unpacked in this review, so no claim is made that its internal files were independently rehashed or parsed outside the Actions log.


## Post-run continuation-chain audit — all four checkpoints

After the initial 64E report was drafted, the complete final curves were re-extracted from the authoritative job logs for the actual target-reaching checkpoints: 8E Run #52 (not the earlier under-target Run #48), 16E Run #53, 32E Run #54, and 64E Run #55. Each curve has 101 degree thresholds. This additional audit corrects a common lineage ambiguity: **Run #48 did not reach its target** (`target_reached=false`, 29,835,212 accepted at 500,000,000 attempts); Run #52 continued the chain to the exact 8E accepted-swap target (29,859,680 at 500,418,411 attempts).

| Checkpoint | Workflow run | Accepted swaps | Attempts | Original-edge overlap | Peak `phi_norm` @ k | >1.01 interval | <0.99 interval |
|---|---:|---:|---:|---:|---:|---:|---:|
| 8E | #52 / 37772800694 | 29,859,680 | 500,418,411 | 24.8152% | 1.0106499 @ 51 | 45–56 | 84–120 |
| 16E | #53 / 37774000742 | 59,719,360 | 1,016,885,788 | 19.8354% | 1.0112045 @ 51 | 43–57 | 84–120 |
| 32E | #54 / 38112364771 | 119,438,720 | 2,053,048,908 | 16.1910% | 1.0117177 @ 51 | 42–58 | 85–120 |
| 64E | #55 / 38122390361 | 238,877,440 | 4,128,211,946 | 13.6984% | 1.0119604 @ 51 | 39–59 | 86–120 |

### Full-curve comparison (101 common thresholds)

| Comparison | Pearson correlation | Mean pointwise delta (later − earlier) | RMSE | Minimum delta | Maximum delta |
|---|---:|---:|---:|---:|---:|
| 8E → 16E | 0.9999372 | −0.00017435 | 0.00083594 | −0.00185506 | +0.00061961 |
| 16E → 32E | 0.9998992 | +0.00067267 | 0.00073861 | +0.00006573 | +0.00134651 |
| 32E → 64E | 0.9999118 | +0.00041453 | 0.00048474 | +0.00005726 | +0.00093964 |
| 8E → 64E | 0.9996261 | +0.00091285 | 0.00117322 | −0.00096571 | +0.00192696 |

The key diagnostic is not Pearson correlation alone: from 16E→32E and again from 32E→64E, **all 101 `phi_norm` values increased**. The 32E→64E mean shift is +0.00041453, and the maximum pointwise change is +0.00093964 at k=82. The curve shape is highly correlated, but the curve is still drifting systematically upward; this does not support a claim that the observable has plateaued. Edge overlap also continues to fall, but overlap is not itself a convergence statistic.

### Updated decision

- 64E execution milestone remains CLOSED.
- The full-curve comparison strengthens the reason to keep formal mixing/convergence OPEN.
- The next useful diagnostic is a predeclared 128E continuation from Run #55's exact checkpoint, target `477,754,880` cumulative accepted swaps, with identical seed/kernel/data/constraints. This should be considered only after reviewing Actions capacity and the checkpoint artifact; it is a drift diagnostic, not a convergence certificate.
- Do not run the synthetic sensitivity ladder concurrently until this C2 checkpoint audit is accepted and runner capacity is clear.
