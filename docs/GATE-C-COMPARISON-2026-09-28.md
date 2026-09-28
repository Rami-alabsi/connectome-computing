# Gate C — Cross-null comparison and 2026-09-28 checkpoint

## Purpose
This document records the first controlled comparison of the FAFB v783 rich-club result across three null-model families:

1. CFG — Configuration Model / نموذج التهيئة: preserves directed in-degree and out-degree sequences.
2. NPC-like — Neuropil Connection Model-like / نموذج اتصال المناطق العصبية — شبيه بـ NPC: preserves degree constraints plus source-neuropil → target-neuropil block counts.
3. Spatial — Arbor-distance hard-binned sensitivity null / نموذج الحساسية المكانية بقيود مسافة التفرعات العصبية: preserves degree sequences and the multiset of coarse source-arbor → target-arbor distance bins.

The comparison is descriptive and null-controlled. It is not a formal hypothesis test, not a mechanistic explanation, and not a claim of computational function.

## Exact comparison audit

All three artifacts were independently downloaded and inspected.

| Property | CFG | NPC-like | Spatial |
|---|---:|---:|---:|
| Dataset | FAFB v783 | FAFB v783 | FAFB v783 |
| Unique directed pairs | 3,732,460 | 3,732,460 | 3,732,460 |
| Synapse threshold | 5, after pair aggregation | 5, after pair aggregation | 5, after pair aggregation |
| Degree sweep | 20–120, step 1 | 20–120, step 1 | 20–120, step 1 |
| Null count | 100 | 100 | 4 |
| Primary constraint | in/out degree | in/out degree + neuropil block counts | in/out degree + arbor-distance bins |
| Full target reached | Yes | Yes | Yes, all 4 |
| Invariants | Passed | Passed | Passed |
| Descriptive >1.01 onset | 27 | 41 | 51 |
| Descriptive >1.01 offset | 120 | 69 | 71 |
| Peak threshold | 96 | 57 | 62 |
| Peak phi_norm | 1.057835 | 1.015171 | 1.012159 |

The observed rich-club curve itself is identical across the three artifacts: same threshold grid, rich-node counts, rich-edge counts and observed density. Therefore the differences in phi_norm arise from the null ensemble, not from changing the observed graph.

## Spatial ensemble execution record

Workflow run: 36381489805

Commit: 6eb894d6e0b0cdf8d25cf3151fb0103e4f54b403

Four seeds: 20260927, 20260928, 20260929, 20260930.

Each null targeted 3,732,460 successful swaps (one successful swap per directed edge).

| Seed | Attempts | Acceptance |
|---|---:|---:|
| 20260927 | 110,813,120 | 3.368% |
| 20260928 | 110,743,807 | 3.370% |
| 20260929 | 110,654,724 | 3.373% |
| 20260930 | 110,752,577 | 3.370% |

All four reached the target and preserved edge count, exact in-degree, exact out-degree and the complete distance-bin histogram.

Aggregate artifact: 10952943175

Aggregate artifact SHA-256: d3749483435b6b49cd1b3594748376355fa0dcd492f4734acb9f73088d60b2f4

Per-null artifacts: seed 20260927 = 10952579930; seed 20260928 = 10953710574; seed 20260929 = 10953388414; seed 20260930 = 10953700682.

The complete GitHub Actions run took about 21 minutes wall-clock. The four null jobs ran in parallel; the dominant cost is swap generation, not aggregation.

## Scientific interpretation

The three controls show a consistent attenuation pattern: CFG → NPC-like → spatial hard-binned.

The CFG result has a broad descriptive enrichment above the project's 1.01 reference line. Adding neuropil block constraints greatly reduces the enrichment. Adding the arbor-distance constraint in the current project-defined form reduces it further, leaving a smaller residual around intermediate degree thresholds.

This does not establish that space is the mechanism. The spatial model is a project-defined hard-binned sensitivity null, not a maximum-entropy fit, not an exact reproduction of Lin et al.'s NND implementation, and not a full biological generative model.

Correct wording: The observed rich-club profile retains a small residual enrichment under a degree-preserving, coarse arbor-distance-constrained null ensemble.

Do not write: space explains the rich club; biology proves the architecture; or the residual is statistically significant.

## Why the result is useful

The audit closes an important implementation concern: the observed graph and threshold grid are held fixed across the three families, so the attenuation cannot be attributed to changing the observed-data construction.

The remaining uncertainty is model choice and ensemble precision. Spatial has only 4 nulls, versus 100 CFG and 100 NPC-like nulls. Therefore the spatial residual should be treated as a first ensemble result, not as having the same precision as the 100-null controls.

## Runtime planning

The latest spatial ensemble provides an empirical runtime anchor:

- 4 spatial nulls, one swap per edge: about 21 min wall-clock with 4-way parallelism.
- 8 nulls at the same settings: approximately 40–45 min wall-clock with 4-way parallelism.
- 16 nulls: approximately 80–90 min wall-clock with 4-way parallelism.
- These are estimates, not guarantees; runner load and swap-attempt variation can change runtime.
- The workflow timeout is currently 90 minutes per job.
- A 100-null spatial ensemble is therefore not the next automatic step; it should be justified only if the 8/16-null stability check warrants it.

