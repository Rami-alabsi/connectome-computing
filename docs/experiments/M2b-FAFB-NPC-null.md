# M2b — FAFB neuropil-constrained null model

## Purpose

The structural analysis now separates a degree-only null from a mesoscale anatomy-aware null. This is required before interpreting a rich-club signal as topology-specific.

The 2024 whole-brain Drosophila network analysis used a neuropil connection (NPC) null that preserves degree sequences and inter-/intra-neuropil connection probabilities. Their neuron-to-neuropil assignment used the neuropil containing the largest number of outgoing synapses.

Our implementation follows that operational definition using the FAFB v783 connection table itself:

1. collapse duplicate synapse rows to unique directed neuron pairs for topology;
2. assign each neuron to its dominant outgoing-synapse neuropil using summed `syn_count`;
3. randomize directed edges with endpoint swaps;
4. accept a swap only when source-neuropil and target-neuropil block identities are preserved;
5. require exact preservation of directed in-degree and out-degree;
6. prohibit self-loops and duplicate directed pairs;
7. measure the rich-club curve against the resulting null ensemble.

This is a degree-corrected block-constrained null, not a generative claim about biological wiring.

## Scientific gate

A rich-club enrichment that survives the degree-only null but disappears under the neuropil-block null should be interpreted as compatible with mesoscale anatomical organization rather than as evidence for an additional topology-specific rich-club mechanism.

If enrichment survives both nulls, the next controls should include spatial-distance constraints and, where possible, alternative neuron-to-neuropil assignments.

The published Drosophila study is the prior-art reference for this control hierarchy; it reported that its observed network was not more connected than its NPC model, indicating that interneuropil connectivity contributed substantially to the measured rich-club effect.

## Reproducibility

The CI workflow runs eight deterministic null seeds and records:

- target and successful swap counts;
- exact in/out-degree preservation;
- exact source-neuropil -> target-neuropil block-count preservation;
- observed/null rich-club density at the same degree thresholds.

No biological conclusion is made from the implementation until the artifact is inspected.
