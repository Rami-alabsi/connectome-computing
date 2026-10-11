# C2 Next Diagnostic Protocol — 2026-10-08

## Purpose

Define the next diagnostic work justified by the completed C2 8E extension without changing the C2 scientific kernel.

This protocol does **not** declare formal convergence, stationarity, ergodicity, burn-in adequacy, or Gate C closure.

## 1. Extended-chain diagnostic

Continue one existing C2 chain from the verified 8E state.

### Milestones

- 8E = 29,859,680 accepted swaps — existing baseline
- 16E = 59,719,360 accepted swaps
- 32E = 119,438,720 accepted swaps

Use the unchanged proposal/acceptance kernel and the same dataset, C0 artifact, seed, and constraint fingerprint.

At each milestone record:

- accepted swaps
- proposal attempts
- cumulative acceptance rate
- overlap with the observed graph
- phi_norm at k = 32, 50, 60, 84, 100, 120
- maximum phi_norm and threshold
- first threshold(s) with phi_norm > 1.01
- first threshold with phi_norm < 0.99
- pairwise edge-set Jaccard against the 8E state and previous milestone when available

The existing runner already supports arbitrary accepted-swap milestone values through `--mixing-milestones`.

### Interpretation

The observed-graph overlap is a memory diagnostic, not a stationarity criterion. A continuing decline in overlap does not by itself prove non-convergence. The key question is whether aggregate observables stabilize while microscopic edge turnover continues.

Do not stop because overlap reaches a chosen numerical value unless an independent, predeclared convergence criterion has been established.

## 2. Cross-family turnover audit

Before interpreting the CFG → NPC-like → spatial → C2 enrichment ladder as purely a consequence of progressively stronger constraints, quantify starting-state memory across the null families.

For every available family, record at minimum:

- null family
- number of accepted swaps per edge
- number of null realizations
- overlap with the observed graph
- if available, final-state pairwise Jaccard
- corresponding rich-club observable

The audit must distinguish:

1. constraint effect;
2. residual starting-state memory;
3. proposal/acceptance-rate differences.

If the required overlap information is absent from historical artifacts, recover it from the saved final edge sets where possible. Do not reconstruct missing values from rounded prose.

### Follow-up

If the families have materially different starting-state memory, repeat the relevant comparison at matched turnover/convergence diagnostics before making a causal statement about the enrichment ladder.

## 3. Positive-control sensitivity ladder

The existing C2 positive control is closed for its declared question: C2 can detect a large planted signal not encoded by the seven preserved constraints.

It does not establish sensitivity to a ~1% FAFB-scale residual.

A second synthetic control should therefore test predeclared smaller effect sizes, preferably including approximately:

- 1%
- 2%
- 5%
- 10%

The planting operation must continue to preserve all seven C2 constraints exactly.

Include a negative control whose structure is fully encoded by preserved block/distance constraints and should therefore not survive as an independent C2 residual.

Report the full curve rather than only its maximum.

## 4. Decision rules

### If 16E/32E aggregate curves plateau

Record strong microscopic turnover plus aggregate stability, but do not call this a formal proof of convergence. This can support proceeding to the remaining Gate C sensitivity controls.

### If aggregate curves continue to drift

Treat the 8E result as insufficient and extend/reassess the mixing diagnostic. Do not interpret the 8E >1.01 crossing as a biological result.

### If the residual disappears

Update the candidate-residual interpretation accordingly.

### If the residual persists

Retain it as a candidate residual and test it against the spatial canonical sensitivity ensemble and the strengthened power controls. Do not convert it into mechanism evidence.

## 5. Frozen boundaries

- C2 proposal/acceptance kernel: unchanged.
- Seven C2 hard constraints: unchanged.
- No threshold tuning after seeing the results.
- phi_norm > 1.01 and <0.99 remain descriptive flags, not significance thresholds.
- Structure→function, RSS, architecture, benchmark, and scaling remain blocked until Gate C is resolved.
- C3-A FAFB execution remains unauthorized until its synthetic and external validation gates are satisfied.

## 6. Compass

C2 replication COMPLETE
→ 8E diagnostic COMPLETE
→ **16E/32E diagnostic**
→ **cross-family turnover audit**
→ **positive-control sensitivity ladder**
→ C3-A scientific/external validation
→ Gate C decision
→ only then structure→function.

