# C2 Same-Chain Curve and Turnover Comparison — 8E to 128E

## Scope

This is a retrospective descriptive comparison of the same-seed C2 chain at 8E, 16E, 32E, 64E, and 128E accepted swaps. It is not an independent-seed ensemble, a formal mixing diagnostic, or a convergence test.

All five result JSON files were extracted from their GitHub Actions artifacts. Each downloaded ZIP was independently SHA-256 hashed; all five hashes match the digest reported by GitHub. Every result uses seed `20261002`, the same code version, input fingerprint, and constraint fingerprint, and contains 101 `phi_norm` values at thresholds k=20..120.

## Source artifacts and digest checks

| Stage | Run ID | Artifact ID | Accepted swaps | Attempts | Original-edge overlap | ZIP SHA-256 |
|---|---:|---:|---:|---:|---:|---|
| 8E | 37737675496 | 11532885112 | 29,859,680 | 500,418,411 | 24.8152% | `aed5fed3fc4cd07066fb8a57290b0bf0ceed4e978aea8f7127cd9931e4a17600` |
| 16E | 37774000742 | 11552145132 | 59,719,360 | 1,016,885,788 | 19.8354% | `aec152cabf94e24277d9fb55cce97e2e2b179c86b0ba75ba3a65de1c050e962f` |
| 32E | 38112364771 | 11695105557 | 119,438,720 | 2,053,048,908 | 16.1910% | `c297deadd7caa74fcda4c42498a2a1d4184b66ff335b0ed38326c7ab88a3f330` |
| 64E | 38122390361 | 11702767144 | 238,877,440 | 4,128,211,946 | 13.6984% | `2febb9ec29918ca811a4139076e6caf7342d34fc664f44c8677d9511847493ac` |
| 128E | 38244237906 | 11761653312 | 477,754,880 | 8,280,080,824 | 12.0973% | `cae38791987a8f5fb7f00e380e12342d789c6f643794f2bc3c736ea9fea9b674` |

Common code version: `890a73d18a8e3d4e006233b45d9dd2c5771fa849f69dc3d462ed7588af6ef076`.

Common input fingerprint: `b43e3aa79c14f5338b4d0dd66ec5c0db88d68b02281facfd2a28941093072a8e`.

Common constraint fingerprint: `b330c16977c084434c129086112cf75710f95b8c39af7fd4df57ab16a87d76e3`.

All five result JSON files report all seven declared invariants true. Run #57's full artifact and JSON/checkpoint hashes are detailed in `C2-RUN-57-128E-COMPLETION-AUDIT-2026-10-13.md`.

## Curve summary

| Stage | Peak `phi_norm` | Peak k | `phi_norm > 1.01` interval | `phi_norm < 0.99` interval |
|---|---:|---:|---|---|
| 8E | 1.0106499041 | 51 | k=45–56 (11 thresholds) | k=84–120 (37 thresholds) |
| 16E | 1.0112045029 | 51 | k=43–57 (15 thresholds) | k=84–120 (37 thresholds) |
| 32E | 1.0117177355 | 51 | k=42–58 (17 thresholds) | k=85–120 (36 thresholds) |
| 64E | 1.0119603674 | 51 | k=39–59 (21 thresholds) | k=86–120 (35 thresholds) |
| 128E | 1.0126376258 | 51 | k=38–59 (22 thresholds) | k=86–120 (35 thresholds) |

Threshold intervals are descriptive flags under the project's fixed cutoffs, not significance intervals.

## Pointwise curve deltas on the common 101 thresholds

Delta is later stage minus earlier stage.

| Comparison | Pearson r | Mean delta | RMSE | Max absolute delta | Threshold of max absolute delta | Direction |
|---|---:|---:|---:|---:|---:|---|
| 8E → 16E | 0.99993719 | -0.0001743540 | 0.0008359351 | 0.0018550584 | k=120 | mixed |
| 16E → 32E | 0.99989921 | +0.0006726689 | 0.0007386053 | 0.0013465088 | k=96 | all 101 increased |
| 32E → 64E | 0.99991184 | +0.0004145310 | 0.0004847429 | 0.0009396361 | k=82 | all 101 increased |
| 64E → 128E | 0.99992982 | +0.0001459177 | 0.0002613567 | 0.0006879088 | k=50 | 71 increased, 30 decreased |

For 64E → 128E, the 30 decreases occurred at k=21–24, 27–30, 64, 69, 71–78, 81–84, and 88–89, 105–110; the other 71 thresholds increased. Thus the late trajectory is not a uniform upward shift, but it is still changing: the mean delta is positive and the maximum absolute pointwise difference is nonzero. High correlations primarily indicate similar curve shape and do not establish a plateau.

## Interpretation

1. **128E is a completed operational milestone.** Its artifact and curve were independently inspected, and the archive digest matches GitHub.
2. **Turnover continues with chain length.** Original-edge overlap decreases monotonically across the five saved milestones, from 24.8152% at 8E to 12.0973% at 128E. This is a state-memory/turnover descriptor, not a calibrated expectation for a constrained Markov chain.
3. **The curve is still moving.** The 64E → 128E comparison has positive mean delta and mixed pointwise changes; no convergence plateau is established.
4. **No inferential result follows from one chain/null at each cumulative stage.** The 128E runner explicitly says `null_count=1`, `scientific_conclusion=null`, and “feasibility only; no rich-club inference.” Threshold flags are not p-values.
5. **Gate C and formal mixing/convergence remain OPEN.** Next priority should be a planned cross-family turnover/control study and/or an explicit drift diagnostic with independent chains, not automatic extension based on correlation.

## Reproducibility note

Artifact hashes above were independently recomputed from the downloaded ZIP bytes and matched GitHub's reported digests. JSON curve metrics were parsed from each artifact. The full underlying edge state was not independently regenerated from the authoritative graph during this curve-comparison audit.
