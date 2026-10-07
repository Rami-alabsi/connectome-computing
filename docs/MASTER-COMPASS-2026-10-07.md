# MASTER COMPASS — Connectome Computing
## Authoritative handoff snapshot — 2026-10-07

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

### Three-seed stability audit
- Full-curve Pearson correlations: **0.9999321–0.9999503**.
- Maximum pointwise difference: **0.0006645**.
- Acceptance: **6.74198%, 6.75711%, 6.75378%**.
- Observed-edge overlap: ~**47.91–47.93%**.

Interpretation: strong descriptive reproducibility. **Not** a formal mixing/convergence proof, significance test, mechanism, uniqueness proof, or computational advantage.

### C3 guardrails
- Salova & Kovács (Network Neuroscience, 2025; DOI 10.1162/netn_a_00428) establishes relevant canonical maximum-entropy spatial connectome modeling. Generic spatial max-entropy nulls are **not novel**.
- C3-A is a separate canonical directed sensitivity ensemble; it does **not** replace C2.
- Candidate model uses independent directed Bernoulli edges with a sigmoid(alpha_i + beta_j - lambda d_ij) probability.
- Required before FAFB: exact small-graph checks, parameter/moment recovery, explicit self-loop/support treatment, and scalable sampling audit.
- Any sparse/candidate support restriction changes the ensemble and must be treated as a scientific model choice.
- C3-B (NPC-aware canonical extension) is deferred until C3-A is validated.

### Authorized sequence
**C2 replication CLOSED → stability audit PASSED → formal mixing OPEN → C3 prior-art/design → synthetic validation → spatial/max-entropy sensitivity ensemble → Gate C decision → structure→function → matched ablations → computational abstraction → benchmark → scaling.**

### Non-negotiable boundaries
- Do not alter C2 to improve a result.
- Do not call descriptive phi_norm > 1.01 a p-value/significance threshold.
- Do not convert the ~0.76% C2 residual into a mechanism; it is a **candidate residual**.
- Do not claim architecture/commercial value before matched computational validation.
- Unexpected results trigger discovery-watch verification, not confirmation bias.
