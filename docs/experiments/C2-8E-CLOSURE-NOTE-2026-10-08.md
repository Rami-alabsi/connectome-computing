# C2 8E Mixing Extension — Closure Note (2026-10-08)

## Verified run
- Repository: Rami-alabsi/connectome-computing
- Workflow run: 37729284335
- Source seed: 20261002
- Resume source: C2 run #47 / workflow 37617681244
- Maximum proposal attempts: 500,000,000
- Target accepted swaps: 29,859,680 (8E)
- Actual accepted swaps at 500M: 29,835,212
- Remaining accepted swaps to 8E: 24,468
- Final acceptance rate: 5.9670%
- All seven C2 invariants remain preserved by the run.

## Artifact
- Artifact: fafb-v783-c2-feasibility-500000000
- Artifact ID: 11531289161
- SHA256: b1a54a8070f6288d61e6d48b51b023c7ef863a1bf89352f1c3852bad6767ff62
- The artifact contains c2-feasibility-500000000.json and c2-state.pkl.gz.
- The checkpoint state was independently inspected: attempt=500,000,000; edge_list length=3,732,460; code_version=890a73d18a8e3d4e006233b45d9dd2c5771fa849f69dc3d462ed7588af6ef076; constraint_fingerprint=b330c16977c084434c129086112cf75710f95b8c39af7fd4df57ab16a87d76e3.

## Milestones actually reached
### 2E
- target_accepted: 7,464,920
- attempt: 117,319,494
- acceptance_rate: 0.0636289822
- original_edge_overlap_fraction: 0.3882404634
- phi_norm: k32=1.0060707296; k50=1.0089147211; k60=1.0068321204; k100=0.9738670919; k120=0.9613952162

### 4E
- target_accepted: 14,929,840
- attempt: 244,062,520
- acceptance_rate: 0.0611721947
- original_edge_overlap_fraction: 0.3113573890
- phi_norm: k32=1.0068581546; k50=1.0100567055; k60=1.0077622837; k100=0.9732090468; k120=0.9595450197

## Interpretation guardrails
- This is a mixing/stability diagnostic, not a formal proof of Markov-chain convergence, burn-in, ESS, or independence.
- The 8E milestone was NOT reached; therefore this note must not be cited as an 8E-complete result.
- The 4E k=50 value crosses the project's descriptive 1.01 threshold. This must be retained as an observable, not suppressed or reinterpreted as statistical significance.
- High-degree depletion remains an observable and is retained alongside the mild positive region.
- Gate C remains OPEN.
- No structure→function, RSS/architecture, benchmark, or scaling claim is unlocked by this run.

## Next authorized action
Resume from the 500M checkpoint and request only the remaining 24,468 accepted swaps. Because the current workflow has a 500M proposal cap, dispatch a follow-up run with a proposal budget safely above 500M (for example 501,000,000) and:
- c0_run_id=36318477728
- seed=20261002
- target_accepted=29859680
- resume_run_id=37729284335
- resume_artifact_name=fafb-v783-c2-feasibility-500000000
- mixing_milestones=7464920,14929840,29859680
- trace_attempts=0
- skip_finalization=false

Do not change the C2 scientific kernel or its seven hard constraints.
