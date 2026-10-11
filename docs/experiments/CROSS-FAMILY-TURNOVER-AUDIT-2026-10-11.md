# Cross-family turnover audit — partial result (2026-10-11)

## Decision summary

The historical CFG, NPC-like, spatial, and C2 aggregate artifacts were downloaded and inspected. This establishes comparable execution-effort summaries and identifies a critical data gap, but **does not complete the starting-state-memory audit**: the CFG, NPC-like, and spatial aggregate artifacts do not contain final edge sets or original-edge-overlap values. Do not infer missing overlaps from rounded prose or acceptance rates.

The result is therefore **PARTIAL / BLOCKED for matched-turnover interpretation**. The CFG → NPC-like → spatial → C2 rich-club ladder remains descriptive; differences cannot be attributed exclusively to constraint strength until starting-state memory is measured on a comparable basis.

## Sources inspected

| Family | Source artifact | Artifact SHA-256 |
|---|---|---|
| CFG 100-null | [Run 35987597540, artifact 10807064530](https://github.com/Rami-alabsi/connectome-computing/actions/runs/35987597540/artifacts/10807064530) | `5343abb81fe1cb1a19692e72c5b326fbed87814e99c1476a5bb303164954fae6` |
| NPC-like 100-null | [Run 36295429519, artifact 10925776875](https://github.com/Rami-alabsi/connectome-computing/actions/runs/36295429519/artifacts/10925776875) | `1d44d072ba34f07d76fc14d480380be3ac3dca91c7a7c6febdb08ab3070ec1e4` |
| Spatial 8-null | [Run 36386665317, artifact 10955439258](https://github.com/Rami-alabsi/connectome-computing/actions/runs/36386665317/artifacts/10955439258) | `9bd4fb3c264374bc93199b5efd14fbaa6fcdf312faff616ca45aa0a34e68d588` |
| C2 independent seed #45 | [Run 37573133004, artifact 11461697865](https://github.com/Rami-alabsi/connectome-computing/actions/runs/37573133004/artifacts/11461697865) | `cb185da57f64467ecb1197f77062c510fd6f3e0c94a6c8e46689090709b9c97a` |
| C2 independent seed #46 | [Run 37582335296, artifact 11466140681](https://github.com/Rami-alabsi/connectome-computing/actions/runs/37582335296/artifacts/11466140681) | `d19aa6383818d30c4cd40d01e1cbc00db8d42af028c021052a5111d2edaec213` |
| C2 independent seed #47 | [Run 37617681244, artifact 11481125143](https://github.com/Rami-alabsi/connectome-computing/actions/runs/37617681244/artifacts/11481125143) | `4850e27dcb285dcfa258a594241bb5c843d9bf295f65d807a77c55a51c47ce64` |
| C2 extended chain 32E | [Run 38112364771, artifact 11695105557](https://github.com/Rami-alabsi/connectome-computing/actions/runs/38112364771/artifacts/11695105557) | `c297deadd7caa74fcda4c42498a2a1d4184b66ff335b0ed38326c7ab88a3f330` |

The three CFG/NPC/spatial aggregate ZIPs each contain the aggregate JSON but not the per-null final edge sets. The C2 artifacts include a resumable state, and their runner explicitly reports original-edge overlap.

## Execution-effort observations

All four null families use 3,732,460 unique directed pairs. CFG, NPC-like, and spatial each report 3,732,460 accepted swaps per null (one accepted swap per original directed pair as a normalized exposure measure). C2 independent realizations use the same 1E target; the extended chain reaches 32E.

| Family / milestone | Realizations | Accepted swaps per realization | Proposal attempts per realization | Mean acceptance rate | Original-edge overlap |
|---|---:|---:|---:|---:|---|
| CFG | 100 | 3,732,460 | 3,763,906–3,765,053 | 99.1486% | Not present in aggregate artifact |
| NPC-like | 100 | 3,732,460 | 127,522,612–127,797,934 | 2.9242% | Not present in aggregate artifact |
| Spatial | 8 | 3,732,460 | 110,624,558–110,813,120 | 3.3712% | Not present in aggregate artifact |
| C2 independent seeds #45–#47 | 3 | 3,732,460 | 55,237,500–55,361,441 | 6.75096% mean | 47.9129% mean |
| C2 8E milestone | 1 chain | 29,859,680 | 500,418,411 | 5.96694% | 24.8152% |
| C2 16E milestone | 1 chain | 59,719,360 | 1,016,885,788 | 5.87277% | 19.8354% |
| C2 32E milestone | 1 chain | 119,438,720 | 2,053,048,908 | 5.81763% | 16.1910% |

Acceptance-rate calculations for CFG, NPC-like, and spatial use each null's successful-swap count divided by its recorded proposal attempts; the family means/ranges were calculated from the archived aggregate `swap_stats`. The C2 independent-seed mean is the arithmetic mean of the three reported acceptance rates.

## Interpretation guardrails

1. Accepted swaps per edge is an exposure normalization, **not** a proof of matched turnover. Each family has a different proposal/acceptance kernel and different constraints.
2. Acceptance rates are not directly comparable as mixing-speed estimates. In particular, CFG's ~99.15% rate does not establish faster mixing than NPC-like or spatial.
3. The C2 overlap decline from 47.91% at 1E to 16.19% at 32E demonstrates continued change relative to the observed graph; it does not establish stationarity or convergence.
4. The aggregate CFG/NPC/spatial JSON files provide curve summaries and swap statistics, not final edge sets or observed-edge-overlap. This audit cannot fill those missing fields.
5. The observed rich-club numerator/curve is documented as identical across CFG, NPC-like, and spatial families. That guards against a changed observed graph, but it does not remove the separate confound of unequal starting-state memory.

## Next required diagnostic

- Add a non-invasive overlap/turnover record to the relevant null runners and retain sufficient per-null edge-set provenance for reproducibility.
- Run a predeclared matched-turnover comparison across CFG, NPC-like, spatial, and C2, recording at each milestone: accepted swaps per edge, attempts, acceptance rate, observed-edge overlap, and the complete rich-club curve.
- Prefer comparison at matched observed-edge-overlap levels as well as reporting accepted-swaps-per-edge. Do not tune thresholds or alter any null-family constraints after inspecting outcomes.
- Until these overlap measurements exist, keep the causal interpretation of the enrichment ladder and Gate C OPEN. Structure→function/RSS/architecture/benchmark/scaling remain BLOCKED.

This record is an audit of existing artifacts, not a new null execution or a scientific significance test.
