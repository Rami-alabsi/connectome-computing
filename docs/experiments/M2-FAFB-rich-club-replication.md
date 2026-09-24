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
Run 35962189226: failed before scientific computation because /usr/bin/time attempted to execute PYTHONPATH=. as a binary. This was a workflow syntax error.
Run 35962219553: corrected benchmark; last observed status was queued. Retrieve current status and artifact before interpretation.

## Expected artifact
artifacts/fafb-v783/rich-club.json

## Interpretation categories
Consistent with published regime: v783 shows a comparable qualitative pattern after matching the major method choices.
Different from published regime: v783 materially differs.
Inconclusive: implementation, dataset, or null-ensemble limitations prevent a conclusion.

No outcome should be described as a failure of the project.