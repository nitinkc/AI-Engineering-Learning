"""Tests for the Agent Reliability Lab."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest

from agent import ToolRequest, ValidationError, execute_workflow, validate_request


# ---------------------------------------------------------------------------
# validate_request
# ---------------------------------------------------------------------------

class TestValidateRequest:
    def _good(self, **kwargs) -> ToolRequest:
        defaults = dict(
            tool_name="search_kb",
            user_id="user-1",
            payload={"query": "reset"},
            idempotency_key="key-1",
            risk_level="low",
        )
        defaults.update(kwargs)
        return ToolRequest(**defaults)

    def test_valid_passes(self):
        validate_request(self._good())  # no exception

    def test_unknown_tool_raises(self):
        with pytest.raises(ValidationError, match="Unknown tool"):
            validate_request(self._good(tool_name="nonexistent"))

    def test_missing_user_id_raises(self):
        with pytest.raises(ValidationError, match="user_id"):
            validate_request(self._good(user_id=""))

    def test_missing_idempotency_key_raises(self):
        with pytest.raises(ValidationError, match="idempotency_key"):
            validate_request(self._good(idempotency_key=""))

    def test_missing_required_payload_field_raises(self):
        with pytest.raises(ValidationError, match="query"):
            validate_request(self._good(tool_name="search_kb", payload={}))


# ---------------------------------------------------------------------------
# execute_workflow
# ---------------------------------------------------------------------------

class TestExecuteWorkflow:
    def _cancel_request(self, risk_level: str = "high") -> ToolRequest:
        return ToolRequest(
            tool_name="cancel_subscription",
            user_id="user-42",
            payload={"subscription_id": "sub-101"},
            idempotency_key="cancel-sub-101-user-42",
            risk_level=risk_level,
        )

    def _search_request(self) -> ToolRequest:
        return ToolRequest(
            tool_name="search_kb",
            user_id="user-7",
            payload={"query": "reset password"},
            idempotency_key="search-reset-user-7",
            risk_level="low",
        )

    def test_approved_high_risk_completes(self):
        result = execute_workflow(self._cancel_request(), approved=True, fail_once=False)
        assert result["status"] == "completed"

    def test_denied_high_risk_cancels(self):
        result = execute_workflow(self._cancel_request(), approved=False)
        assert result["status"] == "cancelled"

    def test_retry_on_fail_once(self):
        result = execute_workflow(self._cancel_request(), approved=True, fail_once=True)
        assert result["status"] == "completed"
        assert result["attempts"] == 2

    def test_escalate_after_budget_exhausted(self):
        # Patch MAX_RETRIES to 1 so one fail triggers escalation
        import agent as agent_mod
        orig = agent_mod.MAX_RETRIES
        agent_mod.MAX_RETRIES = 1
        try:
            result = execute_workflow(self._cancel_request(), approved=True, fail_once=True)
            assert result["status"] == "escalated"
        finally:
            agent_mod.MAX_RETRIES = orig

    def test_low_risk_skips_approval(self):
        result = execute_workflow(self._search_request(), approved=False, fail_once=False)
        assert result["status"] == "completed"
        steps = [step["step"] for step in result["trace"]]
        assert "approval_required" not in steps

    def test_trace_contains_validated_step(self):
        result = execute_workflow(self._search_request())
        steps = [step["step"] for step in result["trace"]]
        assert "validated" in steps

    def test_trace_contains_verify_on_success(self):
        result = execute_workflow(self._search_request(), fail_once=False)
        steps = [step["step"] for step in result["trace"]]
        assert "verify" in steps
