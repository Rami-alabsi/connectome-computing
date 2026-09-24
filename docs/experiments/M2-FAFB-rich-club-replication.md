# M2 — FAFB Rich-Club Replication Record

Status: IN PROGRESS — CFG benchmark gate
Last updated: 2026-09-24

## Objective
Test whether the rich-club organization reported by Lin et al. remains observable in FAFB v783 when matching the principal methodological choices: 5-synapse threshold, total degree, directed rich-club coefficient, degree-preserving CFG null, explicit degree sweep, and ultimately a 100-null ensemble.

This is a method-aligned v783 extension, not an exact v630 reproduction.

## Reference target
Published v630 result: rich-club onset around total degree 37; preferential enrichment fades around approximately 100; 100 CFG samples used for normalization.
These are reference observations, not values to be forced onto v783.

## Benchmark command
Minimum synapses: 5.
Nulls: 2 for runtime benchmark only.
Swaps per edge: 1.0.
Thresholds: 20 through 120, step 1.

## Critical data-table rule

Codex documents that connection tables may contain multiple rows for the same neuron pair when synapses occur in multiple regions/neuropils. Therefore the 5-synapse connection threshold must be applied to the **sum of synapses across all rows for the same directed neuron pair**, not independently to each row. The runner now aggregates pair-level synapse counts before thresholding. This rule is tested in `tests/test_fafb_rich_club.py`.

## Acceptance criteria
- input and five-synapse filtering verified;
- unique directed pairs verified;
- edge count, in-degree and out-degree preserved for every null;
- no self-loops or duplicate directed pairs;
- total-degree definition verified;
- Phi(d) verified;
- threshold 37 explicitly included;
- complete 20–120 curve inspected;
- runtime benchmark measured;
- 100-null final CFG run completed, or limitation documented;
- final artifact and provenance inspected;
- interpretation written only after artifact inspection.

## Run history

- **35962189226 — FAILED:** workflow syntax error; `/usr/bin/time` attempted to execute `PYTHONPATH=.` as a binary. No scientific computation ran.
- **35962219553 — SUPERSEDED:** corrected benchmark workflow from the pre-aggregation implementation. Do not use as scientific evidence.
- **35962522090 — SUCCESS:** first successful real-data publication-aligned v783 rich-club benchmark on commit `9138d7280b4ca5219ed2f56560569751a6aafe99`. Artifact `fafb-v783-rich-club-publication-benchmark`, ID `10792907968`.
- **Current combined anchor — Run 35984738032:** in progress. Download, structural profile, reciprocity, and spatial/neuropil inventory have completed successfully; rich-club is running; motif and artifact upload are pending.

### Scientific gate status

**Gate A is OPEN, not closed.**

The successful 2-null benchmark proves that the real v783 rich-club execution path works and produces a degree-preserving null-controlled curve. It does not close the publication-aligned CFG gate because the final ensemble target is 100 nulls and swap realization quality still needs to be audited.

The combined real-data anchor is the next operational checkpoint. Its successful downstream artifacts must be inspected before declaring the broader biological pipeline executed.

## Expected artifact
artifacts/fafb-v783/rich-club.json

## Interpretation categories
Consistent with published regime: v783 shows a comparable qualitative pattern after matching the major method choices.
Different from published regime: v783 materially differs.
Inconclusive: implementation, dataset, or null-ensemble limitations prevent a conclusion.

No outcome should be described as a failure of the project.
## Real-data benchmark execution — 2026-09-24

Run 35962522090 completed successfully on commit 9138d7280b4ca5219ed2f56560569751a6aafe99.

Artifact:
- name: fafb-v783-rich-club-publication-benchmark
- artifact ID: 10792907968
- SHA-256: 3054b154f18dfd6bae821d084bbd159f1c1d2d5ee13dd90e1ab7b65bd297aea1

Execution parameters:
- FAFB v783;
- pair-level synapse aggregation before thresholding;
- minimum synapses = 5;
- nulls = 2;
- target swaps per null = 3,732,460;
- total-degree sweep = 20–120, step 1.

Measured graph:
- unique directed pairs = 3,732,460.

Null integrity:
- null 0: edge count preserved; in-degree preserved; out-degree preserved.
- null 1: edge count preserved; in-degree preserved; out-degree preserved.

Runtime:
- wall time = 16:11.20;
- maximum resident set size = 1,900,488 kB.

Preliminary curve observation:
- first phi_norm > 1.01 occurs at degree 27;
- degree 37: phi_norm = 1.0152909340573695;
- degree 75: phi_norm = 1.04715818882749;
- peak in the 20–120 sweep: degree 97, phi_norm = 1.0581033995668143;
- phi_norm > 1.01 remains true at degree 120 (1.0420106013590444), so the current descriptive offset is beyond the tested range.

Interpretation status:

Benchmark evidence only. This establishes that the real v783 rich-club path executes successfully and that the observed curve is enriched relative to the two generated degree-preserving nulls. It does not yet establish publication replication because the paper used 100 CFG samples and v630, while this run used v783 and 2 nulls.

The measured runtime suggests approximately 13.5 hours for 100 nulls under naive linear scaling. This is only a planning estimate; actual scaling must be measured. Before the 100-null run, record realized successful swaps and failed attempts so the null-randomization quality is auditable.

The result also does not close the broader FAFB biological gate. Reciprocity, motif, spatial/contact and complete profile artifacts still require real-data execution.