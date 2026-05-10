from __future__ import annotations

import json

EVAL_SET = [
  {
    "question": "How do I reset an expired API key?",
    "expected_terms": ["identity", "security", "portal"],
  },
  {
    "question": "When should a request be escalated?",
    "expected_terms": ["high", "risk", "review"],
  },
]


def release_gate(metrics: dict) -> bool:
  return (
      metrics["faithfulness"] >= 0.85
      and metrics["retrieval_hit_rate"] >= 0.80
      and metrics["latency_p95_ms"] <= 3500
      and metrics["cost_per_success"] <= 0.08
  )


def summarize_run(name: str, metrics: dict) -> dict:
  return {
    "name": name,
    "metrics": metrics,
    "ship": release_gate(metrics),
    "trace": {
      "prompt_version": f"{name}-prompt-v1",
      "model": "gpt-4.1-mini",
      "latency_ms": metrics["latency_p95_ms"],
      "status": "pass" if release_gate(metrics) else "fail",
    },
  }


def main() -> None:
  baseline = summarize_run(
      "baseline",
      {
        "faithfulness": 0.82,
        "retrieval_hit_rate": 0.78,
        "latency_p95_ms": 3300,
        "cost_per_success": 0.06,
      },
  )
  candidate = summarize_run(
      "candidate",
      {
        "faithfulness": 0.89,
        "retrieval_hit_rate": 0.84,
        "latency_p95_ms": 3100,
        "cost_per_success": 0.07,
      },
  )
  print(
    json.dumps({"eval_set": EVAL_SET, "runs": [baseline, candidate]}, indent=2))


if __name__ == "__main__":
  main()
