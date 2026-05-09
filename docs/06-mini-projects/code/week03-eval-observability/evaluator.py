"""Evaluator — golden dataset, metric scoring, and release gate."""
from __future__ import annotations

EVAL_SET: list[dict] = [
    {
        "question": "How do I reset an expired API key?",
        "expected_terms": ["identity", "security", "portal"],
    },
    {
        "question": "When should a request be escalated?",
        "expected_terms": ["high", "risk", "review"],
    },
    {
        "question": "What happens after retry budget is exhausted?",
        "expected_terms": ["escalate", "human", "budget"],
    },
]

# Thresholds for the release gate
GATE_THRESHOLDS: dict[str, float] = {
    "faithfulness": 0.85,
    "retrieval_hit_rate": 0.80,
    "latency_p95_ms": 3500,   # upper bound
    "cost_per_success": 0.08,  # upper bound (USD)
}


def score_response(response: str, expected_terms: list[str]) -> float:
    """Compute term coverage: fraction of expected_terms present in response."""
    if not expected_terms:
        return 1.0
    lowered = response.lower()
    matched = sum(1 for term in expected_terms if term in lowered)
    return round(matched / len(expected_terms), 4)


def evaluate_run(run_name: str, responses: list[str]) -> dict:
    """Score a list of model responses against the golden eval set.

    Args:
        run_name: Identifier for this model version / prompt version.
        responses: One response string per eval set entry (same order).

    Returns:
        Dict with per-question scores and aggregated faithfulness.
    """
    if len(responses) != len(EVAL_SET):
        raise ValueError(
            f"Expected {len(EVAL_SET)} responses, got {len(responses)}"
        )

    per_question = []
    total_score = 0.0
    for item, response in zip(EVAL_SET, responses):
        s = score_response(response, item["expected_terms"])
        total_score += s
        per_question.append(
            {
                "question": item["question"],
                "expected_terms": item["expected_terms"],
                "score": s,
            }
        )

    return {
        "run_name": run_name,
        "per_question": per_question,
        "faithfulness": round(total_score / len(EVAL_SET), 4),
    }


def release_gate(metrics: dict) -> bool:
    """Return True if all metrics satisfy the release thresholds."""
    return (
        metrics.get("faithfulness", 0) >= GATE_THRESHOLDS["faithfulness"]
        and metrics.get("retrieval_hit_rate", 0) >= GATE_THRESHOLDS["retrieval_hit_rate"]
        and metrics.get("latency_p95_ms", 9999) <= GATE_THRESHOLDS["latency_p95_ms"]
        and metrics.get("cost_per_success", 9999) <= GATE_THRESHOLDS["cost_per_success"]
    )


def summarize_run(run_name: str, metrics: dict) -> dict:
    """Bundle metrics with a ship/no-ship decision and trace metadata."""
    ship = release_gate(metrics)
    return {
        "name": run_name,
        "metrics": metrics,
        "ship": ship,
        "trace": {
            "prompt_version": f"{run_name}-prompt-v1",
            "model": "gpt-4.1-mini",
            "latency_ms": metrics.get("latency_p95_ms"),
            "status": "pass" if ship else "fail",
        },
    }
