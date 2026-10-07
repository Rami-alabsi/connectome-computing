# MASTER COMPASS — Connectome Computing
## Authoritative handoff snapshot — 2026-10-06

> This file is the current operational compass for continuing the project.
> It supplements the historical experiment ledger in `docs/PROJECT-STATUS.md`.
> Do not erase historical entries merely because later work supersedes them.

## 1. Mission

Explore whether biological connectome structure can reveal computational principles that remain useful after abstraction, controlled reconstruction, matched ablations, and scaling.

Core rule:

**biology is evidence, not specification.**

The project is not allowed to jump directly from a biological observation to an architecture or product. The required chain is:

**evidence → abstraction → falsifiable prediction → matched control → implementation → execution → ablation → scaling → prior-art recheck**

Unexpected results are discovery signals, not automatic discoveries.

## 2. Dataset / canonical graph

Primary biological source:
- FlyWire FAFB v783
- authoritative Princeton synapse table
- pair-level aggregation before graph analysis
- minimum synapse threshold for the main rich-club/NPC/C2 path: 5
- unique directed pairs: **3,732,460**
- graph nodes in the accepted connection table: **138,584**
- raw Princeton connection-table rows: **80,215,790**
- raw edge rows in the broader analyzed table: **5,342,446**
- multi-region pair rows: **1,609,986**

C0 authoritative spatial definition:
- workflow run **36315995364**
- artifact **10930278435**
- outgoing/incoming arbor-centroid coverage: 100%
- observed-edge median arbor distance: 481,001 nm
- sampled non-edge median: 2,281,970 nm
- anisotropic scale: 4/4/40 nm
- spatial distance bins:
  0–25k, 25–50k, 50–100k, 100–200k, 200–500k,
  500k–1M, 1–2M, 2–5M, 5–10M, >10M nm

The lighter `synapse_coordinates` spatial path is secondary/superseded for primary C0 work.

## 3. Gate state — current truth

| Gate | State | Meaning |
|---|---|---|
| Gate A / CFG | **CLOSED** | Defined v783 degree-preserving rich-club control completed |
| Gate B / NPC-like | **CLOSED** | Defined 100-null v783 NPC-like control completed |
| C0 spatial data | **CLOSED** | Authoritative Princeton arbor geometry/coverage validated |
| C1 spatial feasibility | **CLOSED** | Degree + distance-bin feasibility validated |
| Spatial 4-null | **VALIDATED** | First ensemble |
| Spatial 8-null | **STABLE** | Expanded seed ensemble gave same qualitative descriptive curve landmarks |
| C2 joint NPC + spatial | **ARTIFACT-COMPLETE #1** | One full null is complete with final graph-derived rich-club curve and exact invariants; ensemble/mixing remain open |
| Gate C / biological closure | **OPEN** | Must not be closed before C2 ensemble + mixing/sensitivity work |
| Structure → function | **BLOCKED downstream** | Intentionally waiting for stronger biological controls |
| Computational architecture claim | **NOT ESTABLISHED** | No benchmark advantage/novelty claim yet |
| Commercialization | **RESEARCH ONLY** | No validated product/IP advantage yet |

## 4. Gate A — CFG

100 deterministic CFG nulls were completed.

Authoritative ensemble:
- run **35987597540**
- commit **f53f471de27f0c8cf58d496dcc0885ecfa6a8d4a**
- artifact **10807064530**
- 100/100 nulls reached 3,732,460 successful swaps
- exact edge count, in-degree and out-degree preserved
- descriptive `phi_norm > 1.01`: degree 27 through 120
- peak `phi_norm = 1.057835` at degree 96

Interpretation:
- stable CFG-controlled enrichment under this project's v783 method
- not an exact reproduction of Lin et al. 2024
- does not distinguish NPC/spatial explanations

## 5. Gate B — NPC-like

Definition:
- dominant outgoing-synapse neuropil/block assignment
- degree-preserving swaps
- exact source-block → target-block pair counts

100-null v783 benchmark is CLOSED.

Important wording:
- call it **NPC-like v783**, not exact v630 reproduction
- exact invariants passed
- this control substantially attenuates the CFG rich-club residual but does not settle the joint spatial question

Representative historical benchmark:
- run **36057032102**
- artifact **10836101656**
- 8-null benchmark: 3,732,460 successful swaps/null
- 3,648 block-pair categories preserved
- descriptive >1.01 region around degrees 41–69

The authoritative status is the later 100-null Gate B closure recorded in project history.

