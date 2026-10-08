# C2 Synthetic Positive-Control — Execution Record

## Purpose

This is the first implementation of the pre-registered C2 positive-control
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

## Execution status

**Implementation prepared; execution remains the next controlled step.**

No FAFB execution is authorized by this document.

## Interpretation boundary

A positive-control pass demonstrates only detectability of a synthetic signal
under the C2 constraint geometry. It does not establish that the FAFB residual
is real, significant, mechanistic, or computationally useful.
