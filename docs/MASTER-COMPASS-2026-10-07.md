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

### C2 extended-chain mixing diagnostic — 8E COMPLETE

The planned continuation from the completed 1E/#47 checkpoint is now complete through **8E accepted swaps** under the unchanged C2 proposal/acceptance kernel.

Provenance:
- source chain: seed **20261002** / Run #47;
- 500M-proposal checkpoint: workflow **37729284335**, artifact **11531289161**, SHA-256 **b1a54a8070f6288d61e6d48b51b023c7ef863a1bf89352f1c3852bad6767ff62**;
- completion run: workflow **37737675496**, artifact **11532885112**;
- final target: **29,859,680 accepted swaps = 8E**;
- final proposals: **500,418,411**;
- final cumulative acceptance: **5.9669427%**;
- all seven C2 invariants remained true;
- final observed-edge overlap: **0.2481518891 (~24.8152%)**.

Clean milestone records from the source run and completion artifact show substantial microscopic turnover:
- 1E: ~47.9% overlap;
- 2E: **38.8240%**;
- 4E: **31.1357%**;
- 8E: **24.8152%**.

The 8E final rich-club curve has:
- max phi_norm **1.0106499041 @ k=51**;
- descriptive >1.01 region at **k=45 and k=47–56**;
- phi_norm <0.99 beginning at **k=84** and continuing through k=120;
- k=120 minimum **0.9582184648**.

The 8E chain therefore shows **strong microscopic turnover with a qualitatively persistent aggregate curve**, including a mild positive region and a distinct high-degree depletion region. The 4E and 8E descriptive >1.01 crossings must be retained as observations; they do not retroactively invalidate the three-seed result and are not significance tests.

**Critical interpretation boundary:** this is a mixing/stability diagnostic, not a formal proof of stationarity, ergodicity, burn-in adequacy, effective sample size, or convergence. The chain has one starting state and one seed; aggregate stability plus edge turnover is evidence for mixing behavior, not a theorem about the stationary ensemble.

Decision:
- **C2 8E mixing diagnostic: COMPLETE.**
- **Formal C2 mixing/convergence: OPEN.**
- **Gate C: OPEN.**
- C2 definition/kernel: unchanged.
- Structure→function, RSS/architecture, benchmark and scaling remain blocked.

Next authorized work: positive-control/power validation of the C2 constrained ensemble, then scientific validation/external reproduction of the C3-A spatial canonical sensitivity family. No further C2 extension is required unless a new diagnostic question is justified.

### C2 positive-control / power validation — CLOSED

The synthetic C2 positive-control has now been executed and verified through GitHub Actions.

- workflow: **37761534464**
- artifact: **11542512108**
- artifact SHA-256 digest: **3f59437bf5d0208f21aae4d22e7ba719236b36e9913f6b2581e8888dcb8a0ace**
- synthetic graph: N=80, two source/target blocks, three distance bins
- fixed club: 12 highest-total-degree nodes from the unplanted base graph
- planted fixed-club edges: **36 → 86**
- preserved exactly: edge count, full in/out-degree sequences, block-pair counts, distance-bin histogram, no self-loops, no duplicate edges
- independent null seeds 101/102/103 after 100,000 attempts: fixed-club edges **36 / 41 / 34**
- all predeclared acceptance criteria passed.

Interpretation: the unchanged C2 constraint geometry can detect a deliberately planted rich-club signal that is not encoded by the seven preserved C2 statistics. This is a **synthetic power/control result only**. It does not establish a FAFB effect, significance, mechanism, mixing/convergence, or Gate C closure.

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
