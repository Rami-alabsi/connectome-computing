# C2 Synthetic Positive-Control — Execution Record

## Purpose

This is the first executed implementation of the pre-registered C2 positive-control
plan. It is a synthetic power/control experiment only. It does not use FAFB
data and does not constitute a biological result.

The question is narrow:

Can the unchanged C2 constraint surface and swap kernel detect a rich-club
signal deliberately planted while the seven preserved C2 statistics remain
exactly unchanged?

## Construction

- Directed synthetic graph.
- 80 nodes by default.
- Two source/target blocks: block(u) = u mod 2.
- Three explicit pairwise distance bins.
- Base graph generated before defining the planted club.
- Club membership fixed from the highest total-degree nodes of the base graph.
- Planting uses only C2-valid swaps that increase fixed-club internal edges.
- No self-loops or duplicate directed edges.
- Nulls use the same unbiased conceptual C2 proposal and acceptance rules.
- The primary curve keeps empirical club membership fixed at every degree
  threshold; sampled null degrees therefore cannot move nodes between clubs.

## Predeclared acceptance criteria

The control passes only if:
1. planted club membership is recovered from observed degree;
2. planting preserves edge count, in/out degree, block-pair counts and distance histogram;
3. independent null seeds reduce the planted fixed-club signal;
4. the complete fixed-membership curve shows separation, not only one peak;
5. at least three null seeds reproduce the effect.

A failure would mean the C2 observable/kernel has insufficient demonstrated
power under this constraint geometry.

## Official execution

GitHub Actions workflow run: **37761534464**  
Job: **positive-control** (113258857422)  
Artifact: **c2-positive-control-result**  
Artifact ID: **11542512108**  
Artifact SHA256 digest: **3f59437bf5d0208f21aae4d22e7ba719236b36e9913f6b2581e8888dcb8a0ace**

Predeclared parameters:

- N = 80
- base edge probability = 0.18
- fixed club size = 12
- planting gain = 50 accepted C2-valid swaps
- null seeds = 101, 102, 103
- null attempts per seed = 100,000

## Result

The execution passed all predeclared acceptance criteria.

### Constraint preservation

The base and planted graphs have identical:

- directed edge count: **1,144**
- complete in-degree sequence
- complete out-degree sequence
- source-block → target-block counts:
  - 0→0: 269
  - 0→1: 276
  - 1→0: 320
  - 1→1: 279
- distance-bin histogram:
  - bin 0: 393
  - bin 1: 373
  - bin 2: 378
- no-self-loop condition
- no-duplicate-edge condition

The planted graph increased fixed-club internal edges from **36 to 86**
(+50 accepted C2-valid swaps) without changing any of the preserved C2
statistics above.

### Independent nulls

After 100,000 proposal attempts per seed:

| Seed | Accepted swaps | Final fixed-club edges | Peak phi_norm | Peak threshold |
|---|---:|---:|---:|---:|
| 101 | 14,108 | 36 | 2.54545 | 35 |
| 102 | 14,208 | 41 | 3.11111 | 35 |
| 103 | 14,333 | 34 | 2.33333 | 35 |

The three nulls therefore reduced the planted fixed-club edge count from 86
to 36, 41, and 34 respectively, while preserving the C2 constraint signature.

The complete fixed-membership curves also show a reproducible separation
around the high-degree thresholds, rather than a single isolated point.
The official result file records the full curves for all three seeds.

## Scientific interpretation

**Positive-control result: PASS.**

This establishes a limited but important methodological fact:

> The C2 constraint geometry is capable of detecting a deliberately planted
> rich-club signal that is not encoded in the seven preserved C2 statistics.

Therefore, the absence of a >1.01 signal in the real FAFB C2 nulls cannot be
dismissed solely by saying that the C2 ensemble is intrinsically incapable of
detecting rich-club structure.

This does **not** establish:

- a biological effect in FAFB;
- statistical significance or a p-value;
- formal C2 mixing/convergence;
- a causal mechanism;
- that the observed FAFB residual is meaningful;
- Gate C closure;
- any structure→function, RSS/architecture, benchmark, or scaling result.

## Next controlled step

The positive-control gate is now closed as a **synthetic power sub-gate**.

The next scientific priority remains the independent-ensemble/convergence
question for C2. The 8E continuation demonstrates strong microscopic edge
turnover while aggregate curves remain qualitatively similar, but it is not a
formal stationarity/ergodicity/ESS proof.

No change to the C2 kernel or its seven hard constraints is authorized to
improve the FAFB result.

No FAFB C3 execution is authorized merely because this positive control passed.
C3-A remains a separately validated canonical ensemble candidate.

## Provenance

This record describes the exact GitHub Actions execution above. The archived
JSON artifact is the authoritative machine-readable result for this run.
