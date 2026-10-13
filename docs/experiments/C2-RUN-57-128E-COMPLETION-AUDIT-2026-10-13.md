# C2 Run #57 — 128E Completion and Artifact Audit

## Status and scope

- C2 experiment run: **#57**; GitHub Actions workflow run: [**#58 / 38244237906**](https://github.com/Rami-alabsi/connectome-computing/actions/runs/38244237906)
- Job: [feasibility / 114794049385](https://github.com/Rami-alabsi/connectome-computing/actions/runs/38244237906/job/114794049385)
- Workflow conclusion: **success**; all 10 substantive job steps completed successfully.
- Dataset: FAFB v783; purpose remains the C2 NPC-like + arbor-distance feasibility pilot.
- Seed: `20261002`.
- Run commit: `07e362e476c3f1a15b51e9c60013eb46804849a4`.
- The job resumed from Run #56's saved checkpoint at attempt `6,200,000,000`, accepted swaps `358,099,863`; log confirms resume and entry into the sampling loop. The GitHub Actions API reports workflow `run_number=58`; the project's C2 experiment sequence labels this as Run #57.
- Cumulative target `477,754,880` accepted swaps (128E) was reached.

## Result and reproducibility metadata

- Attempts at target: **8,280,080,824**.
- Accepted swaps: **477,754,880**.
- Overall acceptance rate: **5.7699301511%**.
- Elapsed sampling time in result: **20,064.41 seconds** (~5 h 34 min 24 s).
- Original-edge overlap fraction: **0.1209730312** (12.0973%; descriptive turnover measure only).
- Unique directed pairs / edge count: **3,732,460**.
- Block-pair classes: **3,648**; frozen edges without complete block assignment: **9,869**.
- Code version: `890a73d18a8e3d4e006233b45d9dd2c5771fa849f69dc3d462ed7588af6ef076`.
- Input fingerprint: `b43e3aa79c14f5338b4d0dd66ec5c0db88d68b02281facfd2a28941093072a8e`.
- Constraint fingerprint: `b330c16977c084434c129086112cf75710f95b8c39af7fd4df57ab16a87d76e3`.
- Result JSON reports `target_reached=true` and `all_invariants_preserved=true`.

## Artifact verification

- Artifact: [`fafb-v783-c2-feasibility-9000000000`](https://github.com/Rami-alabsi/connectome-computing/actions/runs/38244237906/artifacts/11761653312)
- Artifact ID: `11761653312`; size: **46,379,353 bytes**; expires `2027-01-10T11:41:07Z`.
- GitHub-reported ZIP SHA-256: `cae38791987a8f5fb7f00e380e12342d789c6f643794f2bc3c736ea9fea9b674`.
- ZIP was downloaded and hashed independently in the working environment; SHA-256 **matches exactly**.
- ZIP contains:
  - `c2-feasibility-9000000000.json` — 585,564 bytes; SHA-256 `4c1c9691d2c73f739a9c937c7b4775bd6b9f2112a7ddaeb31dd4ef72f946e902`.
  - `c2-state.pkl.gz` — 46,276,494 bytes; SHA-256 `4196fdc9dfa1a92b01aad9a815a375e795360718841e3b22d14a4181047ee32a`.
- Archive listing and JSON were independently inspected. The JSON contains 1,669 checkpoint records and the full 101-threshold curve.

## Seven declared invariants

All are `true` in the final result JSON:

1. Same edge count.
2. Same in-degree sequence.
3. Same out-degree sequence.
4. Same block-pair counts.
5. Same distance-bin histogram.
6. No self-loops.
7. No duplicate edges.

This is the runner's reported invariant validation, independently confirmed to be present in the downloaded JSON. The checkpoint's full graph state was not independently re-derived from the authoritative graph in this audit.

## Descriptive rich-club curve — not inferential evidence

- Full curve: **101 thresholds**.
- Peak `phi_norm`: **1.0126376258 at k=51**.
- Descriptive `phi_norm > 1.01` interval: **k=38–59** (22 thresholds).
- Descriptive `phi_norm < 0.99` interval: **k=86–120** (35 thresholds).
- At the final milestone, selected values: k=32: **1.0084475991**; k=50: **1.0126167629**; k=60: **1.0099717269**; k=100: **0.9730095234**; k=120: **0.9578061264**.
- Original-edge overlap declined across the five saved milestones: 12.6766%, 12.4974%, 12.3386%, 12.2026%, 12.0973%.
- The result explicitly sets `scientific_conclusion=null` and `interpretation="feasibility only; no rich-club inference"`. Its rich-club section says `null_count=1` and “descriptive single-null comparison; not a significance test.”

## Limitations and interpretation

- **128E completion is an operational milestone, not proof of Markov-chain mixing or convergence.** The single-chain trajectory still shows changing overlap and descriptive curve movement; do not infer a plateau from this run alone.
- `phi_norm > 1.01` and `phi_norm < 0.99` are descriptive thresholds, not p-values or significance tests.
- The 9,869 edges lacking complete dominant-block assignment are frozen/excluded from the block-pair constraint as documented by the runner.
- CI's pytest step was **collection preflight only**, not execution of the full test suite; do not report this workflow as a full pytest pass.
- Coarse arbor-distance bins and project-specific NPC-like block definitions remain modeling choices.
- No biological mechanism, functional advantage, novelty, patentability, or commercial value is established.
- Gate C and formal mixing/convergence remain **OPEN**.

## Next decision

1. Preserve Run #57 and its hashes as the completed same-chain 128E record.
2. Update the master compass and authoritative status; supersede, but do not erase, the historical Run #56 partial audit.
3. Before another long C2 run, prioritize a cross-family turnover audit or a predeclared curve-drift comparison using the 8E/16E/32E/64E/128E results and matched controls. Do not launch sensitivity or C3-A scale-up concurrently without a separate budget and scientific decision.
