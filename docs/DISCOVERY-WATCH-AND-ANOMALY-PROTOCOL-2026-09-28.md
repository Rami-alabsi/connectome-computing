# Discovery Watch / Anomaly Protocol

## Purpose

The project is not only a confirmatory test of a preselected rich-club hypothesis. It is also an exploratory instrument for detecting unexpected, internally coherent structure in the FlyWire FAFB v783 connectome.

Unexpected results must be treated as **signals to investigate**, not as discoveries by default.

This protocol is deliberately added so that a surprising result is not discarded merely because it is inconvenient for the current hypothesis, while also preventing post-hoc pattern hunting from being mistaken for confirmation.

## Core principle

**Unexpected ≠ wrong, and unexpected ≠ true.**

An anomaly earns escalation when it survives progressively stronger controls.

Exploratory findings can legitimately generate new hypotheses, but confirmatory interpretation must be separated from the exploratory stage. This distinction is important because post-hoc hypothesis formation without independent testing can inflate false discoveries.

## What counts as a discovery signal?

Flag results that are:

1. unexpected under the current model or null;
2. large enough to be practically interesting, not merely numerically nonzero;
3. reproducible across independent seeds/runs where appropriate;
4. robust to reasonable implementation and preprocessing checks;
5. not explained by a known artifact, degree effect, spatial sampling bias, annotation incompleteness, or null-model weakness;
6. connected to a measurable structural or dynamical feature;
7. capable of generating a falsifiable follow-up experiment.

Especially important are **direction reversals**, **sharp thresholds**, **unexpected scaling laws**, **localized anomalies**, **constraint-dependent phase changes**, **unexpected null acceptance behavior**, and **relationships between observables that were not part of the original hypothesis**.

## Current high-priority anomaly candidates

### 1. Spatial standardized residuals

The 8-realization spatial null audit produced very large standardized residuals at some degrees because the realized null-to-null SD was extremely small.

These are **not p-values** and are not yet evidence of significance. The possibility that the sampler's realized variance is too small because of incomplete mixing must be resolved first.

Nevertheless, the phenomenon itself is worth preserving as a discovery signal:

> Does the combination of degree-preserving + arbor-distance-preserving constraints produce an unusually narrow reachable ensemble around the observed rich-club curve?

If yes, this may reveal something about the geometry of the constraint surface or sampler dynamics rather than merely a rich-club effect.

Required follow-up: C2 joint NPC + spatial null ensemble, independent seeds, acceptance trajectory, mixing diagnostics, and comparison of null-to-null variance across constraint surfaces.

### 2. C2 acceptance structure

The 1M C2 feasibility benchmark accepted 94,751/1,000,000 proposals (9.4751%), with 867,194 distance-bin rejections and zero block rejections after block-pair stratification.

This is currently a runtime/feasibility observation, not a biological result.

However, the strong asymmetry between block-pair eligibility and distance-bin rejection should be retained as a possible clue about the interaction between mesoscale block structure and fine spatial geometry.

Required follow-up: full C2 chain; record acceptance trajectory rather than only the aggregate rate; compare early/mid/late acceptance; test whether acceptance declines, stabilizes, or changes regime as the graph moves through the joint constraint surface.

### 3. Constraint hierarchy

The observed rich-club curve survives CFG and NPC-like controls descriptively, and the spatial null also shows a stable >1.01 regime. The next scientifically important question is whether the residual changes qualitatively under the **joint** constraint.

Do not pre-decide the direction. Possible outcomes include:

- residual largely disappears;
- residual persists with similar shape;
- residual changes threshold/peak;
- residual splits into multiple regimes;
- residual reverses;
- the null ensemble itself becomes unusually narrow or structured.

Each outcome is informative and should be documented before interpretation.

## Escalation ladder

**Signal → artifact verification → independent rerun → stronger null → alternative explanation → preregistered/locked follow-up → external or held-out validation**

No anomaly is promoted to a discovery claim without passing the relevant levels.

## Anti-self-deception rules

- Never choose a threshold because it makes the result look interesting after seeing the result.
- Never call an exploratory standardized residual a p-value.
- Never convert a rich-club residual directly into a mechanism claim.
- Never silently change the null to rescue or destroy an effect.
- Preserve failed and superseded runs.
- If a surprising result suggests a new hypothesis, record the hypothesis and the exact observation that generated it before running the next confirmatory test.
- Prefer independent seeds, held-out observables, or an independently constructed control when practical.

## Discovery ledger fields

Every escalated anomaly should record:

- observation;
- exact artifact/run;
- dataset/version;
- code commit;
- parameter set;
- null/control;
- expected behavior;
- observed behavior;
- effect size;
- uncertainty/ensemble size;
- possible artifact explanations;
- competing explanations;
- prior-art status;
- falsifiable hypothesis;
- next test;
- outcome;
- final disposition: artifact / expected / unresolved / robust anomaly / new finding.

## External science watch

Recent literature makes the exploratory route particularly relevant to this project. A 2026 analysis of more than 750 major discoveries argues that many apparently serendipitous discoveries were enabled by new methods/tools that exposed observations not previously accessible. The methodological lesson for this project is not to chase surprises blindly, but to build analyses that make unexpected structure visible while keeping the confirmation boundary explicit.

A recent 2026 FlyWire-v783-constrained modeling preprint is also relevant because it reports an unexpected-to-the-original-model organizational result: spontaneous activity in its fitted model was concentrated around a compact neuropil core and sparse brain-spanning inhibitory hub ensemble. This is model-dependent evidence, not validation of the present project, but it is a useful external comparator for later structure→function work.

## Decision rule

If C2 produces a surprising result, **pause before interpreting it**. First create the smallest artifact that can distinguish:

1. implementation bug;
2. sampling/mixing artifact;
3. null-model consequence;
4. known biological/network property;
5. genuinely new structural observation.

Only after that classification should the project decide whether the result deserves a new hypothesis branch.

