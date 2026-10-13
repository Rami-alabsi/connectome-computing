# C2 Run #58 — 128E Continuation Completion and Evidence Audit (2026-10-12)

## Executive result

GitHub Actions workflow run **#58** completed successfully and reached the predeclared cumulative **128E** accepted-swap target on the existing seed-20261002 C2 chain. This closes the **128E execution milestone only**. It does **not** close formal Markov-chain mixing/convergence, Gate C, or authorize structure→function work.

- Workflow: [Run #58 / 38244237906](https://github.com/Rami-alabsi/connectome-computing/actions/runs/38244237906)
- Job: [feasibility / 114794049385](https://github.com/Rami-alabsi/connectome-computing/actions/runs/38244237906/job/114794049385)
- Workflow: `FAFB v783 C2 NPC-spatial feasibility benchmark`
- Workflow conclusion: `success`
- Branch: `main`
- Workflow head SHA: `07e362e476c3f1a15b51e9c60013eb46804849a4`
- Seed: `20261002`
- C0 source run: `36318477728`

## Artifact identity and integrity

- Artifact name: `fafb-v783-c2-feasibility-9000000000`
- Artifact ID: `11761653312`
- Artifact size: **46,379,353 bytes**
- GitHub artifact ZIP SHA-256 (GitHub digest and locally computed digest agree): `cae38791987a8f5fb7f00e380e12342d789c6f643794f2bc3c736ea9fea9b674`
- Retention expiry reported by GitHub: **2027-01-10T11:41:07Z**; `expired=false` at audit time.
- ZIP members: `c2-feasibility-9000000000.json` (585,564 bytes) and `c2-state.pkl.gz` (46,276,494 bytes).
- Extracted result JSON SHA-256: `4c1c9691d2c73f739a9c937c7b4775bd6b9f2112a7ddaeb31dd4ef72f946e902`.

The result JSON was extracted and parsed independently from the uploaded ZIP; its 101-point curve and summary were checked against the final job log.

## Resume provenance and frozen definitions

The job log confirms:
- `resumed_from_attempt=6200000000`
- accepted swaps at resume: **358,099,863**
- `resume_state_released=true`
- `edge_list_len=edge_set_len=edge_bins_len=3,732,460`
- `bucket_count=3,648`
- `eligible_pair_choices=213,055,629,164`
- sampler entered the loop at attempt 6,200,000,000; current RSS was about 2,032 MiB and reported max RSS about 2,800 MiB.

Fingerprint checks match the frozen 64E protocol:
- Sampler code-version SHA-256: `890a73d18a8e3d4e006233b45d9dd2c5771fa849f69dc3d462ed7588af6ef076`
- Constraint fingerprint: `b330c16977c084434c129086112cf75710f95b8c39af7fd4df57ab16a87d76e3`
- Input fingerprint: `b43e3aa79c14f5338b4d0dd66ec5c0db88d68b02281facfd2a28941093072a8e`

The C2 definition and proposal kernel were not changed: block-pair-stratified degree-preserving swaps with exact global arbor-distance-bin acceptance; seed 20261002; minimum synapse threshold 5.

## Exact completion facts

| Field | Verified value |
|---|---:|
| Cumulative target | 477,754,880 accepted swaps (128E) |
| Final accepted swaps | 477,754,880 |
| Target reached | `true` |
| Total proposal attempts | 8,280,080,824 |
| Final acceptance rate | 5.7699301511% |
| Sampler elapsed telemetry | 20,064.41 seconds (~5.57 hours) |
| Unique directed pairs | 3,732,460 |
| Block-pair classes | 3,648 |
| Frozen edges without complete dominant-block assignment | 9,869 |
| Eligible pair choices | 213,055,629,164 |
| Original-edge overlap | 0.1209730312 (~12.0973%) |
| `scientific_conclusion` | `null` |
| Stated interpretation | `feasibility only; no rich-club inference` |

All seven declared invariants are true in the final JSON:
1. exact edge count preserved;
2. in-degree sequence preserved;
3. out-degree sequence preserved;
4. source-block → target-block counts preserved;
5. global distance-bin histogram preserved;
6. no self-loops;
7. no duplicate directed edges.

The aggregate flag `all_invariants_preserved=true` and `target_reached=true` are both present. These are implementation checks for this realization, not proof of chain mixing.

## Full rich-club curve audit

The extracted result contains **101 thresholds (k=20–120)**.

- Peak: **`phi_norm=1.0126376257614715` at k=51**.
- Descriptive `phi_norm > 1.01` interval: **k=38–59** (22 thresholds).
- Descriptive `phi_norm < 0.99` interval: **k=86–120** (35 thresholds).
- Selected final values: k=32: 1.0084475991; k=50: 1.0126167629; k=60: 1.0099717269; k=100: 0.9730095234; k=120: 0.9578061264.
- `null_count=1`; the result explicitly says this is a descriptive single-null comparison, not a significance test.

## Direct comparison with Run #55 / 64E

The 64E JSON was re-downloaded from artifact 11702767144 and its full curve compared pointwise with this 128E JSON, using all 101 matching thresholds.

| Observable | 64E / Run #55 | 128E / Run #58 | Difference / reading |
|---|---:|---:|---|
| Cumulative accepted swaps | 238,877,440 | 477,754,880 | Target doubled |
| Attempts | 4,128,211,946 | 8,280,080,824 | More than doubled |
| Acceptance rate | 5.7864625926% | 5.7699301511% | Small decline |
| Peak `phi_norm` | 1.0119603674 at k=51 | 1.0126376258 at k=51 | Increase of 0.0006772583 |
| `>1.01` interval | k=39–59 | k=38–59 | Onset extends one degree lower |
| `<0.99` interval | k=86–120 | k=86–120 | Same interval |
| Original-edge overlap | 13.69839195% | 12.09730312% | Decline of 1.6011 percentage points |

Full-curve metrics for 128E minus 64E:
- Pearson correlation: **0.9999298210**.
- Mean pointwise delta: **+0.0001459177**.
- Mean absolute delta: **0.0001913622**.
- RMSE: **0.0002613567**.
- Minimum delta: **−0.0003043290**.
- Maximum delta / maximum absolute delta: **+0.0006879088**, at **k=50**.
- 71 of 101 thresholds increased; 30 decreased.

### Interpretation boundary

The curve correlation is extremely high, but the peak increased, the `>1.01` onset moved, and most pointwise values increased. Therefore this is **not a demonstrated plateau**. The result supports continuing observable drift along this same chain; it neither proves nor disproves formal mixing/convergence. Original-edge overlap is a turnover descriptor, not a mixing statistic. Since this is one continued chain and one null realization, the curve is not a p-value, ensemble estimate, biological mechanism, or computational advantage claim.

The run's own `scientific_conclusion=null` and `feasibility only; no rich-club inference` must be preserved in any downstream summary.

## Workflow / preflight audit

The following workflow steps all completed successfully: checkout, Python setup, syntax preflight, pytest collection preflight, graph download, authoritative C0 artifact download, optional C2 resume checkpoint download, C2 feasibility benchmark, and upload of the result plus latest checkpoint.

Important limitation: the workflow performed **pytest collection preflight**, not a full `pytest` test execution in this job. Do not report this run as having executed the full test suite. Non-blocking Node.js deprecation warnings were emitted by GitHub Actions dependencies.

## Current decision and next steps

- **128E same-chain execution:** CLOSED.
- **C2 artifact and provenance milestone at 128E:** CLOSED for this run.
- **C2 formal mixing/convergence:** OPEN.
- **Matched-turnover cross-family audit:** PARTIAL/BLOCKED.
- **C3-A validation / spatial-max-entropy sensitivity:** OPEN; this run does not replace it.
- **Gate C:** OPEN.
- **Structure→function, matched ablations, RSS/architecture claims, benchmarks, scaling, and commercialization claims:** BLOCKED pending the biological-control and validation gates.

Next:
1. Preserve the 128E JSON and checkpoint artifact; no new same-chain extension should be dispatched automatically just because 128E finished.
2. Update the continuation-chain comparison record with this full-curve comparison.
3. Continue with the documented C3-A/prior-art-aligned design and synthetic validation gate, after reviewing Actions capacity. Keep C2's primary definition frozen.
4. Design defensible mixing diagnostics; do not infer convergence from curve correlation, edge overlap, or accepted-swap count alone.
5. Re-open the 128E protocol only if a specific predeclared question justifies another same-chain milestone. Any continuation is a drift diagnostic, not a convergence certificate.