## 6. C0 / C1 spatial work

C0 is the authoritative Princeton geometry path described above.

C1 established that exact distance-bin preservation is feasible while preserving:
- edge count
- in-degree
- out-degree
- distance-bin histogram

The earlier lightweight centroid artifact was superseded for primary use.

## 7. Spatial 8-null stability

Workflow **36386665317**:
- 8/8 nulls completed
- each: 3,732,460 successful swaps
- exact edge count/in-degree/out-degree/distance-bin preservation

4-null → 8-null landmarks:
- >1.01 onset: 51 → 51
- >1.01 offset: 71 → 71
- peak degree: 62 → 62
- peak phi_norm: 1.0121585 → 1.0120821

Interpretation:
**stable across the expanded seed ensemble**, not a formal significance result.

A standardized-residual audit gave very large z-like values because realized null-to-null SD was extremely small. These are **not p-values**. The important open question is whether the narrow variance reflects a genuinely narrow constrained ensemble or incomplete/slow mixing.

## 8. C2 — the central current problem

### Scientific purpose

C2 asks:

> Does the rich-club residual survive when BOTH the NPC-like mesoscale block constraint AND the arbor-distance-bin spatial constraint are imposed simultaneously?

This is the key unresolved biological control.

### Exact C2 constraint surface

Every C2 realization must preserve:
1. exact directed edge count;
2. exact in-degree sequence;
3. exact out-degree sequence;
4. exact source-block → target-block edge counts for edges with complete block assignment;
5. exact global arbor-distance-bin histogram;
6. no self-loops;
7. no duplicate directed edges.

Edges without complete dominant block assignment are **FROZEN**, not deleted.
Current frozen count: **9,869**.

All edges still participate in the global distance-bin histogram.

### Proposal kernel

Current kernel:
- proposals are stratified inside fixed source-block → target-block classes
- candidate pairs are sampled from precomputed block buckets
- distance-bin equality is checked after proposing the two rewired edges
- the proposal kernel changes efficiency, not the declared C2 constraint surface

Important:
Do NOT silently replace the primary C2 null with a stronger block-pair × distance-bin-preserving null. Such a stronger null may be useful later as a sensitivity analysis, but it is a different ensemble.

## 9. C2 feasibility/runtime history

Corrected baseline:
- run **36396525136**
- 100k attempts
- 1,168 accepted
- 1.168%
- 9,869 frozen edges
- all invariants passed
- ~78.1 s

Block-pair-stratified optimization:
- run **36396805573**
- commit **8fd9f6ad8ca6765a5ed1d60d602ff131a86a7f1c**
- 100k attempts
- 9,789 accepted = 9.789%
- zero block rejections
- all invariants passed
- ~86.6 s

Bucket lookup optimization:
- run **36396814001**
- commit **d12c4ca05310f6ab41fca94237afcd2c461c98af**
- same 9,789 accepted / 100k
- ~55.2 s
- projected roughly 6 h/null on that runner

Full C2 realization #1:
- run **36418874492**
- commit **ecac77ad658905e24990f35d1a5a34f389fe983d2**
- target 3,732,460 accepted swaps
- attempts **55,361,441**
- acceptance **6.7419849%**
- frozen **9,869**
- all declared invariants passed
- artifact ID **10968562956**
- ZIP SHA-256 **70549dbe9e0082e710c0b4521b7c94cc01714e842c17b787cee2cbef5b0f8093**

Critical limitation:
That historical artifact stored metadata/checkpoints but **not the final graph**. Therefore it proves feasibility of one C2 realization, but it cannot be used as the artifact-complete C2 rich-club result.

Do not accidentally call this a completed C2 scientific result.

## 10. C2 checkpoint/resume engineering

The long-run problem was infrastructure, not evidence.

Important historical failures:
- 180 min then 350 min workflow timeout
- old checkpoints were in-memory only
- a timer bug compared absolute `perf_counter()` to relative elapsed time
- full-state gzip serialization is expensive
- resume initially duplicated large graph structures and pushed RSS high
- diagnostic traces and GC hypotheses were tested
- resume path was ultimately shown to execute real attempts beyond 55M

Checkpoint state contains:
- version
- seed
- code_version
- constraint_fingerprint
- attempt
- accepted
- rejection counters
- edge_list
- edge_bins
- RNG state
- checkpoints

Checkpoint writes are atomic temp-file → replace.
Compression default was reduced to gzip level 1 for recovery speed.

