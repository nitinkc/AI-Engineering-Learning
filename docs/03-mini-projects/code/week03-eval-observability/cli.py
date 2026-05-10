"""CLI entry point for the Eval & Observability Lab.

Usage examples
--------------
  # Compare baseline vs candidate (default):
  python cli.py compare

  # Evaluate a single named run:
  python cli.py run --name baseline
  python cli.py run --name candidate

  # Show release gate thresholds:
  python cli.py thresholds
"""
from __future__ import annotations

import argparse
import json

from evaluator import EVAL_SET, GATE_THRESHOLDS, evaluate_run, summarize_run
from tracer import Trace, timed_span

# ---------------------------------------------------------------------------
# Pre-built run configurations
# ---------------------------------------------------------------------------

RUNS: dict[str, dict] = {
  "baseline": {
    "faithfulness": 0.82,
    "retrieval_hit_rate": 0.78,
    "latency_p95_ms": 3300,
    "cost_per_success": 0.06,
  },
  "candidate": {
    "faithfulness": 0.89,
    "retrieval_hit_rate": 0.84,
    "latency_p95_ms": 3100,
    "cost_per_success": 0.07,
  },
}

# Synthetic responses aligned with the golden eval set
SYNTHETIC_RESPONSES: dict[str, list[str]] = {
  "baseline": [
    "Go to the security portal and verify your identity to reset the key.",
    "Escalate to the review team for high risk situations.",
    "The system will notify an operator when budget runs low.",
  ],
  "candidate": [
    "Use the security portal to verify identity and reset the expired API key.",
    "High risk requests require review and escalation to the security team.",
    "When retry budget is exhausted the system will escalate to a human reviewer.",
  ],
}


def cmd_run(args: argparse.Namespace) -> None:
  name = args.name
  if name not in RUNS:
    raise SystemExit(f"Unknown run {name!r}. Choose from: {', '.join(RUNS)}")

  trace = Trace(trace_id=f"trace-{name}")

  with timed_span(trace, "evaluate", {"run": name}):
    eval_result = evaluate_run(name, SYNTHETIC_RESPONSES[name])

  metrics = {**RUNS[name], "faithfulness": eval_result["faithfulness"]}

  with timed_span(trace, "release_gate"):
    summary = summarize_run(name, metrics)

  print(
      json.dumps(
          {
            "eval": eval_result,
            "summary": summary,
            "trace": trace.to_dict(),
          },
          indent=2,
      )
  )


def cmd_compare(_args: argparse.Namespace) -> None:
  results = []
  for name in ("baseline", "candidate"):
    eval_result = evaluate_run(name, SYNTHETIC_RESPONSES[name])
    metrics = {**RUNS[name], "faithfulness": eval_result["faithfulness"]}
    results.append(summarize_run(name, metrics))

  print(
      json.dumps(
          {"eval_set": EVAL_SET, "runs": results},
          indent=2,
      )
  )


def cmd_thresholds(_args: argparse.Namespace) -> None:
  print(json.dumps(GATE_THRESHOLDS, indent=2))


def build_parser() -> argparse.ArgumentParser:
  parser = argparse.ArgumentParser(
      description="Eval & Observability Lab — score model runs and gate on quality metrics.",
      formatter_class=argparse.RawDescriptionHelpFormatter,
  )
  subparsers = parser.add_subparsers(dest="command", required=True)

  # run sub-command
  p = subparsers.add_parser("run", help="Evaluate a single named run.")
  p.add_argument(
      "--name",
      default="baseline",
      choices=list(RUNS),
      help="Run name to evaluate (default: baseline).",
  )
  p.set_defaults(func=cmd_run)

  # compare sub-command
  p = subparsers.add_parser("compare", help="Compare baseline vs candidate.")
  p.set_defaults(func=cmd_compare)

  # thresholds sub-command
  p = subparsers.add_parser("thresholds", help="Show release gate thresholds.")
  p.set_defaults(func=cmd_thresholds)

  return parser


def main() -> None:
  parser = build_parser()
  args = parser.parse_args()
  args.func(args)


if __name__ == "__main__":
  main()
