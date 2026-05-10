"""Tests for the Eval & Observability Lab."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest

from evaluator import (
  EVAL_SET,
  GATE_THRESHOLDS,
  evaluate_run,
  release_gate,
  score_response,
  summarize_run,
)
from tracer import Trace, timed_span


# ---------------------------------------------------------------------------
# score_response
# ---------------------------------------------------------------------------

class TestScoreResponse:
  def test_full_match(self):
    assert score_response("identity security portal",
                          ["identity", "security", "portal"]) == 1.0

  def test_partial_match(self):
    s = score_response("identity only", ["identity", "security", "portal"])
    assert s == round(1 / 3, 4)

  def test_no_match(self):
    assert score_response("completely unrelated",
                          ["identity", "security"]) == 0.0

  def test_empty_expected_returns_one(self):
    assert score_response("anything", []) == 1.0

  def test_case_insensitive(self):
    assert score_response("IDENTITY SECURITY PORTAL",
                          ["identity", "security", "portal"]) == 1.0


# ---------------------------------------------------------------------------
# evaluate_run
# ---------------------------------------------------------------------------

class TestEvaluateRun:
  def _good_responses(self) -> list[str]:
    return [
      "Use the security portal to verify identity and reset the expired API key.",
      "High risk requests require review and escalation to the security team.",
      "When retry budget is exhausted the system will escalate to a human reviewer.",
    ]

  def test_returns_expected_keys(self):
    result = evaluate_run("test", self._good_responses())
    assert {"run_name", "per_question", "faithfulness"}.issubset(result)

  def test_faithfulness_between_0_and_1(self):
    result = evaluate_run("test", self._good_responses())
    assert 0.0 <= result["faithfulness"] <= 1.0

  def test_per_question_count(self):
    result = evaluate_run("test", self._good_responses())
    assert len(result["per_question"]) == len(EVAL_SET)

  def test_wrong_response_count_raises(self):
    with pytest.raises(ValueError, match="responses"):
      evaluate_run("bad", ["only one response"])


# ---------------------------------------------------------------------------
# release_gate
# ---------------------------------------------------------------------------

class TestReleaseGate:
  def _passing(self) -> dict:
    return {
      "faithfulness": 0.90,
      "retrieval_hit_rate": 0.85,
      "latency_p95_ms": 3000,
      "cost_per_success": 0.05,
    }

  def test_passing_metrics_gate_true(self):
    assert release_gate(self._passing()) is True

  def test_failing_faithfulness_gate_false(self):
    m = {**self._passing(), "faithfulness": 0.70}
    assert release_gate(m) is False

  def test_failing_latency_gate_false(self):
    m = {**self._passing(), "latency_p95_ms": 9999}
    assert release_gate(m) is False

  def test_boundary_faithfulness_passes(self):
    m = {**self._passing(), "faithfulness": GATE_THRESHOLDS["faithfulness"]}
    assert release_gate(m) is True


# ---------------------------------------------------------------------------
# summarize_run
# ---------------------------------------------------------------------------

class TestSummarizeRun:
  def _metrics(self) -> dict:
    return {
      "faithfulness": 0.89,
      "retrieval_hit_rate": 0.84,
      "latency_p95_ms": 3100,
      "cost_per_success": 0.07,
    }

  def test_ship_true_when_passing(self):
    result = summarize_run("candidate", self._metrics())
    assert result["ship"] is True

  def test_ship_false_when_failing(self):
    m = {**self._metrics(), "faithfulness": 0.50}
    result = summarize_run("bad", m)
    assert result["ship"] is False

  def test_trace_status_pass(self):
    result = summarize_run("candidate", self._metrics())
    assert result["trace"]["status"] == "pass"

  def test_trace_status_fail(self):
    m = {**self._metrics(), "faithfulness": 0.50}
    result = summarize_run("bad", m)
    assert result["trace"]["status"] == "fail"


# ---------------------------------------------------------------------------
# Tracer
# ---------------------------------------------------------------------------

class TestTracer:
  def test_span_recorded(self):
    trace = Trace(trace_id="t-1")
    with timed_span(trace, "test_span"):
      pass
    assert len(trace.spans) == 1
    assert trace.spans[0].name == "test_span"

  def test_span_duration_positive(self):
    trace = Trace(trace_id="t-2")
    with timed_span(trace, "work"):
      _ = sum(range(1000))
    assert trace.spans[0].duration_ms >= 0

  def test_span_status_ok(self):
    trace = Trace(trace_id="t-3")
    with timed_span(trace, "ok_span"):
      pass
    assert trace.spans[0].status == "ok"

  def test_span_status_error_on_exception(self):
    trace = Trace(trace_id="t-4")
    with pytest.raises(RuntimeError):
      with timed_span(trace, "bad_span"):
        raise RuntimeError("boom")
    assert "error" in trace.spans[0].status

  def test_to_dict_includes_total_ms(self):
    trace = Trace(trace_id="t-5")
    with timed_span(trace, "s1"):
      pass
    d = trace.to_dict()
    assert "total_ms" in d
    assert d["total_ms"] >= 0
