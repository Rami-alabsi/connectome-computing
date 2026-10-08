# C3-A External Reproduction Plan — 2026-10-08

## Purpose

Validate the implementation against the published Salova & Kovács k+L family
before using a C3-A residual as sensitivity evidence.

Reference:
Salova & Kovács, Network Neuroscience 9(1), 181–206 (2025),
DOI 10.1162/netn_a_00428.
Public data/code repository: Zenodo 13376416.

## Important model distinction

The published analysis uses the fruit-fly hemibrain dataset and an undirected,
unweighted connectome. Its k+L model combines the degree sequence with total
wiring length as canonical maximum-entropy constraints.

Project C3-A is instead a directed Bernoulli model with separate source and
target multipliers:

p_ij = sigmoid(alpha_i + beta_j - lambda d_ij).

Therefore the reproduction target is a **literature-family validation**, not an
exact reproduction claim and not a claim that the published formula is directed.

## Required reproduction

Using the released hemibrain processed data:

1. reconstruct the undirected, unweighted graph under the published data
   definition;
2. use the published spatial distance definition appropriate to the model;
3. reproduce the k+L fitting logic or execute the released reference code;
4. verify the reported fly characteristic length scale of approximately
   d0 = 9 soma-size units;
5. where feasible, compare graphlet/network statistics reported for k+L;
6. record all preprocessing and any differences from the published pipeline.

## Acceptance

The gate is passed only if the reproduced characteristic scale and at least one
published structural validation statistic agree within a predeclared tolerance,
or if any discrepancy is explained by an identified version/preprocessing
difference.

## Scientific interpretation

Even a successful reproduction does not validate C3-A biologically. It establishes
that the project understands and can reproduce the relevant prior-art model family.

A C3-A residual on FAFB must still be interpreted against the published observation
that k+c can outperform k+L on fly structural measures and that k+L does not
capture all fly distance-dependence heterogeneity.

## Status

**Not executed yet.**

No FAFB C3 run is authorized by this document.
