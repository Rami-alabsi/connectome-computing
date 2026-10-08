# MASTER COMPASS — Connectome Computing
## Authoritative handoff snapshot — 2026-10-08

### Mission
Explore whether biological connectome structure can reveal computational principles that remain useful after controlled reconstruction, matched controls, ablations, and scaling.

**Core rule: biology is evidence, not specification.**

### Canonical dataset
- FlyWire FAFB v783; authoritative Princeton synapse table.
- Main graph: **138,584 nodes; 3,732,460 unique directed pairs** after pair aggregation and the 5-synapse threshold.
- C0 arbor-distance definition and spatial bins are the authoritative spatial path.

### Gate state
| Gate | State |
|---|---|
| Gate A / CFG | **CLOSED** |
| Gate B / NPC-like | **CLOSED** |
| C0 / C1 | **CLOSED** |
| Spatial 8-null | **STABLE** |
| C2 three-seed replication | **COMPLETE** |
| C2 stability audit | **PASSED as reproducibility/control** |
| Formal C2 mixing/convergence | **OPEN** |
| Gate C | **OPEN** |
| Structure → function | **BLOCKED** |
| Architecture / benchmark / scaling | **BLOCKED** |

### C2 authoritative result
Runs #45, #46, #47 are independent artifact-complete realizations using the same C2 definition/kernel/dataset.

Each reached **3,732,460 accepted swaps** and preserved exact directed edge count, in-degree sequence, out-degree sequence, source-block → target-block counts, global arbor-distance-bin histogram, no self-loops, and no duplicate directed edges.

Frozen edges without complete block assignment: **9,869**.

Rich-club maxima:
- #45: **1.0076221 @ d=51**
- #46: **1.0076660 @ d=50**
- #47: **1.0077486 @ d=51**

No run has **phi_norm > 1.01**.

The C2 three-seed result must not be summarized as "enrichment disappeared."
The full curve retains a reproducible mild positive region around **k≈32–60**
while the high-degree tail becomes depleted. For Run #46, the review of the
authoritative curve found 29 consecutive thresholds with phi_norm > 1.005
(k=32–60), followed by values below 1 at higher thresholds and about 0.963 at
k=120. The positive criterion >1.01 is therefore not the only observable.

From this point, C2 reporting records both:
- enrichment: **phi_norm > 1.01** (existing descriptive flag);
- depletion: **phi_norm < 0.99** (new symmetric descriptive flag).

Neither is a significance threshold. The complete curve, not only the maximum,
is the primary descriptive object.

### Three-seed stability audit
- Full-curve Pearson correlations: **0.9999321–0.9999503**.
- Maximum pointwise difference: **0.0006645**.
- Acceptance: **6.74198%, 6.75711%, 6.75378%**.
- Observed-edge overlap: ~**47.91–47.93%**.
- Pairwise final-edge-set Jaccard: **0.2439655–0.2441324** (~24.4%).

Interpretation: strong descriptive reproducibility despite substantial microscopic edge turnover. **Not** a formal mixing/convergence proof, significance test, mechanism, uniqueness proof, or computational advantage.

### C2 mixing extension

A diagnostic extension has now been added to the runner to record, during one continued chain, observed-edge overlap and phi_norm at k=32, 50, 60, 100, and 120 at accepted-swap milestones. The intended continuation was executed from the completed 1E/#47 checkpoint. It reached 2E and 4E milestones, then hit the 500M proposal cap at 29,835,212 accepted swaps, leaving 24,468 accepted swaps to the 8E target of 29,859,680. The extension remains a convergence diagnostic rather than a proof of stationarity or ergodicity. The next authorized action is to resume from the verified 500M checkpoint and complete those remaining swaps without changing the C2 proposal or acceptance kernel.

### C3 guardrails
- Salova & Kovács (Network Neuroscience, 2025; DOI 10.1162/netn_a_00428) establishes relevant canonical maximum-entropy spatial connectome modeling. Generic spatial max-entropy nulls are **not novel**.
- C3-A is a separate canonical directed sensitivity ensemble; it does **not** replace C2.
- Candidate model uses independent directed Bernoulli edges with a sigmoid(alpha_i + beta_j - lambda d_ij) probability.
- Required before FAFB: exact small-graph checks, parameter/moment recovery, explicit self-loop/support treatment, scalable exact-support audit, and an external-data reproduction check.
- The primary C3-A rich-club observable uses **fixed empirical club membership** (nodes selected by degree in the observed graph), so sampled degree fluctuations cannot move nodes across the threshold and create an artificial signal.
- Any C3-A residual must be interpreted against the known limitation of the k+L-like ensemble: the published hemibrain study reports that k+c can outperform k+L on fly data and that k+L does not capture distance-dependence heterogeneity as well. Therefore a C3-A residual is not mechanism evidence by itself.
- Positive-control requirement: before interpreting a null negative, demonstrate power by planting a known rich-club signal in a synthetic graph compatible with the C2 structural/block/spatial constraints and verify that the full C2 analysis recovers it.
- Salova & Kovács report k+L characteristic distance d0 around 9 soma-size units for fly, and provide public processed data/code through Zenodo 13376416. Reproduction of a small external k+L result is a validation gate, not a claim that C3-A is their model.

- Any sparse/candidate support restriction changes the ensemble and must be treated as a scientific model choice.
- C3-B (NPC-aware canonical extension) is deferred until C3-A is validated.

### Gate C closure criteria

Gate C is not closed by a single null maximum. Before Gate C can close, the
project must have:

1. a stable C2 full-curve result including both enrichment and depletion observables;
2. an executed extended-chain mixing diagnostic, with its limitations explicitly reported;
3. a positive-control/power demonstration for the C2 constrained ensemble;
4. a scientifically validated spatial sensitivity ensemble, or a documented reason why an exact full-support C3 model is computationally infeasible;
5. if C3-A is used as sensitivity evidence, an external-data reproduction check against the published k+L family on the released hemibrain/Zenodo data;
6. only then, a decision on whether the observed C2 residual is robust enough to motivate structure→function analysis.

These are closure criteria, not a promise that Gate C must close in favor of the hypothesis.

### Authorized sequence
**C2 replication CLOSED → stability audit PASSED → formal mixing OPEN → C3 prior-art/design → synthetic validation → spatial/max-entropy sensitivity ensemble → Gate C decision → structure→function → matched ablations → computational abstraction → benchmark → scaling.**

### Non-negotiable boundaries
- Do not alter C2 to improve a result.
- Do not call descriptive phi_norm > 1.01 a p-value/significance threshold.
- Do not convert the ~0.76% C2 residual into a mechanism; it is a **candidate residual**.
- Do not claim architecture/commercial value before matched computational validation.
- Unexpected results trigger discovery-watch verification, not confirmation bias.
