# Spec Drift Benchmark

**Spec Drift** measures whether coding models preserve previously established software constraints across successive feature changes.

The central question is not simply “can the model implement the next feature?” but:

> How long does a non-negotiable requirement survive once the conversation moves on?

The benchmark compares two conditions:

- **stated_once** — invariants appear only in the initial prompt.
- **reinforced** — the same invariants are restated before every later change request.

Each scenario is evaluated after every turn on two independent axes:

1. **Feature success** — did the requested change work?
2. **Constraint retention** — do the original invariants still hold?

This makes it possible to measure constraint erosion over time instead of collapsing everything into a single coding score.

## Status

Project scaffold is ready. The `file_no_overwrite` scenario is fully specified and locally testable. The remaining scenario catalog is frozen as the planned benchmark corpus and can be implemented one by one.

## Planned corpus

1. Public API signature compatibility
2. Ordered async processing
3. Standard-library-only dependency boundary
4. Never overwrite an existing file ✅
5. Error propagation
6. Unknown configuration keys remain errors
7. Secrets never appear in logs
8. Existing JSON schema remains stable
9. Offline component performs no network access
10. CLI flags remain backward compatible
11. Event processing remains idempotent
12. Authorization occurs before state mutation

## Repository layout

```text
benchmark/              Kaggle Benchmarks task entrypoint
scenarios/              Frozen scenario fixtures and executable tests
src/spec_drift/         Prompt construction, scoring, and evaluation helpers
tests/                  Unit tests for the benchmark harness
docs/methodology.md     Experimental design and hypotheses
scripts/                Local helper scripts
```

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest
```

For Kaggle integration:

```bash
pip install -e '.[kaggle]'
kaggle b init -y
python benchmark/kaggle_task.py
```

The current Kaggle CLI can push a task file directly:

```bash
kaggle b t push spec-drift-file-overwrite -f benchmark/kaggle_task.py --wait
```

## Experimental unit

A scenario contains:

- starter code
- one or more non-negotiable invariants
- three sequential change requests
- feature tests for each change
- invariant tests that run after every change

For each model, every scenario is run in both experimental conditions using the same starter code and turn order.

## Primary metrics

- **Feature Success Rate (FSR)** — passed feature checks / total feature checks
- **Constraint Retention Rate (CRR)** — passed invariant checks / total invariant checks
- **Spec Drift Rate (SDR)** — violated invariant checks / total invariant checks

The main visualization should be a **constraint survival curve** across turns 0–3.

## Methodological rule

Avoid describing failures as model “memory loss.” The benchmark observes **constraint retention in generated code**. Internal forgetting is only one possible explanation.

## License

MIT
# spec-drift
