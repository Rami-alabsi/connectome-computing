# M2 FAFB v783 — Structural synthesis gate

## Scope

This document records the current structural validation state for the real FAFB v783 connection table. It is a measurement record, not a biological or engineering advantage claim.

## Dataset integrity

- 3,732,460 unique directed neuron-pair connections.
- 5,342,446 raw rows.
- 1,609,986 duplicate pair rows attributable to multi-region records.
- 50,666,648 summed synapses across the raw rows.
- 138,584 neurons appearing in the connection table.

The published FAFB dataset contains 139,255 neurons; the smaller 138,584 count here is therefore interpreted as the number of neurons represented by at least one connection-table endpoint, not as a contradiction of the published neuron count.

All structural graph statistics in this project use unique directed pairs unless explicitly stated otherwise.

## Current measurements

### Degree

The graph-statistics implementation was corrected so degree is computed from unique directed pairs rather than raw neuropil rows. This avoids inflating degree when one neuron pair has connection records in multiple neuropils.

### Rich-club

The current rich-club analysis uses total degree = in-degree + out-degree, thresholds selected from observed degree quantiles, directed degree-preserving edge swaps, and exact preservation checks for edge count, in-degree and out-degree.

A preliminary four-null run produced observed/null rich-density ratios of approximately:

| Degree threshold | Observed / null mean |
|---:|---:|
| 106 | 1.055 |
| 167 | 0.974 |
| 374 | 0.707 |
| 510 | 0.576 |

These numbers are not treated as a final rich-club biological conclusion because the initial run used only four null realizations. The workflow has been strengthened to use eight null realizations. The result must be re-read from the resulting artifact before interpretation.

### Reciprocity

A dedicated FAFB reciprocity analysis has been implemented. It measures P(v -> u | u -> v) over unique directed non-self pairs and reports reciprocal-edge count, reciprocal-node count, and reciprocal degree statistics.

The analysis workflow is now triggered by both manual dispatch and relevant source changes. No numerical result is recorded here until a successful CI artifact is available.

### Directed triads

The motif analysis now maps sampled three-node wedges to the 16 canonical directed triad-census classes: 003, 012, 102, 021D, 021U, 021C, 111D, 111U, 030T, 030C, 201, 120D, 120U, 120C, 210, 300.

The current experiment is a wedge sample rather than a full O(N^3) census. Therefore its class frequencies are interpretable only relative to the same sampling procedure applied to degree-preserving null networks.

A CI workflow now records the observed sample and degree-preserving null samples.

## Interpretation gate

The 2026 neuromorphic hierarchical-reservoir literature provides a useful control principle: hierarchical modularity can affect memory, multitasking and timescale diversity, but reported benefits saturate quickly with additional hierarchy; in that study the third level rarely added further benefit over the second. This supports testing hierarchy depth explicitly rather than assuming that more levels are better. See the cited Nature Communications study in the accompanying research record.

The whole-brain Drosophila network literature also demonstrates that reciprocal motifs, rich-club populations and other higher-order structural statistics can be measured directly from the fly connectome. Our analysis therefore treats these quantities as empirical constraints to reproduce or explain, not as evidence that a particular computational architecture is automatically advantageous.

## Next evidence gates

1. Obtain successful CI artifacts for reciprocity and canonical triad sampling.
2. Re-evaluate rich-club statistics using the eight-null run.
3. Add spatial/neuropil-aware null constraints where the available data support them; degree-only randomization is insufficient for testing spatial organization.
4. Compare structural statistics jointly rather than one metric at a time.
5. Only then calibrate synthetic generators and connect the resulting structural constraints to M6 computational experiments.

## Scientific claim boundary

At this stage the project can claim:

> The software now has a real-data FAFB v783 validation path that separates raw connection rows from unique directed neuron-pair structure and provides reproducible null-model analyses for degree, rich-club organization, reciprocity and directed triad composition.

It cannot yet claim that FAFB has a uniquely advantageous architecture, that a rich-club backbone is enriched under all definitions, that any particular motif causes computational performance, or that the proposed connectome-inspired architecture is superior to non-biological baselines.

## Rich-club replication gate (2026-09-24)

The rich-club runner now accepts explicit total-degree thresholds in addition to its exploratory quantile thresholds. This is required for a faithful comparison with published FAFB analysis, which evaluates the rich-club coefficient across degree thresholds and reports a rich-club regime beginning around total degree 37 under its CFG normalization. The published analysis also evaluates the NPC normalization using 100 null samples. This project will treat that published threshold/normalization as a replication target, not as a premise about the biological meaning of the rich club. citeturn0search0

The current CI path remains an 8-null reproducibility gate. A publication-aligned run should use explicit thresholds (rather than the current 90/95/99/99.5% quantiles) and a substantially larger null ensemble before any comparison is interpreted. Because the current Python swap implementation is much less optimized than the graph-tool implementation used in the publication, runtime must be measured before committing the 100-null run to ordinary push CI.

This separates two questions:
1. **Implementation gate:** do our directed swaps preserve edge count, in-degree, out-degree and, for NPC, neuropil block counts exactly?
2. **Replication gate:** does the observed rich-club curve reproduce the published CFG/NPC pattern under the same degree definition and thresholding convention?

Until the second gate is run and its artifact inspected, the project should not describe the current rich-club result as a replication or biological confirmation.
