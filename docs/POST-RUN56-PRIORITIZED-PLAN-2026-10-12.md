# Post-Run #57 Prioritized Research Plan
## Decision note — 2026-10-13

This note operationalizes the latest review. It does not change the C2 null definition, authorize a long run, close a gate, or report new scientific findings. The current live-run status must always be checked against GitHub.

## Priority 0 — Completed: Run #57 128E completion and artifact audit (2026-10-13)

Run #57 (workflow 38244237906) reached 477,754,880 accepted swaps and its artifact ZIP was independently downloaded, hashed, and inspected. The ZIP digest matches GitHub; it contains the final JSON and checkpoint. The JSON records seed 20261002, 8,280,080,824 attempts, matching code/input/constraint fingerprints, target reached, and all seven declared invariants true. Full audit: `docs/experiments/C2-RUN-57-128E-COMPLETION-AUDIT-2026-10-13.md`.

The five same-chain result artifacts (8E/16E/32E/64E/128E) have now all been downloaded and ZIP-hashed independently; every digest matches GitHub. Their 101-point curves were compared at common thresholds. The 64E→128E curve has Pearson r=0.99992982, mean delta +0.0001459177, RMSE 0.0002613567, and max absolute delta 0.0006879088 at k=50; 71 thresholds increased and 30 decreased. Original-edge overlap declined from 24.8152% at 8E to 12.0973% at 128E. This is evidence of continued trajectory/turnover, not a convergence certificate. Full comparison: `docs/experiments/C2-128E-CURVE-DRIFT-COMPARISON-2026-10-13.md`.

Next step: review the curve/turnover evidence and prioritize matched cross-family controls. Do not launch PR #7 or another expensive C2/C3 run without a separate budget and scientific decision.

## Priority 1 — Close the cross-family turnover / edge-set evidence gap

Before another expensive C2 extension, add prospective edge-set and overlap accounting to the relevant CFG, NPC-like, and spatial runners:
- overlap with the original edge set;
- overlap between independent nulls where practical;
- accepted swaps, attempted proposals, and unique edges changed;
- the exact state/edge-list fingerprint and all invariant checks.

Use one representative null per family first. CFG can use a short diagnostic; NPC-like and spatial runs should have a predeclared runtime cap around 20–25 minutes per diagnostic. These are feasibility probes, not a substitute for adequate replication. Do not backfill missing historical edge sets or infer turnover from acceptance rate.

Interpret overlap only as a state-memory/turnover diagnostic. A simple random-selection heuristic such as exp(-2) is a reference intuition, not a calibrated expected overlap for these constrained samplers; the real proposal process, frozen edges, rejections, and dependencies can change it.

## Priority 2 — Redesign PR #7 sensitivity as effect-size calibration

The existing synthetic +1/+2/+5/+10/+50-edge ladder on a small graph does not establish power to detect a 1% effect on FAFB. Before execution, revise the plan to include:
- effect sizes of 1%, 2%, and 3% of a clearly defined rich-club edge count, with the denominator and integer-rounding rule fixed in advance;
- a positive control that creates a known, measurable club-enrichment effect;
- a negative control with the same perturbation budget but no intended club enrichment;
- sham/no-effect trials to estimate false-positive behavior;
- multiple independent graph/chain seeds and repeated trials per effect size;
- explicit invariants and artifact/fingerprint checks;
- a predeclared primary threshold/statistic or a multiple-testing correction across thresholds;
- empirical detection rate, false-positive rate, uncertainty intervals, and failure cases.

Define exactly what “planting an effect” means under the graph constraints. Prefer a controlled edge-replacement/rewiring intervention if the scientific question is about enrichment under fixed edge count; do not silently add edges or violate C2 constraints and then claim the same test. First validate the test harness synthetically, then run a bounded FAFB-scale calibration only after Run #56 audit and budget approval. Do not call this a calibrated 1% test until the false-positive and detection behavior is demonstrated at the target scale.

## Priority 3 — C3-A external reproduction before any full-FAFB attempt

Keep C3-A gated. The next concrete step is to reproduce the published k+L spatial model on released hemibrain data from Zenodo, using the paper's original graph directionality and preprocessing (the cited reproduction target is undirected). Record the exact dataset/version, DOI/record, preprocessing, equations, objective, parameters, seeds, and reference outputs. Confirm NumPy is declared and installed in the reproducible environment.

Separate the published model from the project's provisional directed C3-A equation; they are not interchangeable. Require small-graph tests, parameter/moment recovery where applicable, self-loop/support policy, external reproduction, runtime/memory profile, and a scalability estimate before considering a full FAFB run. The rough 12-minute-per-pass estimate for full FAFB is an estimate, not a measured benchmark; do not schedule hundreds of hours of fitting before profiling and algorithmic review.

## Priority 4 — Investigate a methodological paper only after the evidence gap is narrowed

A possible methods-paper hypothesis is that comparisons among constrained null families can be confounded by unequal state-space turnover or memory of the initial edge set, and that auditable samplers should report turnover and artifact provenance alongside structural metrics.

This is a hypothesis, not a finding or a novelty claim. Before drafting conclusions:
1. obtain comparable prospective edge-set/turnover measurements across families;
2. distinguish sampler-specific effects from differences in constraints and initial states;
3. replicate across independent seeds and at least one controlled synthetic graph family;
4. compare against relevant existing graph-randomization and mixing-diagnostic methods;
5. preserve negative results and state the limits of any turnover proxy.

Seek qualified IP advice before public disclosure if a specific implementation may be protectable. Do not delay ordinary scientific integrity or describe this note as legal advice.

## Parallel low-cost analysis — structural bridges

A separate descriptive branch may inventory cross-neuropil participation and inter-hemisphere edges from the authoritative graph, because those measurements do not depend on the rich-club residual. Keep it observational: document region/block mapping, missing labels, denominator choices, and uncertainty. Do not infer function, mechanism, or computational value without independent evidence and matched tests. Do not launch a costly workflow that competes with Run #56.

## Decision rules

- Run #57 has completed 128E; its artifact and final JSON are hashed and audited. The next decision is cross-run curve/turnover comparison, not automatic scale-up.
- Run #56 remains a historical cancelled partial checkpoint; Run #57 resumed from it and reached the cumulative target. Preserve both records for provenance.
- If no valid artifact/checkpoint is available: preserve the failure evidence and fix the artifact path/protocol before resubmitting.
- If cross-family turnover can be measured cheaply: do that before extending the same C2 chain again.
- If sensitivity controls fail calibration: repair the test design rather than escalating to full FAFB.
- If C3-A external reproduction fails: stop the scale-up and resolve the mismatch first.

## Scope boundary

No current result closes Gate C or establishes formal Markov-chain mixing, a biological mechanism, a functional advantage, novelty, patentability, market demand, or commercial value.