For any new experiment, record the estimated runtime before launch and the actual runtime afterward.

## Next experiment decision

The next operation should be a spatial ensemble stability expansion to 8 nulls, not an immediate combined NPC + spatial run.

Reason: C1 feasibility is closed; four spatial nulls all passed; the residual is small so ensemble stability matters; spatial acceptance is only about 3.37%; and the 8-null result can determine whether the peak/location and >1.01 interval are stable enough to justify the more expensive combined NPC + spatial model.

If the 8-null result is unstable, inspect the null definition before increasing the ensemble further. If stable, the next candidate is C2 — NPC + spatial / نموذج NPC + مكاني — but only after a feasibility pilot.

## Proposed C2 feasibility pilot

Before a full C2 ensemble, run a small fixed-attempt pilot rather than a full null.

Pilot goal: preserve exact in-degree; preserve exact out-degree; preserve source-neuropil → target-neuropil block counts; preserve the declared arbor-distance constraint; measure accepted swaps per 100,000 attempts; and verify no invariant drift.

No rich-club curve should be interpreted from this pilot.

Because C2 combines two hard structural constraints, its acceptance rate is unknown and may be much lower than the spatial-only 3.37%. The pilot prevents a long blind run.

## Current literature checkpoint — 2026-09-28

A fresh literature search was performed before this checkpoint.

### Salova & Kovács — Network Neuroscience, 2025
They report that spatial constraints alone do not recover broad connectome topology, while degree alone does not recover spatial structure; combined maximum-entropy models capture additional network properties beyond the constraints supplied to them. This supports keeping topology and spatial structure as separate, explicit controls. citeturn0search0

Project use: the current spatial hard-bin model remains a sensitivity/null extension. A future maximum-entropy distance model could be a separate line, not silently substituted for the current result.

### Lin & Murthy — Nature Methods, 2025
They frame connectomes as a route from circuit architecture to neural activity and behavior, while emphasizing the need for biologically realistic models of function. citeturn0search3

Project use: structural rich-club evidence is not functional evidence. Functional validation remains downstream.

### Zhang et al. — Fundamental Research, 2026
The study reports that simplified dynamical models constrained by real Drosophila network structure can reproduce studied activation patterns, and distinguishes network distance from physical distance. citeturn0search1

Project use: relevant when we eventually bridge surviving structural constraints to dynamics; it is not a reason to skip the null hierarchy.

### Li et al. — bioRxiv, 2026
A 2026 preprint fits a whole-brain model to spontaneous Drosophila activity while constraining the model with FlyWire v783 connectivity, then uses perturbations to identify a compact neuropil core and sparse hub ensemble associated with resting-state dynamics. Because it is a preprint and model-dependent, it is evidence for the structure→function research direction, not a settled architectural specification. citeturn0search4turn0search5

Project use: keep it in the evidence ledger as a recent structure→dynamics bridge and monitor for peer-reviewed revision.

## Arabic/English terminology contract

- Connectome — شبكة الوصلات العصبية
- Rich-club — نادي الوصلات الكثيفة / بنية العقد عالية الاتصال
- Degree — درجة العقدة
- In-degree — درجة الدخول
- Out-degree — درجة الخروج
- Null model — نموذج صفري / نموذج ضابط
- Configuration Model (CFG) — نموذج التهيئة
- NPC (Neuropil Connection Model) — نموذج اتصال المناطق العصبية
- Spatial constraint — قيد مكاني
- Arbor — التفرعات العصبية
- Arbor-distance — مسافة التفرعات العصبية
- Centroid — المركز الهندسي / المتوسط المكاني
- Presynaptic — قبل مشبكي
- Postsynaptic — بعد مشبكي
- Synapse — مشبك عصبي
- Directed edge — وصلة موجهة
- Degree-preserving swap — تبديل يحافظ على درجات العقد
- Distance-bin — فئة مسافة
- Rich-club density — كثافة نادي الوصلات الكثيفة
- phi_norm — كثافة النادي مُطبّعة على النموذج الصفري
- Feasibility — قابلية التنفيذ
- Sensitivity control — ضابط حساسية
- Maximum-entropy model — نموذج أقصى إنتروبيا
- Structure→function — من البنية إلى الوظيفة
- Functional validation — التحقق الوظيفي

English terminology remains in code, filenames and formal scientific identifiers; Arabic translations are explanatory and do not replace the formal names.

## Gate state after this checkpoint

- Gate A — CLOSED.
- Gate B — CLOSED for the defined 100-null NPC-like v783 benchmark.
- Gate C0 — CLOSED for authoritative arbor-aware data definition and coverage.
- Gate C1 feasibility — CLOSED.
- Gate C spatial rich-club ensemble — first 4-null result validated.
- Gate C overall — OPEN pending ensemble stability and stronger spatial-model comparison.
- C2 NPC + spatial — NOT STARTED.
- Functional/computational validation — downstream.


## 8-null stability update

