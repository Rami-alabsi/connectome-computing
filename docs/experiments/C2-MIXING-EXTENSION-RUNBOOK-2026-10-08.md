# C2 Mixing-Extension Runbook — 2026-10-08

## Purpose

This document records the exact manual inputs for the first extended-chain C2 mixing diagnostic. It is an operational diagnostic only; it does not alter the C2 null definition and does not close Gate C by itself.

## Authoritative inputs

- Repository: `Rami-alabsi/connectome-computing`
- Workflow: `.github/workflows/m2-fafb-c2-feasibility.yml`
- Authoritative C0 workflow run ID: `36318477728`
- C0 artifact name: `fafb-v783-gate-c0-princeton-arbor-spatial-preflight`
- C0 artifact ID: `10931780910`
- C0 artifact SHA256: `7265e20db3721f6b438a93227180eb0d8b0d3ad3fd9894bcbbe4a14a81dd5f36`
- C2 source run: #47
- C2 source workflow run ID: `37617681244`
- C2 source artifact: `fafb-v783-c2-feasibility-60000000`
- C2 source artifact ID: `11481125143`
- C2 source artifact SHA256: `4850e27dcb285dcfa258a594241bb5c843d9bf295f65d807a77c55a51c47ce64`
- C2 source seed: `20261002`
- C2 one-E target: `3732460` accepted swaps

## Exact workflow inputs for the extension

| Input | Value |
|---|---:|
| `c0_run_id` | `36318477728` |
| `seed` | `20261002` |
| `attempts` | `500000000` |
| `target_accepted` | `29859680` |
| `resume_run_id` | `37617681244` |
| `resume_artifact_name` | `fafb-v783-c2-feasibility-60000000` |
| `trace_attempts` | `0` |
| `skip_finalization` | `false` |
| `mixing_milestones` | `7464920,14929840,29859680` |

The accepted-swap milestones are:
- 2E = 7,464,920
- 4E = 14,929,840
- 8E = 29,859,680

The large `attempts` ceiling is only a maximum proposal budget; the workflow stops when `target_accepted` is reached. The existing workflow timeout is 350 minutes.

## Why these values

This continues Run #47 from its final checkpoint using the same deterministic seed, rather than starting a new independent chain. The diagnostic records at 2E, 4E and 8E:
- accepted swaps,
- proposal attempts,
- acceptance rate,
- overlap with the original observed graph,
- `phi_norm` at k = 32, 50, 60, 100, 120.

This is intended to test whether the aggregate observable remains stable as microscopic edge turnover continues.

## Interpretation guardrails

- This is a mixing/convergence diagnostic, not a formal proof of mixing.
- The same starting graph and same seed mean this is not independent-start evidence.
- Do not use Pearson correlation against the observed reference as a mixing proof.
- Do not infer p-values or significance from the descriptive `phi_norm` curves.
- The existing C2 ensemble constraints remain unchanged.
- The observed positive region around k≈32–60 and the high-degree depletion (<0.99) must both be retained as descriptive observables.
- Gate C remains OPEN until all documented closure criteria are satisfied.

## Execution status

**Prepared; not yet executed.**

The current GitHub connector can inspect runs/artifacts but does not expose a workflow-dispatch action. Therefore no execution is claimed here.

After manual dispatch, record:
1. new workflow run ID;
2. conclusion;
3. artifact name/ID/digest;
4. milestone records at 2E/4E/8E;
5. any timeout, stall, checkpoint, or memory observations;
6. whether the final state reached 8E.

