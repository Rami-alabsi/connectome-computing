# Motif Analysis

Codex explicitly supports three-node connectivity motifs, including reciprocal,
feed-forward-loop and 3-cycle structures. It also exposes connectivity tags such
as rich-club, broadcaster, integrator, attractor, repeller and reciprocal.

Our analysis layer will independently reproduce motif measurements from downloaded
static connection data rather than treating Codex labels as ground truth.

## First motif layer

The first implementation counts transparent six-bit directed signatures over unique
neuron pairs. This is deliberately a baseline rather than the final biological
motif taxonomy.

Next steps:

1. Aggregate regional rows when computing neuron-level motifs.
2. Add canonical directed-triad classification.
3. Compare observed motif counts against degree-preserving random graphs.
4. Measure motif enrichment and significance.
5. Join motif participation with cell type, neuropil and neurotransmitter.
6. Translate robustly enriched structures into candidate computational primitives.

A motif becomes an architectural candidate only after it survives controls and has a
measurable computational interpretation.