The 8-null spatial ensemble (run 36386665317) completed with all 8 nulls valid.

- onset >1.01: 51
- offset >1.01: 71
- peak threshold: 62
- peak phi_norm: 1.012082112699241
- all invariants preserved
- successful swaps/null: 3,732,460
- acceptance rates across seeds: approximately 3.368%–3.374%

The 4-null result was independently re-aggregated from its four original null artifacts after the aggregator metadata update; it reproduced peak degree 62 and peak phi_norm 1.0121585259506658, with onset 51 and offset 71.

Thus the main qualitative spatial result is stable when expanding from 4 to 8 nulls: the >1.01 interval remains 51–71 and the peak remains at degree 62. The peak amplitude changes by about 0.0000764.

This strengthens the claim of ensemble stability for this project-defined null, but does not provide a formal significance test or establish a biological mechanism.

## C2 feasibility pilot active

Run 36393368885 is testing a combined null move set that preserves:
- directed in-degree;
- directed out-degree;
- source-neuropil → target-neuropil block counts;
- coarse arbor-distance-bin histogram;
- no self-loops or duplicate directed pairs.

The pilot uses 100,000 attempted swaps and reports feasibility only. No rich-club interpretation is allowed.


## 2026-09-28 — Spatial 8-null standardized-residual audit

The existing 8 spatial null artifacts from Run `36386665317` were re-aggregated without generating any new null graph. For each degree, the aggregator now records the null mean, sample SD, normalized observed/null ratio, and the descriptive standardized residual:

`(observed rich-club density - null mean density) / null SD density`.

Key values:
- degree 62: `phi_norm = 1.012082112699241`, null SD = `1.9387922455161827e-07`, standardized residual = **88.6667**;
- degree 57: `phi_norm = 1.011612176027949`, standardized residual = **68.3294**;
- degree 71: `phi_norm = 1.0100282904400153`, standardized residual = **38.5167**;
- degree 93: `phi_norm = 1.0029680243648245`, standardized residual = **6.8186**;
- degree 120: `phi_norm = 0.9776608134065369`, standardized residual = **-32.1668**.

The maximum absolute standardized residual occurs at degree 32 (139.49), where `phi_norm` is only 1.00772 and therefore below the project's descriptive 1.01 line.

**Interpretation rule:** these standardized residuals quantify separation from the eight realized null samples; they are **not p-values, not formal significance tests, and not evidence that the null ensemble has converged to a population variance estimate**. The very small null SDs make the standardized residual numerically large. This is precisely why ensemble size, sampler mixing and null-model choice must remain separate from any significance claim.

The result does answer the immediate feasibility question: the spatial residual is not simply an artifact of visible null-to-null amplitude noise in these eight samples. C2 therefore remains scientifically justified because the unresolved question is the **joint** NPC + spatial constraint, not whether either constraint alone can attenuate CFG enrichment.

## 2026-09-28 — C2 feasibility result and runtime decision

The corrected C2 feasibility pilot was executed against the authoritative Princeton C0 artifact.

### Baseline kernel
Run `36396525136`, artifact `10958119130`:
- 100,000 attempts; 1,168 accepted; acceptance = 1.168%.
- 9,869 edges without complete NPC block assignment were frozen.
- All edge-count, in/out-degree, block-pair, distance-bin, self-loop and duplicate invariants passed.
- Pilot step runtime ≈78.1 s.

A direct extrapolation would require ≈319.6 million attempts for one 3,732,460-successful-swap null, or roughly 69 h at the measured attempt throughput. No ensemble was launched.

### Optimized proposal kernel
Run `36396805573`, commit `8fd9f6ad8ca6765a5ed1d60d602ff131a86a7f1c`, artifact `10958720816`:
- 100,000 attempts; 9,789 accepted; acceptance = **9.789%**.
- 0 block rejections because proposals are sampled within fixed source-block -> target-block classes.
- 86,453 distance-bin rejections and 3,758 invalid/duplicate/self-loop rejections.
- All declared invariants passed.
- Pilot step runtime ≈86.6 s.

The proposal-kernel optimization changes how candidate pairs are proposed, not the declared C2 constraints. It is therefore an implementation/runtime optimization, not a new scientific null definition. However, the resulting full-null runtime is still too high for the current Python runner (~8 h/null by simple extrapolation).

**Decision:** C2 joint feasibility is established, but full C2 ensemble execution remains blocked on sampler/runtime optimization. Do not weaken the distance-bin or NPC block constraints to make the experiment faster.


## Runtime refinement after bucket-lookup fix

Run `36396814001` (commit `d12c4ca05310f6ab41fca94237afcd2c461c98af`) repeated the optimized C2 pilot after removing an avoidable per-attempt bucket-key lookup. The acceptance rate remained exactly 9.789% and all invariants remained exact. The pilot computation step decreased to approximately 55.2 s. Linear extrapolation gives approximately 6 h per 3,732,460-successful-swap null on this runner.

This confirms the remaining bottleneck is the Python constrained-swap kernel rather than the proposal bookkeeping alone. Full C2 ensemble execution remains blocked pending a faster exact implementation.
