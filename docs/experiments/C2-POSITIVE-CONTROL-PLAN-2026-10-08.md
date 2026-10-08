# C2 Positive-Control / Power Plan — 2026-10-08

## Purpose

The C2 null can only support a "no residual" interpretation if the analysis
pipeline demonstrates power to recover a known structural signal that is not
explicitly preserved by the C2 constraints.

This is a control experiment, not a biological result.

## Required planted signal

Construct a synthetic directed graph with:

- a fixed observed degree sequence;
- explicit source/target block assignments;
- explicit spatial distance-bin labels;
- a planted rich-club structure among a known fixed set of high-degree nodes;
- no self-loops or duplicate directed edges.

The planted high-degree membership must be fixed from the observed graph.

The planted signal must be designed so that it is **not** encoded by any C2
preserved statistic. In particular, the block-pair counts and distance-bin
histogram of the planted graph must be matched to the control construction.

## Null procedure

Run the same conceptual C2 swap constraints:

1. preserve directed edge count;
2. preserve in-degree sequence;
3. preserve out-degree sequence;
4. preserve source-block -> target-block counts;
5. preserve global distance-bin histogram;
6. reject self-loops;
7. reject duplicate directed edges.

The planted rich-club is then evaluated against independently randomized graphs
from this constrained ensemble.

## Power criterion

The pipeline passes the positive-control gate only if:

- the planted club membership is recovered from the observed degree sequence;
- the observed planted graph shows a clear rich-club excess;
- constrained null realizations reduce that excess reproducibly;
- the complete curve, not only its maximum, shows the expected separation;
- the result survives multiple synthetic seeds.

A failure is scientifically informative: it means the C2 observable/kernel
may have insufficient power under the relevant constraint geometry, and a
negative FAFB residual cannot then be interpreted as evidence of absence.

## Anti-cheating rule

Do not tune the planted signal after seeing the C2 null result.

The synthetic graph, planted set, constraints, and success criterion must be
defined before inspecting the resulting null curve.

## Scope

This control does not alter C2 and does not authorize C3 or FAFB execution.
A minimal one-block/one-distance-bin sanity control may be used first as a
software smoke test, but it does **not** close the scientific positive-control
gate. A stronger control with heterogeneous blocks and distance bins is
required for scientific closure.
