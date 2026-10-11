# C2 extended-chain diagnostic — 32E result (2026-10-11)

## Decision summary

**Run #54 completed successfully at the predeclared 32E accepted-swap target.** The checkpoint resume, target completion, final artifact upload, and all declared C2 invariant checks are confirmed in the GitHub Actions log. The result supports continued microscopic turnover and modest movement in the descriptive rich-club curve through 32E. It does **not** establish stationarity, ergodicity, adequate burn-in, effective sample size, formal convergence, statistical significance, or a biological mechanism. Gate C remains **OPEN**.

## Provenance

- Repository: `Rami-alabsi/connectome-computing`
- Workflow run number: **#54**
- Actual GitHub run ID: **38112364771**
- Job ID: **114390401018**
- Run URL: https://github.com/Rami-alabsi/connectome-computing/actions/runs/38112364771
- Artifact name: `fafb-v783-c2-feasibility-2500000000`
- Artifact ID: **11695105557**
- Artifact URL: https://github.com/Rami-alabsi/connectome-computing/actions/runs/38112364771/artifacts/11695105557
- Artifact ZIP SHA-256: `c297deadd7caa74fcda4c42498a2a1d4184b66ff335b0ed38326c7ab88a3f330`
- Code version: `890a73d18a8e3d4e006233b45d9dd2c5771fa849f69dc3d462ed7588af6ef076`
- Input fingerprint: `b43e3aa79c14f5338b4d0dd66ec5c0db88d68b02281facfd2a28941093072a8e`
- Constraint fingerprint: `b330c16977c084434c129086112cf75710f95b8c39af7fd4df57ab16a87d76e3`
- Seed: `20261002`
- Data: FAFB v783; 3,732,460 unique directed pairs.

## Resume verification

The log confirms that Run #54 downloaded artifact **11552145132** from Run #53 and resumed from **1,016,885,788 proposal attempts / 59,719,360 accepted swaps (16E)**. The final target was **119,438,720 accepted swaps (32E)**. The run reached that target and uploaded its result plus resumable checkpoint.

The resume source's actual workflow run ID was **37774000742** (displayed as Run #53), not the display number alone.

## Final execution metrics

| Metric | Run #54 result |
|---|---:|
| Target accepted swaps | 119,438,720 |
| Actual accepted swaps | 119,438,720 |
| Proposal attempts | 2,053,048,908 |
| Final acceptance rate | 5.8176266% |
| Original-edge overlap fraction | 0.1619103755 (16.1910%) |
| Unique directed pairs | 3,732,460 |
| All declared invariants preserved | `true` |
| Target reached | `true` |
| Scientific conclusion field | `null` |
| Interpretation emitted by runner | Feasibility only; no rich-club inference |

The seven C2 invariants remain the frozen constraint surface: exact directed edge count, exact in-degree sequence, exact out-degree sequence, exact source-block→target-block counts, exact global arbor-distance-bin histogram, no self-loops, and no duplicate directed edges. This run did not change the C2 proposal/acceptance kernel or constraint fingerprint.

## Rich-club descriptive observables at 32E

| Total-degree threshold k | `phi_norm` |
|---:|---:|
| 32 | 1.0081645 |
| 50 | 1.0117064 |
| 60 | 1.0095789 |
| 100 | 0.9724246 |
| 120 | 0.9569453 |

- Maximum `phi_norm`: **1.0117177 at k=51**.
- Runner-reported descriptive `>1.01` onset/offset: **k=42 / k=58**.
- Runner-reported `<0.99` depletion onset/offset: **k=85 / k=120**.
- These cutoffs are descriptive flags only, not statistical significance thresholds.

## Comparison with earlier milestones

| Observable | 8E (Run #48 continuation) | 16E (Run #53) | 32E (Run #54) |
|---|---:|---:|---:|
| Accepted swaps | 29,859,680 | 59,719,360 | 119,438,720 |
| Acceptance rate | 5.9669427% | 5.8727697% | 5.8176266% |
| Original-edge overlap | 24.8152% | 19.8354% | 16.1910% |
| `phi_norm` at k=50 | 1.01061* | 1.0111500 | 1.0117064 |
| `phi_norm` at k=120 | 0.9582185 | 0.9563634 | 0.9569453 |

`* `The 8E value is the previously recorded rounded milestone value; consult its original artifact for full precision.

Interpretation:
1. Original-edge overlap continues to fall, showing substantial turnover relative to the original graph. Overlap is a memory/turnover diagnostic, **not** a convergence test.
2. The intermediate-degree positive residual around k≈50 is above the descriptive 1.01 flag at 16E and 32E, and its value changes modestly between those milestones.
3. The high-degree depletion tail remains visible. The selected k=120 value moved slightly upward from 16E to 32E, so do not describe the entire curve as monotonically drifting in one direction.
4. Two late milestones do not establish a plateau. A similar-looking aggregate curve can coexist with continued movement in the underlying graph; conversely, turnover alone does not prove non-convergence.

## Scientific boundary

This is one continued chain from seed `20261002`, not an independent null ensemble. It is not a p-value, confidence interval, stationarity diagnostic, effective-sample-size estimate, or biological-mechanism result. Do not close Gate C based on this run or a single `phi_norm > 1.01` crossing.

## Next authorized steps

1. Preserve Run #54 and its artifact as the 32E checkpoint/source of record.
2. Perform the planned cross-family turnover audit (CFG, NPC-like, spatial, and C2) before attributing turnover differences to the added constraints.
3. Review the 32E trajectory and protocol-defined diagnostics. If continuing the same chain, use Run #54's **actual run ID `38112364771`** and artifact **`fafb-v783-c2-feasibility-2500000000`**, with target accepted swaps **238,877,440 (64E)** and milestone **238,877,440**, keeping seed, code, and C2 constraints unchanged. This 64E extension is a proposed diagnostic continuation, not a claim that it is sufficient to prove convergence.
4. Separately complete the preplanned positive-control sensitivity ladder and negative control; the existing positive control only demonstrates detection of a large planted signal.
5. Keep Gate C and all structure→function/RSS/architecture/benchmark/scaling claims blocked until the full gate criteria are met.

No kernel change, threshold tuning, or post-hoc redefinition is authorized by these results.
