# Week 03 — Eval & Observability Lab

A self-contained Python project demonstrating **evaluation pipelines and observability**: golden
dataset scoring, release gate logic, structured trace collection, and ship/no-ship decisions.

## Project Structure

```
week03-eval-observability/
├── __init__.py
├── evaluator.py     # Golden dataset, metric scoring, release gate
├── tracer.py        # Span-based trace collection with context manager
├── cli.py           # Argparse CLI (run / compare / thresholds sub-commands)
├── requirements.txt
└── tests/
    └── test_evaluator.py  # 20 unit tests (pytest)
```

## Quick Start

```bash
# From this directory — no install needed

# Compare baseline vs candidate:
python cli.py compare

# Evaluate a single run with trace:
python cli.py run --name candidate

# Show release gate thresholds:
python cli.py thresholds
```

## Running Tests

```bash
python -m pytest tests/ -v
```

## Key Concepts Covered

| Concept        | Module         | Description                                  |
|----------------|----------------|----------------------------------------------|
| Golden dataset | `evaluator.py` | Fixed Q&A pairs with expected term coverage  |
| Metric scoring | `evaluator.py` | Per-question faithfulness scores             |
| Release gate   | `evaluator.py` | Multi-metric threshold check → ship/no-ship  |
| Span tracing   | `tracer.py`    | Context-manager-based timing and metadata    |
| Observability  | `tracer.py`    | Structured trace dict with duration per span |
| CLI            | `cli.py`       | Sub-commands: `run`, `compare`, `thresholds` |

## Requirements

- Python 3.9+
- No external dependencies (stdlib only)
