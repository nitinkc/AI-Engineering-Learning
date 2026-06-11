# Week 3 Mini Project - Eval and Ops Lab

Pre-reading: [03 Evals, Observability, and Production](../01-foundations/03-evals-observability-production.md)

This mini project gives Week 3 a production-minded loop: small eval set, baseline vs candidate
comparison, release gate decision, structured trace records, and a simple readiness summary.

Run the commands below from an activated project venv.

## What You Will Build

| Capability                       | Output                       |
|----------------------------------|------------------------------|
| Golden dataset                   | Small evaluation set         |
| Baseline vs candidate comparison | Metric delta summary         |
| Release gate                     | Deploy or no-deploy decision |
| Trace record                     | Structured run evidence      |
| Readiness summary                | Operational review note      |

## How to Run

```bash
cd docs/03-mini-projects/code/week03-eval-observability

# Compare baseline vs candidate
04-python cli.py compare

# Evaluate one run with trace data
04-python cli.py run --name candidate

# Run tests
04-python -m pytest tests/ -v
```

## Portfolio Structure

```text
code/week03-eval-observability/
├── evaluator.py
├── tracer.py
├── cli.py
└── tests/test_evaluator.py
```

## What to Modify Across the Week

| Day    | Suggested change                                   |
|--------|----------------------------------------------------|
| Day 15 | Add 3 more eval questions and acceptance criteria. |
| Day 16 | Change one threshold and observe gate behavior.    |
| Day 17 | Add one new trace field for diagnosis.             |
| Day 18 | Add one policy or safety status field.             |
| Day 19 | Tighten or relax the latency budget.               |
| Day 20 | Write a short postmortem for a failed gate.        |
| Day 21 | Summarize readiness gaps in one scorecard.         |

## Starter Assets

| Asset                                                                                                       | Purpose                                        |
|-------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| [week03-eval-observability/cli.py](code/week03-eval-observability/cli.py)                                   | CLI entry point for eval runs and comparisons  |
| [week03-eval-observability/evaluator.py](code/week03-eval-observability/evaluator.py)                       | Golden set scoring and release-gate logic      |
| [week03-eval-observability/tracer.py](code/week03-eval-observability/tracer.py)                             | Structured span tracing for observability      |
| [week03-eval-observability/tests/test_evaluator.py](code/week03-eval-observability/tests/test_evaluator.py) | Unit tests for evaluator and tracer logic      |
| [week03_eval_observability_output.json](output/week03_eval_observability_output.json)                       | Sample eval comparison and release-gate output |

## Matching Lab Outputs

| Output              | Why keep it                         |
|---------------------|-------------------------------------|
| Eval set            | Shows you define quality explicitly |
| Metric delta        | Helps justify a change objectively  |
| Release gate result | Demonstrates deployment discipline  |
| Readiness review    | Feeds ops and interview narratives  |

## Portfolio Checklist

| Item                                                     | Done? |
|----------------------------------------------------------|-------|
| Save one baseline vs candidate metric comparison.        | [ ]   |
| Save one failed-gate example with threshold explanation. | [ ]   |
| Save one structured trace output with span timing.       | [ ]   |
| Write one STAR-ready bullet on shipping decisions.       | [ ]   |

--8<-- "_abbreviations.md"
