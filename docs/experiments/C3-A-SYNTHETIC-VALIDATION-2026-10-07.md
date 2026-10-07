# C3-A Synthetic Validation Gate — 2026-10-07

## Status

**SYNTHETIC VALIDATION IMPLEMENTATION — CI PASSED — FAFB NOT TOUCHED**

This branch is a validation layer for the provisional C3-A mathematical candidate. It does not modify C2 and does not authorize any FAFB-scale C3 run.

## 1. Mathematical object being validated

For a simple directed graph on fixed nodes, with self-loops excluded from the support and arbor distance d_ij, C3-A uses independent Bernoulli edge variables:

p_ij = sigmoid(alpha_i + beta_j - lambda d_ij), for i != j.

The sufficient statistics are:

- expected out-degree of every source node;
- expected in-degree of every target node;
- expected total wiring length.

The implementation fixes the additive parameter gauge with mean(alpha) = 0.

The total expected edge count is not an additional independent constraint because it equals both the sum of expected out-degrees and the sum of expected in-degrees.

This is a directed canonical analogue of the literature-aligned degree + wiring-length family. It is not claimed to be the exact published directed formula of Salova & Kovacs.

## 2. What was implemented

src/generator/canonical_spatial.py provides a deliberately dependency-free synthetic engine:

- numerically stable sigmoid;
- probability matrix construction with p_ii = 0;
- expected out-degree/in-degree/total-length calculation;
- alternating degree-multiplier fitting for fixed lambda;
- one-dimensional bisection for lambda;
- independent Bernoulli graph sampling;
- graph-level statistic calculation.

It intentionally does not contain FAFB data loading, sparse support approximation, NPC/block constraints, C2 state/resume logic, a large-scale pair enumerator, or a production FAFB sampler.

## 3. Validation tests

tests/test_canonical_spatial.py currently checks:

1. Known-parameter recovery: a small directed spatial model is generated from known alpha, beta, lambda; fitting the expected sufficient statistics recovers the parameters to numerical tolerance.
2. Exact graph enumeration: for N=4, all 2^(N(N-1)) = 4096 loop-free directed graphs are enumerated. The factorized probabilities sum to one, and enumerated expected out-degree, in-degree, and wiring length agree with analytic moments.
3. Independent-sampling recovery: 4,000 independent samples recover analytic ensemble moments within predefined tolerances.
4. Support correctness: independent samples contain no self-loops and remain within the simple directed graph support.
5. Statistic correctness: direct graph-level degree and wiring-length calculations are checked on a small hand-constructed graph.

## 4. Scientific interpretation of this gate

Passing these tests would establish only that the proposed small-scale canonical ensemble is mathematically and computationally consistent with its own definition.

It would not establish:

- that C3-A is the correct biological null;
- that it reproduces FAFB;
- that it is computationally scalable to 138,584 nodes;
- that its fitted parameters are unique/robust on FAFB;
- that its rich-club prediction differs from or agrees with C2;
- any biological significance or mechanism.

## 5. Next gate after synthetic tests

If the synthetic tests pass, the next gate is scalability and fitting feasibility, still without a scientific FAFB run:

- establish memory/runtime cost of evaluating the dense N(N-1) probability surface;
- determine whether expected-degree equations can be solved at useful scale;
- quantify cost of evaluating expected wiring length;
- identify whether any sparse approximation would change ensemble support;
- if an approximation is required, define it as a new model and validate its bias on progressively larger synthetic graphs.

Only after that should a small FAFB pilot be considered.

## 6. Non-negotiable boundary

C2 remains the primary hard-constraint null.

This C3-A branch must never silently alter C2 degree constraints, C2 source-block -> target-block counts, C2 global distance-bin constraint, or C2 frozen-edge treatment.

Any future NPC-aware canonical model is a separate C3-B family and requires its own mathematical definition and validation.

## CI verification

GitHub Actions workflow **tests #587** (run **37625325208**) completed successfully on the current-main-based validation branch.

The workflow executed:
- Python syntax preflight;
- pytest collection preflight;
- full pytest suite.

This closes the **software/CI validation sub-gate**, not the scientific C3-A gate.

## Decision

**C3-A implementation/CI sub-gate: PASSED**

**C3-A scientific validation gate: OPEN**

**FAFB C3: NOT AUTHORIZED**

**FAFB C3: NOT AUTHORIZED**

**C2: UNCHANGED**