The current final-completion workflow disables time-based full-state checkpoints by setting:
`--checkpoint-seconds 1000000000`
and retains 5M-attempt checkpoints.

## 11. The 55M resume checkpoint

Authoritative resume source:
- original run **36586932202** (#19)
- artifact **11061616207**
- artifact name `fafb-v783-c2-feasibility-60000000`
- artifact digest:
  **sha256:18b0048234e0d99c23bc8ab2a2d2479aabc37eac52f27bc53666a5d5293a93ef**
- checkpoint:
  - attempt **55,000,000**
  - accepted **3,710,356**
  - acceptance **6.7461%**

Run #22 confirmed the checkpoint could be loaded and resumed.
Run #23/24/25/26 investigated apparent stalls.
Compact buckets, GC disabling, and detailed traces were tested.
A lightweight probe later proved the resumed loop can execute 100k attempts beyond 55M.

A diagnostic run reached:
- 55.1M → **3,716,517 accepted**
- 55.2M → **3,722,609 accepted**
- 55.3M → **3,728,657 accepted**

Thus the resume path is real and deterministic enough to continue the same realization.

## 12. C2 finalization issue

C2 now computes a rich-club curve from:
- original observed graph
- final null graph

The rich-club implementation was optimized from repeated full edge scans to a mathematically equivalent sorted-edge-cutoff method.

Commits:
- **74ae52858fd81e5e03dace6a512fd7fa160d0e73** — optimization
- **d139ba1e93e561c6986c6037d352c0d650034f4c** — equivalence test
- **5f3b42f6bcd1fc2c556dd3623f280234b091ed56** — fixed missing `Counter` and `bisect` imports

The latest push CI for the 100-null workflow on **5f3b42f...** succeeded.
Run **37415968989** (#41) was cancelled after ~32 minutes. It produced a recovery artifact before cancellation:
- artifact **11392495820**
- name `fafb-v783-c2-feasibility-55000020`
- SHA-256 **5d0cbb46f9080edbbb158bd5d5a05ee08102f4327574d7cce348ee28200b6a73**
- this artifact is the checkpoint/result from attempt **55,000,020** with accepted **3,710,357**.

This is not a scientific null result; it is a recovery checkpoint. It is useful because it is newer than the 55M checkpoint and was produced after the rich-club import fix.

Do not treat run #41 as a scientific C2 result.

## 13. Why the project appeared to “freeze”

There were several distinct phenomena; they must not be conflated:

1. **Real sampler execution:** proved by the 55.1M/55.2M/55.3M probes.
2. **Full-state checkpoint serialization:** can be slow and previously obscured progress.
3. **Finalization:** after reaching `args.attempts`, the program may spend time computing final degree maps, converting edge sets, rich-club curves and preservation checks.
4. **Workflow cancellation:** a 350-minute timeout can kill a job without indicating a scientific failure.

Therefore:
**“GitHub log stopped changing” is not itself evidence that the C2 sampler is scientifically or algorithmically stuck.**

Use `skip_finalization=true` for diagnostic runs when isolating the sampling loop.

## 14. Exact next C2 sequence

Do not restart from zero.

### Step C2-A — build a clean 55.3M recovery checkpoint
Use the newer Run #41 artifact as the resume source first. Run a diagnostic with:
- attempts = **55,300,000**
- target_accepted = 0
- resume_run_id = **37415968989**
- resume_artifact_name = **fafb-v783-c2-feasibility-55000020**
- skip_finalization = **true**
- trace_attempts = 0 for normal run

Expected state from the observed diagnostic:
- attempt 55,300,000
- accepted about **3,728,657**

Treat this as a continuation checkpoint, not a new scientific null.

### Step C2-B — finish the same realization
Resume from the 55.3M checkpoint and run until:
- target_accepted = **3,732,460**
- time-based checkpoint disabled
- preserve exact seed **20260935**
- preserve constraint fingerprint
- do not alter proposal kernel or constraints

Expected remaining accepted swaps from the observed 55.3M point:
**3,803**.

### Step C2-C — inspect final artifact
Require:
- target_reached = true
- accepted_swaps = 3,732,460
- exact all invariants true
- no self loops/duplicates
- complete rich-club curve
- original-edge-overlap fraction
- exact checkpoint/provenance metadata
- artifact hash

Only then call it an **artifact-complete C2 realization**.

### Step C2-D — independent C2 seeds
One realization is not enough.
Then run independent seeds, preserving the same constraint surface.
Record:
- acceptance trajectory
- early/mid/late acceptance
- null-to-null rich-club variation
- mixing diagnostics
- overlap/turnover
- convergence sensitivity

### Step C2-E — stronger spatial sensitivity
After primary C2 is stable, test stronger spatial/max-entropy variants separately.
Do not replace the primary C2 definition.

## 15. C2 interpretation decision tree

After independent C2 nulls:

### Outcome 1 — residual disappears
This supports the explanation that the CFG/NPC residual can be accounted for by joint mesoscale + spatial constraints.

### Outcome 2 — residual persists
This makes a stronger structure-specific residual interesting, but still not a mechanism.
Proceed to matched computational ablations and prior-art review.

### Outcome 3 — peak/onset/shape changes
Treat the shape change itself as a possible discovery signal.

### Outcome 4 — null ensemble is extremely narrow
Investigate mixing and constraint-surface geometry before interpreting the biological residual.

### Outcome 5 — residual reverses
High-priority anomaly. Verify implementation, independent seeds, and alternative null explanations before interpretation.

## 16. Discovery watch

High-priority existing anomaly:
- spatial null standardized residuals can be huge because null SD is tiny
- this is not a p-value
- possible interpretations include narrow constrained ensemble or incomplete mixing

High-priority C2 anomaly:
- block-pair stratification removes block rejection while distance-bin rejection dominates
- this may reveal interaction between mesoscale organization and geometry
- currently it is a runtime/feasibility observation, not a biological discovery

Protocol:
**signal → artifact verification → independent rerun → stronger null → alternative explanation → locked follow-up → held-out/external validation**

Never retrofit a hypothesis to a surprising result and then call it confirmation.

## 17. RSS / M6 branch

M6/RSS is a parallel computational research branch, not the current biological Gate-C blocker.

Important:
- earlier 6,720-row RSS results before semantic correction are invalid for scientific interpretation
- corrected C/D ranks the full candidate pool under matched route budget
- H is shuffled-context null
- I is shuffled-collective null
- seed is the replication unit, not timestep
- current design is a bounded collective-pooling surrogate, not a general higher-order interaction claim

Do not use RSS benchmark results to bypass unresolved biological controls.

## 18. Computational architecture branch

Long-term spine:

**biological structure → structural abstraction → bounded resources → effective state → relational coordination → dynamics → benchmark → ablation → scaling**

The project already contains prototypes for:
- modular/sparse/hierarchical/spatial generators
- capacity-triggered hierarchy
- effective-state interface
- bounded higher-order coordination
- local-plus-interface dynamics
- state-dependent routing
- dynamic relational layering
- field-mediated relational layer
- controlled RSS benchmarks

But these are prototypes until the biological evidence and matched computational ablations support a specific abstraction.

## 19. Prior art / novelty boundary

Known prior art includes:
- FlyWire whole-brain connectome
- whole-brain network/rich-club analysis
- connectome-derived computational processing units
- Loihi 2 fly-connectome implementation
- connectome-constrained neural models
- generative biological-network models

Do NOT claim novelty merely because the project:
- uses FlyWire
- measures graph statistics
- builds modular graphs
- maps motifs to primitives
- benchmarks connectome-derived networks
- mentions human brain scaling

Potentially distinctive territory requires:
1. multiple biological constraints;
2. scalable synthetic generation;
3. separation of biological constraints from generic graph priors;
4. matched ablations;
5. reproducible workload advantage;
6. scaling evidence;
7. targeted prior-art search.

## 20. Commercialization boundary

The commercial asset, if it emerges, is likely to be:
- algorithm
- computational abstraction
- generator
- runtime/compiler
- benchmark/tooling
- optimization/IP

Not the third-party biological dataset itself.

Current commercial state:
**research asset only**.
No validated computational advantage, product-market fit, patentability, or commercial data clearance has been established.

## 21. Rules for the next AI/person

1. Read this file first.
2. Read `docs/AI-CONTEXT.md`.
3. Read the relevant experiment record before changing code.
4. Never invent an artifact/result.
5. Never restart C2 from zero when a valid checkpoint exists.
6. Never change the C2 constraint surface merely to improve runtime.
7. Treat infrastructure failures separately from scientific failures.
8. Preserve failed/superseded runs.
9. Every scientific claim must point to an executed artifact/run.
10. Update documentation in the same change window as a gate-state change.
11. Keep exploratory discovery and confirmatory testing separate.
12. Do not build the computational architecture around an unclosed biological interpretation.

## 22. One-line compass

**We are NOT trying to prove that a fly is a computer. We are testing whether carefully isolated biological constraints survive as useful computational principles after stronger null controls, ablations, and scaling.**

Current immediate objective:

**Finish artifact-complete C2 on the same 20260935 realization → independent C2 seeds → mixing/sensitivity audit → Gate C decision → only then structure→function and computational abstraction.**

## 23. C2 Run #44 finalization root cause (2026-10-07)

Run #44 (GitHub Actions run `37457876685`) was cancelled after 5h50m. The sampler itself is not the demonstrated bottleneck:
- Run #43 resumed the identical checkpoint at attempt 55,300,000 / accepted 3,728,657 and reached the target 3,732,460 at attempt 55,361,441 in ~0.45 s after entering the loop.
- The absence of `performance_probe` lines in #44 is therefore not evidence of a sampling stall: probes are emitted every 100,000 attempts, while only 61,441 attempts separate the checkpoint from the target.
- The actual C2 finalization path contained an O(E²) overlap calculation: `sum(1 for e in final_edges if e in edges)`, where `edges` is a 3,732,460-element list. Worst-case membership work is approximately 13.93 trillion list comparisons.
- The rich-club calculation itself uses set-based edge input and was not identified as the 5h-scale blocker.

Fix committed in `aedb0a0315ede73b909db26dc838122480b85cb6`:
- materialize `original_edge_set = set(edges)` once;
- use hash membership for the original-edge overlap calculation;
- reuse the same set for C2 rich-club finalization;
- add regression test `test_c2_edge_overlap_materializes_original_edges_as_set`.
- test workflow run 554 (`37572718666`) passed.

Scientific status:
**C2 constraint sampler validated; C2 artifact-complete result still OPEN pending a clean finalization run after this infrastructure-only fix.**

Do not alter the C2 null constraint or proposal kernel in response to Run #44. The 5h50m failure was a finalization-complexity bug, not evidence for a rare-tail sampling phenomenon.

Next action:
**Run the same 20260935 C2 completion from the preserved 55.3M checkpoint with `skip_finalization=false`, then audit the resulting final JSON, rich-club output, invariants, provenance, artifact digest, and original-edge overlap.**


## 24. C2 Run #45 — artifact-complete joint NPC + spatial null (2026-10-07)

**Run:** 37573133004  
**Job:** 112636019092  
**Commit:** 59db12b97023e4e8258b4a9948e810ac0895c66c  
**Seed:** 20260935  
**C0 source:** 36318477728  
**Artifact:** 11461697865  
**Artifact SHA-256:** cb185da57f64467ecb1197f77062c510fd6f3e0c94a6c8e46689090709b9c97a

The clean finalization rerun succeeded after the O(E²) original-edge-overlap bug was fixed. The sampler resumed from attempt 55,300,000 / 3,728,657 accepted swaps and reached the exact target at:
- attempts: **55,361,441**
- accepted swaps: **3,732,460 / 3,732,460**
- acceptance rate: **6.7419849%**
- target reached: **true**

Exact C2 invariants passed:
- same edge count: true
- same in-degree: true
- same out-degree: true
- same source-block → target-block counts: true
- same global distance-bin histogram: true
- no self-loops: true
- no duplicate edges: true
- all invariants preserved: **true**
- frozen edges without complete block assignment: **9,869**
- block-pair classes: **3,648**

### First artifact-complete C2 observable
The final artifact contains the full descriptive rich-club curve for thresholds 20–120. Under the joint NPC-like + spatial constraint surface:
- maximum phi_norm: **1.0076220771931181** at degree threshold **51**;
- no threshold exceeded the project's descriptive criterion phi_norm > 1.01;
- onset/offset above 1.01: **none**;
- single-null comparison only: **not a significance test**;
- original-edge overlap fraction: **0.47913761969317825** (~47.91%).

This is scientifically important but deliberately bounded: it is **one realized C2 null**, not an ensemble estimate, p-value, mechanism, or convergence proof. The primary observation is that the C2 joint constraints reduce the maximum normalized rich-club residual to ~0.762%, below the project's 1% descriptive criterion, whereas the earlier spatial-null curve had a >1.01 descriptive region. This difference is a candidate structural-control result, but it must be tested against independent C2 seeds and mixing diagnostics before Gate C is closed.

### C2 state after Run #45
**C2 artifact-complete realization #1 = CLOSED as an artifact/provenance milestone.**  
**C2 ensemble/mixing = OPEN.**  
**Gate C = OPEN.**

### Authorized next sequence
1. Independently reproduce the same C2 constraint surface with new seeds; do not change the proposal kernel or constraints.
2. Record acceptance trajectory and rich-club curve for each seed.
3. Add non-invasive mixing diagnostics / chain checkpoints rather than changing the null definition.
4. Compare the independent C2 ensemble against CFG, NPC-like, and spatial controls.
5. Only after ensemble stability, run stronger spatial/max-entropy sensitivity as a separate null family.
6. Then decide Gate C and only then proceed to matched structure→function ablations.

**Discovery flag:** the disappearance of the >1.01 descriptive rich-club region under the joint C2 constraints is a potentially meaningful structural-control signal. It is not yet a discovery claim; replication is mandatory.


## 2026-10-07 — C2 Run #46 independent-seed replication

Run #46 is the second artifact-complete C2 realization and the first independent-seed replication of Run #45.

Provenance:
- workflow run **37582335296** (Run #46)
- job **112664615048**
- commit **e22a13c41b7a25191b8bbecce700acc00e22efd7**
- seed **20261001**
- C0 source **36318477728**
- artifact **11466140681**
- artifact SHA-256 **d19aa6383818d30c4cd40d01e1cbc00db8d42af028c021052a5111d2edaec213**

Execution:
- attempts **55,237,500**
- accepted swaps **3,732,460 / 3,732,460**
- acceptance rate **6.7571125%**
- target reached: **true**
- frozen edges **9,869**
- block-pair classes **3,648**

All seven declared invariants passed.

Rich-club:
- maximum phi_norm **1.0076660261640915** at threshold **50**
- no threshold exceeded **1.01**
- onset/offset above 1.01: none
- original-edge overlap **0.47912877833921863** (~47.9129%)
- null_count=1; descriptive comparison only, not a significance test.

### Replication reading
Run #45 and #46 independently show the same qualitative C2 outcome: the descriptive >1.01 rich-club region is absent under the joint NPC-like + spatial constraint surface. Peak phi differs by only ~0.00004395 and peak threshold by one degree (51 → 50). Overlap is very close but not identical.

This strengthens the C2 structural-control signal but does not establish significance, mixing/convergence, mechanism, uniqueness of explanation, or computational advantage. C2 ensemble/mixing remains OPEN and Gate C remains OPEN.

### Immediate next step
Run the planned third independent realization with **seed 20261002**, same C2 definition/kernel/dataset/target, starting from the observed graph with no resume from #45/#46. Then perform the planned three-seed curve comparison and non-invasive mixing/stability audit before Gate-C interpretation.


## 2026-10-07 — C2 Run #47: third independent seed completed

Run #47 completes the planned third independent C2 realization.

- workflow run **37617681244**; job **112779897382**
- commit **62d5f9fd0700eca281f4067bb0bf7c5fab922e87**
- seed **20261002**
- C0 source **36318477728**
- artifact **11481125143**
- artifact SHA-256 **4850e27dcb285dcfa258a594241bb5c843d9bf295f65d807a77c55a51c47ce64**
- attempts **55,264,717**
- accepted **3,732,460 / 3,732,460**
- acceptance **6.7537847%**
- target reached **true**

All seven declared invariants passed; frozen edges **9,869** and block-pair classes **3,648**.

Rich-club: maximum phi_norm **1.0077486180432564** at threshold **51**; no threshold exceeded **1.01**; onset/offset none; overlap **0.4792729192007416**; null_count=1.

### Three-seed stability signal

Runs #45, #46, and #47 independently reproduce the same qualitative C2 outcome. Maxima are **1.0076221, 1.0076660, 1.0077486** at thresholds **51, 50, 51**, respectively. All three have no >1.01 region.

This is strong descriptive replication of the structural-control signal, but not a significance test, mixing/convergence proof, mechanism, uniqueness-of-explanation proof, or computational advantage.

### Current gate state

**Three-seed C2 replication set = COMPLETE. C2 ensemble/mixing audit = OPEN. Gate C = OPEN pending stability/mixing and stronger spatial/max-entropy sensitivity. Structure→function remains blocked.**

### Next authorized sequence

1. Perform non-invasive three-seed stability/mixing audit using the existing complete artifacts.
2. Compare full curves, acceptance trajectories, edge turnover/overlap, and available chain/checkpoint diagnostics.
3. Run the stronger spatial/max-entropy sensitivity family as a separate null, without changing the primary C2 definition.
4. Decide Gate C only after those controls.
5. Only then proceed to matched structure→function ablations.
