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
M = 138,584 \times 138,583 = 19,205,386,472 
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


## 8. Initial local complexity probe

A dependency-free Python pair-evaluation probe was timed on random 2-D synthetic coordinates, evaluating every ordered non-self pair once and accumulating a wiring-length statistic.

Observed wall times for one full pair pass:

| N | Pair count | One-pass time |
|---:|---:|---:|
| 32 | 992 | ~0.00036 s |
| 64 | 4,032 | ~0.00101 s |
| 128 | 16,256 | ~0.00441 s |
| 256 | 65,280 | ~0.0191 s |
| 512 | 261,632 | ~0.0771 s |
| 1,024 | 1,047,552 | ~0.299 s |

This is a local complexity probe, not a production benchmark and not a claim about FAFB runtime on another machine.

The observed scaling is consistent with O(N²). A naive quadratic extrapolation from N=1,024 would put one full pair pass at roughly 1.5 hours for N=138,584 on comparable single-threaded Python execution. This extrapolation is intentionally treated only as an order-of-magnitude warning; it must not be used as a final performance claim.

Crucially, fitting C3-A requires repeated evaluations of the degree and wiring-length expectations. Therefore a naive dense/streaming implementation could require many such passes. This is currently the main computational feasibility risk.

## 9. Consequence

The project should not proceed directly from the small synthetic implementation to a FAFB fit.

The next technical gate is an exact-support benchmark with a streaming implementation and explicit instrumentation. Any acceleration must be shown to reproduce the same sufficient statistics, rather than merely produce a faster approximate model.


## 10. Exact dense-vs-streaming equivalence and exploratory scaling probe

An additional local synthetic probe compared the dense formulation with the new
exact full-support streaming formulation using the same random 2-D coordinates,
parameters, sigmoid, and Euclidean distance calculation.

For every tested N, both implementations evaluated all ordered non-self pairs.
The resulting total expected wiring lengths agreed to floating-point precision;
the largest observed absolute difference in this probe was approximately
4.6e-8 at N=2,048, with the absolute difference remaining tiny relative to the
total statistic.

Observed wall times for one pass were:

| N | Pair count | Dense | Exact streaming |
|---:|---:|---:|---:|
| 64 | 4,032 | 0.0039 s | 0.0037 s |
| 128 | 16,256 | 0.0092 s | 0.0067 s |
| 256 | 65,280 | 0.0892 s | 0.0246 s |
| 512 | 261,632 | 0.1790 s | 0.0974 s |
| 1,024 | 1,047,552 | 0.9553 s | 0.4509 s |
| 1,536 | 2,357,760 | 1.6712 s | 0.8574 s |
| 2,048 | 4,192,256 | 2.8574 s | 1.5381 s |

These numbers are an exploratory local Python probe, not a hardware-normalized
benchmark and not a FAFB runtime claim. The streaming implementation removes
the N×N probability storage requirement, but it does **not** remove the O(N²)
pair-evaluation cost.

Using the observed streaming timing as a rough local warning only, one full
19.205-billion-pair pass is on the order of hours rather than seconds. Because
C3-A fitting requires repeated sufficient-statistic evaluations, this is not
yet a feasible FAFB implementation.

The correct conclusion at this stage is therefore:

1. Exact streaming preserves the declared full-support ensemble.
2. Exact streaming is substantially lighter in storage than dense evaluation.
3. Exact streaming remains computationally quadratic.
4. No FAFB C3 execution is authorized yet.
5. The next investigation should target exact mathematical acceleration or a
   rigorously validated computational decomposition, not an unannounced sparse
   approximation.
