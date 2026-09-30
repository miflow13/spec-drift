# Methodology

## Research question

When an AI coding model receives a software requirement once, how reliably does it preserve that requirement across successive feature changes?

Secondary question: does explicitly restating the original constraints during later changes reduce regressions?

## Conditions

### stated_once

The initial prompt includes all non-negotiable invariants. Later prompts contain only the requested change.

### reinforced

The initial prompt is identical, but every later request also repeats the original invariants verbatim.

No other wording, starter code, feature request, or turn ordering changes between conditions.

## Hypotheses

- **H1: Constraint erosion.** Constraint retention decreases as additional modifications accumulate.
- **H2: Reinforcement effect.** Restating invariants improves constraint retention.
- **H3: Feature/constraint tradeoff.** Some models achieve high feature success while causing more regressions.
- **H4: Constraint type effect.** Safety, behavioral, architectural, compatibility, and validation constraints erode at different rates.

These are pre-registered hypotheses for the project, not conclusions.

## Scoring

Every turn is evaluated separately.

### Feature Success Rate

`FSR = feature checks passed / feature checks attempted`

### Constraint Retention Rate

`CRR = invariant checks passed / invariant checks attempted`

### Spec Drift Rate

`SDR = 1 - CRR`

For reporting, preserve per-turn results. Do not report only a final aggregate; the erosion curve is a primary result.

## Controls

- Python only for v1.
- Small programs to avoid turning the task into a long-context benchmark.
- Same starter code across conditions.
- Same change requests and ordering across conditions.
- Deterministic executable assertions whenever possible.
- No LLM-as-judge for primary metrics.
- Freeze scenarios before inspecting final cross-model results.

## Interpretation

The benchmark measures whether generated code continues to satisfy previously stated constraints. It does not directly reveal a model's internal memory state or reasoning process.
