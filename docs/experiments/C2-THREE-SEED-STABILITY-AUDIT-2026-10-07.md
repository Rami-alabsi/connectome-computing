# C2 THREE-SEED STABILITY AUDIT — 2026-10-07

## Purpose

Non-invasive audit of the three complete C2 artifacts (Runs #45, #46, #47) before any Gate-C decision. This audit does not generate a new null and does not alter the primary C2 constraint surface.

## Inputs

- Run #45 artifact: 11461697865, seed 20260935
- Run #46 artifact: 11466140681, seed 20261001
- Run #47 artifact: 11481125143, seed 20261002

All three artifacts contain the final JSON and checkpoint state and were independently verified as target-complete.

## Three-seed scalar stability

| Metric | #45 | #46 | #47 |
|---|---:|---:|---:|
| Attempts | 55,361,441 | 55,237,500 | 55,264,717 |
| Acceptance | 6.7419849% | 6.7571125% | 6.7537847% |
| Max phi_norm | 1.0076220772 | 1.0076660262 | 1.0077486180 |
| Peak threshold | 51 | 50 | 51 |
| Original-edge overlap | 47.91376197% | 47.91287783% | 47.92729192% |
| Frozen edges | 9,869 | 9,869 | 9,869 |
| Block-pair classes | 3,648 | 3,648 | 3,648 |
| Any phi_norm > 1.01 | No | No | No |

Across the three runs:
- mean acceptance = **6.7509607%**
- sample SD acceptance = **0.007949 percentage points**
- mean max phi_norm = **1.0076789071**
- max-min max-phi spread = **0.0001265409**
- mean overlap = **47.91797724%**
- sample SD overlap = **0.0080789 percentage points**

## Full-curve comparison

The complete threshold 20–120 phi_norm curves were compared directly.

Pairwise Pearson correlations:
- #45 vs #46: **0.9999346**
- #45 vs #47: **0.9999503**
- #46 vs #47: **0.9999321**

Maximum absolute pointwise phi_norm differences:
- #45 vs #46: **0.0006511**
- #45 vs #47: **0.0005282**
- #46 vs #47: **0.0006645**

The largest three-run pointwise spread occurs at degree **72** and is **0.00066445**. No curve develops a >1.01 region.

This is strong evidence that the *descriptive shape* of the C2 rich-club curve is reproducible across the three RNG seeds.

## Acceptance-trajectory observation

Run #47 logs show a smooth decline in acceptance rate as accepted swaps accumulate, without a late-stage collapse or stall:
- 50.0M attempts: 3,408,157 accepted, 6.8163%
- 55.0M attempts: 3,716,476 accepted, 6.7572%
- 55.2M attempts: 3,728,553 accepted, 6.7546%
- final: 55,264,717 attempts, 3,732,460 accepted, 6.7538%

Throughput remained healthy, reaching roughly 122k attempts/s late in the run, with RSS current around 2.03 GB and RSS max around 2.79 GB.

This rules out an obvious late-run computational stall in #47. It is not, by itself, a proof of Markov-chain mixing.

## Pairwise edge-set turnover / Jaccard

The three final edge sets were compared directly from the artifact checkpoint states (3,732,460 directed edges per realization). Pairwise intersection and Jaccard similarity were computed on the exact directed edge sets:

| Pair | Shared directed edges | Jaccard |
|---|---:|---:|
| #45 vs #46 | 1,464,302 | **0.2440252** |
| #45 vs #47 | 1,464,819 | **0.2441324** |
| #46 vs #47 | 1,464,014 | **0.2439655** |

Thus pairwise edge-set Jaccard is tightly clustered around **24.4%**, while the full rich-club curves correlate at >0.99993.

This is useful evidence that the three realizations are not simply reproducing nearly identical final edge sets. It also shows that a highly reproducible aggregate observable can coexist with substantial microscopic graph turnover. However, final-state Jaccard alone is **not** a formal mixing diagnostic: it does not provide within-chain autocorrelation, ESS, burn-in/convergence behavior, or a convergence bound.

## Mixing/convergence boundary

The existing artifacts provide:
- independent seeds;
- pairwise final-edge-set Jaccard/turnover;

- complete final graphs;
- full final rich-club curves;
- checkpoint histories;
- acceptance trajectories/logs.

They do **not** provide a formal mixing diagnostic such as integrated autocorrelation time, effective sample size from a trajectory of observables, independent chain distance over time, or a proven total-variation/convergence bound.

Therefore:

**Observed:** strong cross-seed reproducibility of the final descriptive curve.

**Not established:** formal chain mixing/convergence.

This distinction is retained explicitly.

## Discovery/control reading

The striking feature is not only the absence of >1.01; it is the tight reproducibility of the entire curve shape across independent seeds. This is a useful control signal supporting the interpretation that the C2 outcome is not a single-seed accident.

It should not yet be promoted to a biological mechanism or uniqueness claim.

## Decision

- Three-seed C2 replication: **COMPLETE**
- Pairwise final-edge-set Jaccard: **~24.4% across all three pairs**

- Non-invasive curve stability audit: **PASSED as a reproducibility/control check**
- Formal mixing/convergence: **OPEN**
- Gate C: **OPEN**
- Primary C2 definition: **UNCHANGED**
- Next authorized control: **stronger spatial/max-entropy sensitivity family**, followed by Gate-C decision.
