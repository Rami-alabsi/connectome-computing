# Research Discovery, Prior-Art, and Value Strategy
## Dated operating protocol — 2026-10-12

This document supplements (does not replace) `docs/MASTER-COMPASS-2026-10-12.md`. It defines how to search for unexpected results, avoid duplicating prior work, and test whether any validated result has scientific or commercial value.

## Mission

Find a defensible, reproducible result or method that is genuinely differentiated and could eventually support a useful product, license, investment, or intellectual-property strategy. A major discovery is an aspiration, not a result currently established. No claim of patentability, market demand, or million-dollar value is made here.

## Non-negotiable evidence ladder

For every surprising observation, preserve this chain:

1. **Observation:** exact metric, code/data version, run ID, seed, artifact, and uncertainty.
2. **Integrity:** independently verify artifact contents, fingerprints, constraints, tests, and data provenance.
3. **Reproduction:** repeat across independent seeds and, where appropriate, an independent implementation or dataset.
4. **Nulls and controls:** test whether the effect is explained by degree, spatial embedding, block structure, weights, sampling, preprocessing, or the statistic itself.
5. **Sensitivity:** change reasonable thresholds, binning, parameter choices, and assumptions; report failures and negative results.
6. **Mechanism:** propose an explanation only after the effect survives controls; distinguish post-hoc interpretation from a preregistered prediction.
7. **Function:** test whether the structural property improves a named task, against strong baselines and matched compute/data budgets.
8. **Novelty:** compare the precise method/result against papers, preprints, open-source projects, patents, and adjacent fields.
9. **Value:** identify a real customer/user, costly problem, measurable advantage, deployment requirements, and plausible route to adoption.
10. **Protection and disclosure:** before public disclosure of a potentially patentable implementation, obtain qualified IP advice for relevant jurisdictions. This document is not legal advice.

A high correlation between curves, low overlap, a long run, or an unusual plot is not by itself proof of convergence, biological mechanism, novelty, function, or commercial value.

## Current C2 interpretation guardrail

C2 is an exact-constraint null-model feasibility/sampling study, not yet a product or a demonstrated computational invention. Run #55's same-chain curve remains systematically drifting across turnover levels despite very high curve correlation; the overlap statistic is a turnover/memory diagnostic, not a convergence proof. Run #56 (128E continuation) must be audited before any next long run. Do not use C2 sampling behavior as evidence for a new architecture or commercial advantage without a separate functional experiment.

## Prior-art reconnaissance — first-pass sources checked 2026-10-12

This is a targeted first-pass scan, not an exhaustive literature review, freedom-to-operate opinion, or patentability search. Search terms and adjacent fields must be expanded as each specific hypothesis becomes testable.

1. **Milisav et al., “A simulated annealing algorithm for randomizing weighted networks,” Nature Computational Science (published 2024; journal volume 2025).** Discusses connectome null models, preserving weighted degree/strength, and sampling biases of degree-preserving rewiring. This means generic claims about better connectome randomization or preserving common graph constraints need a precise comparison and cannot be presumed novel.
   - https://www.nature.com/articles/s43588-024-00735-z
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC11774763/

2. **“Combined topological and spatial constraints are required to capture the structure of neural connectomes” (2025).** Examines degree and spatial/wiring constraints and their joint explanatory role across neural connectomes. This is close prior art for broad claims that both topology and spatial constraints matter.
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC11949549/

3. **“Connectome-Guided Optimization for Deep Networks,” AISTATS/PMLR (2026).** Uses a functional connectome of neural-network co-activations to adjust learning rates. Broad connectome-guided optimization is therefore an active research area; any proposed idea needs a narrowly specified differentiator and direct baselines.
   - https://proceedings.mlr.press/v300/he26b.html

4. **“Connectome-based reservoir computing with the conn2res toolbox,” Nature Communications (2024).** Demonstrates connectome-informed reservoir computing and comparisons with rewired null networks. Generic claims that connectomes can inform computational reservoirs or that their topology can affect task performance are not new by themselves.
   - https://doi.org/10.1038/s41467-024-44900-4

5. **US12050991B1, “Connectomics-based neural architecture search,” assigned to Google LLC; granted 2024.** Describes using biological connectomics/motifs to constrain neural-architecture search. This is a concrete patent-landscape warning: do not treat “derive AI architectures from connectomes/motifs” as an unoccupied invention category.
   - https://patents.google.com/patent/US12050991B1/en

