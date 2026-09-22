# M6-COSMIC: Field vs Explicit Relational Communication

## Scope

M6-COSMIC tests a narrow engineering hypothesis derived from the cross-domain synthesis:
a compact global relational field may carry aggregate information efficiently, while
explicit sparse relations remain necessary for pair-sensitive information.

This is a synthetic computational experiment. It is **not** a model of gravity,
quantum fields, spacetime, or the physical cosmic web.

## Matched conditions

The first benchmark contains three conditions:

1. **Field** — one compact global field payload.
2. **Sparse** — explicit endpoint effective states for selected module pairs.
3. **Hybrid** — global field plus selected explicit pair relations.

The benchmark records transmitted values/bytes and evaluates two task classes:

- **Global aggregate task:** recover the mean effective state across modules.
- **Pair-sensitive task:** recover the effective state of one selected module pair.

The fixture intentionally makes the selected pair different from the global mean, so
a field that discards module identity cannot pass the pair-sensitive test by accident.

## Interpretation rule

No architecture is declared superior from this benchmark alone.

The intended falsifiable result is a **tradeoff curve**:

- field communication should be compact for aggregate information;
- explicit pair communication should retain pair identity;
- hybrid communication should be evaluated for whether a small explicit backbone can
  recover pair-sensitive information without losing the communication advantage of
  the compact field.

## Next benchmark gates

Before any novelty claim:

- scale modules and hierarchy size;
- sweep field dimension;
- sweep explicit active-pair budget;
- add random/degree-matched relation controls;
- add noise/perturbation tests;
- separate global, local, and pair-sensitive tasks;
- report communication bytes, useful information/error, active relations and compute proxy;
- repeat across random seeds;
- compare against non-biological compression/routing baselines;
- re-run targeted prior-art search.

## Current status

The first scaling sweep has now executed successfully in CI (144 rows; nodes = 100, 1,000, 10,000; field dimensions = 1, 2, 4, 8; active-pair budgets = 1, 4, 16). CI and unit tests passed on the benchmark commit.

### Observed baseline sweep

The deterministic fixture shows the expected communication scaling: for state dimension 8, full transmission grows from 640 bytes (100 nodes) to 6,400 bytes (1,000) and 64,000 bytes (10,000), while the field payload remains 8–64 bytes depending on field dimension and the sparse payload is bounded by the active-pair budget.

For the current synthetic task definitions, sparse routing gives much lower global RMSE than the compact field at the same small communication budgets, while the field can recover the global aggregate exactly when field dimension equals the full state dimension. The hybrid condition exactly recovers the selected pair-sensitive target while retaining the compact field payload.

These are **implementation-validation observations, not evidence of architectural superiority**. The field error grows strongly with node count in this fixture because the deterministic node-state generator currently has a magnitude that grows with node index. Therefore the absolute RMSE is not yet a scale-normalized scientific metric. The next revision must use bounded/normalized signals and report normalized error before interpreting scaling behavior.

No novelty claim is made from this sweep.

## Multiscale implementation

The benchmark now includes a deterministic hierarchy generator and scaling runner. The first sweep varies node count, compact field dimension, and explicit active-pair budget across full, sparse, field, and hybrid conditions. The runner writes a CSV under `results/` when executed locally or in CI. No empirical result is recorded in this document until the sweep is actually executed and its output is reviewed.
