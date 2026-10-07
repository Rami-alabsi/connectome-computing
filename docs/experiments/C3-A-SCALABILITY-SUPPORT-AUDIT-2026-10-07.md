# C3-A Scalability / Support Audit — 2026-10-07

## Status

**DESIGN AUDIT — NO FAFB C3 RUN AUTHORIZED**

This document audits the computational boundary of the exact C3-A canonical ensemble before any large biological execution.

## 1. Exact support size

C3-A defines an independent Bernoulli variable for every ordered pair i != j.

For N nodes:

\[
M = N(N-1)
\]

For the project graph N = 138,584:

\[
M = 138,584 \times 138,583 = 19,194,? 
\]

The exact value must be computed by code before publication rather than copied from a rough estimate.

The important conclusion is invariant to the final arithmetic: the dense support contains approximately 19.2 billion directed candidate pairs.

A dense N×N probability matrix is therefore not a practical FAFB implementation.

## 2. Why this is a scientific issue, not only an engineering issue

The canonical distribution is defined over the full declared support.

Replacing the support by:
- k-nearest neighbours;
- a distance cutoff;
- observed-contact pairs;
- sampled candidate pairs;
- block-local pairs;
- any other sparse candidate set

changes the probability space and therefore changes the maximum-entropy ensemble.

Such a restriction cannot be described merely as a memory optimization.

It becomes a new model and requires independent synthetic bias validation.

## 3. Exact computation requirements

The mathematical C3-A target requires, for fitted parameters:

- expected out-degree for every node;
- expected in-degree for every node;
- expected total wiring length.

The first two require row/column sums over the declared support.

The third requires the weighted sum of p_ij d_ij.

A production implementation must therefore avoid materializing the full dense probability matrix while still evaluating these quantities over the intended support exactly, or explicitly define and validate a changed support.

## 4. Candidate computational strategies

### Strategy A — Exact dense

Correct ensemble support.

Rejected for FAFB-scale execution because N(N-1) pair storage is too large.

Useful only for small synthetic graphs.

### Strategy B — Exact streaming over all pairs

Do not store p_ij. Evaluate probabilities in chunks and accumulate row/column moments and total length.

This preserves the full support mathematically, but still requires O(N²) pair evaluations per fitting iteration.

It is therefore a candidate for benchmarking, not yet a claim of practical FAFB feasibility.

### Strategy C — Exact/controlled spatial decomposition

Exploit mathematical structure of the distance function and spatial representation to reduce repeated work while retaining exact support.

This requires a proof that the acceleration computes the same sufficient statistics as the dense definition.

No such method is currently accepted by this project.

### Strategy D — Sparse candidate support

Potentially practical, but changes the ensemble.

Must be treated as a separate model and validated against exact small/medium synthetic references.

## 5. First authorized benchmark

Before any FAFB C3 run, benchmark the exact dense and exact-streaming formulations on progressively larger synthetic graphs, for example:

N = 32, 64, 128, 256, 512, 1024

with controlled coordinates and known parameters.

Measure:

- wall-clock time;
- peak memory;
- fitting iterations;
- maximum degree-moment error;
- total-length error;
- numerical stability;
- scaling exponent.

The benchmark is methodological, not biological.

## 6. Scientific stopping rule

Do not escalate to FAFB simply because a sparse approximation makes execution fast.

If exact full-support evaluation is infeasible, report that boundary and decide whether a separately defined support-restricted model is scientifically justified.

## 7. Current decision

- C2: unchanged.
- C3-A synthetic software/CI: passed.
- C3-A scientific validation: open.
- Full-support scalability: **open**.
- Sparse support: **not authorized**.
- FAFB C3: **not authorized**.