6. **“Geometric constraints on the architecture of mammalian cortical connectomes,” Cell (2026).** Proposes resonant geometric modes as a model for mammalian cortical connectome architecture across species. It is recent adjacent work; geometry-based explanations or generative claims require direct comparison.
   - https://www.sciencedirect.com/science/article/pii/S0092867426006483

These sources do not establish that the project's exact C2 constraint combination or any future method is already published or patent-protected. Conversely, failure to find an exact match in this first pass would not establish novelty. Check supplements, code, citations, preprints, claims, priority dates, jurisdiction, and patent family before drawing stronger conclusions.

## Candidate discovery directions — hypotheses only, not findings

### A. Constraint trade-off and sampler diagnostics
Test whether the exact combination of degree sequence, block-pair counts, and distance-bin histogram creates a distinctive feasible-state geometry or mixing bottleneck. Compare against carefully named alternative samplers/null families, synthetic graphs with known ground truth, and independent chains. Possible value would be a reliable validation/diagnostic tool for constrained network randomization—not a claim that current C2 behavior itself is novel.

### B. A practical “constraint compiler” for graph null models
Explore whether a reusable tool can accept a declared constraint set, detect incompatible/redundant constraints, generate valid proposals, audit invariants, estimate mixing diagnostics, and emit reproducible evidence bundles. This is only a product hypothesis. Survey existing graph-randomization, statistical-physics, and network-science software before implementation; demonstrate measurable advantages in correctness, runtime, diagnostics, or reproducibility.

### C. Constraint attribution for downstream computation
If and only if residual structure survives C2 and matched controls, test whether selected structural constraints improve a concrete computational task. Use biological and non-biological baselines, matched parameter count/compute/data, ablations, multiple tasks, and held-out evaluation. Connectome-derived AI architectures are crowded prior art and patent-sensitive; no generic architecture claim should be made.

### D. Multi-scale residual signatures
Test whether a reproducible signature survives a hierarchy of increasingly realistic null models and remains stable across seeds, thresholds, data versions, and relevant neuron/region subsets. Avoid post-hoc metric fishing: define the metric family and correction strategy before looking at confirmatory outcomes. A signature is only a biological discovery candidate after robust replication and expert review.

### E. Data-quality and provenance-aware network inference
Explore whether explicit handling of uncertain labels, frozen/unclassified edges, synapse thresholds, and spatial-coordinate uncertainty materially changes inference. Quantify uncertainty rather than hiding it. A useful deliverable could be an auditable pipeline, but novelty and demand must be independently established.

## How to evaluate unexpected results

For each surprising result, create a dated record with:
- a one-sentence observation and a separate hypothesis;
- exact source commit, workflow/run/job IDs, dataset/version, parameters, seeds, artifact IDs and hashes;
- expected result under each competing explanation;
- the smallest discriminating experiment;
- nulls, controls, multiple-comparison risk, and stopping rule;
- independent replication status;
- literature and patent search terms, date, sources, and closest prior art;
- what would falsify the hypothesis;
- functional benchmark and commercial user/problem, if applicable;
- a decision: discard, replicate, investigate, or advance.

Maintain a “negative results” record too. Do not silently drop failed approaches or redefine success after seeing the data.

## Commercial-value gate

Before investing heavily in a product direction, require at minimum:
- a specific user/customer and costly workflow/problem;
- evidence that the problem exists beyond our intuition (interviews, usage data, or documented demand);
- a measurable advantage over the strongest practical alternative;
- reproducible results and a deployment/cost model;
- an initial IP and licensing review;
- a clear distinction between open-source publication, paid software/service, data/analytics licensing, and patent strategy.

Potential market value is not inferred from scientific novelty alone. Patentability, freedom to operate, ownership, and commercial rights require qualified professional review.

## Immediate operating rules

1. Finish and audit active Run #56 before spending more Actions quota on long C2 jobs.
2. Independently download and inspect the final Run #55 and #56 artifacts when available; a workflow log or recorded checksum is not a substitute for inspecting artifact contents.
3. Keep C2 mixing/convergence claims open until supported by appropriate sampling diagnostics and independent chains.
4. Do not launch the C2 sensitivity ladder until the active run is audited and compute budget is clear.
5. Expand prior-art search for each concrete method, including terms from statistics, graph sampling, combinatorial optimization, neuroscience, AI architecture search, and patents.
6. Update this document with dated, sourced findings—not unsourced declarations that a search was “complete.”
