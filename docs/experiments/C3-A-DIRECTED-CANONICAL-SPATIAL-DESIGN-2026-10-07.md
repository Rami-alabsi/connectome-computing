# C3-A — Provisional Directed Canonical Spatial Maximum-Entropy Specification

Date: 2026-10-07
Status: DESIGN ONLY — NOT IMPLEMENTED / NOT SCIENTIFIC RESULT

## 1. Why this model exists

C2 is a microcanonical-style hard-constraint swap ensemble. C3-A is intentionally a different ensemble family, motivated by the maximum-entropy connectome literature.

The purpose is sensitivity/control, not to replace C2 and not to create a novelty claim.

Relevant prior art:
Salova & Kovács (Network Neuroscience, 2025), DOI 10.1162/netn_a_00428, develops canonical maximum-entropy connectome models using degree and spatial constraints. Their framework explicitly discusses directionality as an extensible additional constraint, but the published core models used here are not identical to the project's directed C2 ensemble.

## 2. Candidate target ensemble

For a directed graph with node set V, candidate directed pair (i,j), and arbor distance d_ij, consider independent Bernoulli edge variables with

p_ij = sigmoid(alpha_i + beta_j - lambda * d_ij)

where:
- alpha_i controls expected out-degree of source i;
- beta_j controls expected in-degree of target j;
- lambda >= 0 controls a linear wiring-cost penalty;
- sigmoid(x)=1/(1+exp(-x)).

The canonical maximum-entropy distribution is

P(G) proportional to exp[-H(G)]

with sufficient statistics corresponding to:
- expected out-degree sequence;
- expected in-degree sequence;
- expected total wiring length.

The parameters must be fitted so that the model's expected constraints match the empirical graph to a documented tolerance.

This is a candidate directed analogue of the literature's degree + wiring-length maximum-entropy family, not a claim that the cited paper itself used this exact directed equation.

## 3. Important difference from C2

C2 preserves exactly:
- every node's in-degree;
- every node's out-degree;
- global distance-bin histogram;
- NPC source-block -> target-block counts.

C3-A would preserve the degree statistics and a distance-cost statistic only in expectation.

Therefore:
- C3-A is not a stronger version of C2;
- it is a different null family;
- disagreement between C2 and C3-A is scientifically informative about ensemble definition.

## 4. Required model-fitting checks

Before generating any FAFB ensemble, the implementation must demonstrate:

1. Expected total edge count matches 3,732,460 within a predefined tolerance.
2. Expected out-degree vector matches empirical out-degrees within a predefined aggregate and maximum error criterion.
3. Expected in-degree vector matches empirical in-degrees within the same criteria.
4. Expected total arbor wiring length matches the empirical total within a predefined tolerance.
5. Probability values are numerically stable.
6. Self-loops are handled explicitly and consistently.
7. The treatment of frozen/incomplete-block edges is explicitly decided; C3-A must not silently inherit C2's frozen-edge rule.
8. Any candidate-pair restriction is justified because restricting the support changes the entropy ensemble.

## 5. Sampling requirements

The model is not automatically validated merely because p_ij can be calculated.

The implementation must specify how the full directed ensemble is sampled at FAFB scale.

A naive enumeration of all N(N-1) directed pairs is not acceptable without a documented memory/runtime strategy.

Possible approaches include:
- exact/approximate degree-corrected spatial sampling;
- sparse candidate generation with a proof/quantification of support bias;
- mathematically justified independent sampling if probabilities can be evaluated without enumerating all pairs.

Any approximation that changes the support must be treated as part of the model and validated.

## 6. Synthetic validation

Before FAFB:

A. Generate small directed spatial graphs from known alpha, beta, lambda.

B. Fit the model back to those graphs.

C. Check recovery of:
- expected in/out degree;
- total edge count;
- total wiring length;
- distance dependence.

D. Generate independent ensembles and verify that held-out graph statistics converge to the known target.

E. Compare the model against an exact enumerated small-graph maximum-entropy ensemble where feasible.

Failure of these tests blocks FAFB implementation.

## 7. Rich-club evaluation

Once a validated ensemble exists, each sampled graph should be evaluated using the same rich-club observable already used by C2:

- thresholds 20–120;
- same definition of rich density;
- same observed/reference ratio convention.

Do not change the >1.01 descriptive threshold merely because C3 has a different null.

The primary comparison is not a single peak. Compare the full curve.

## 8. C3-A interpretation rules

If C3-A reproduces the C2 disappearance of the >1.01 region:
- this strengthens the interpretation that the C2 result is not solely an artifact of its hard distance-bin microcanonical construction.

If C3-A restores a >1.01 region:
- do not call this a contradiction;
- first identify which ensemble assumption causes the divergence.

If C3-A cannot be sampled or fitted without uncontrolled approximations:
- do not force it to FAFB scale;
- report the computational boundary and consider a smaller validated subset.

## 9. C3-B is deferred

An NPC-aware canonical model should not be implemented until C3-A is validated.

A possible future C3-B Hamiltonian would add a source-block -> target-block sufficient statistic, but this changes both parameter fitting and the interpretation of the ensemble. It must be derived and validated independently.

## 10. Gate

C3-A is currently:
**MATHEMATICAL CANDIDATE — NOT IMPLEMENTED**

Next authorized technical step:
**small synthetic exact-vs-canonical validation**, followed by a scalability assessment.

No full FAFB C3 scientific run is authorized by this document.


## Operational update — 2026-10-13 (after C2 Run #57 / workflow run #58 / 128E)

The same seed-20261002 C2 continuation has now reached 128E. See [Run #57 completion audit](C2-RUN-57-128E-COMPLETION-AUDIT-2026-10-13.md). The 128E curve still has a descriptive `phi_norm > 1.01` interval (k=38–59); relative to 64E the peak increased from 1.0119604 to 1.0126376 at k=51, and 71/101 curve points increased. This is continuing observable drift, not evidence of a plateau or a formal mixing/convergence result. It does not alter the C3-A design gate or justify changing C2's definition.

### Current authorized order

1. Keep the C2 primary constraint surface frozen; formal mixing/convergence remains OPEN.
2. Execute the documented [external prior-art reproduction plan](C3-A-EXTERNAL-REPRODUCTION-PLAN-2026-10-08.md) for the published undirected k+L family, recording data/code provenance and deviations. Do not call the directed candidate equation an exact reproduction of the published model.
3. Define a small directed synthetic test suite with a known target distribution and exact-enumeration cases where feasible; predeclare parameter-recovery tolerances and edge/self-loop/support conventions.
4. Validate canonical sampling against those small exact cases and test parameter recovery before any FAFB-scale model or ensemble.
5. Benchmark memory/runtime on a smaller subset only after correctness gates pass.

No full FAFB C3-A run is authorized yet. The run's own result remains `scientific_conclusion=null` / `feasibility only; no rich-club inference`; Gate C stays OPEN and structure→function stays BLOCKED.
