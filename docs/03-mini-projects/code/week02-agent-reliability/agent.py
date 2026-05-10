"""Agent — validation, approval gate, retry loop, and trace logging."""
from __future__ import annotations

from dataclasses import asdict, dataclass

from tools import TOOL_REGISTRY, TOOL_SCHEMAS

MAX_RETRIES = 2


@dataclass
class ToolRequest:
  tool_name: str
  user_id: str
  payload: dict
  idempotency_key: str
  risk_level: str = "low"


class ValidationError(ValueError):
  """Raised when a ToolRequest fails schema validation."""


def validate_request(request: ToolRequest) -> None:
  """Check that the request references a known tool with required fields.

  Raises:
      ValidationError: If the tool is unknown, user_id or idempotency_key is
          missing, or required payload fields are absent.
  """
  schema = TOOL_SCHEMAS.get(request.tool_name)
  if schema is None:
    raise ValidationError(f"Unknown tool: {request.tool_name!r}")
  if not request.user_id:
    raise ValidationError("user_id is required")
  if not request.idempotency_key:
    raise ValidationError("idempotency_key is required")
  for field in schema.get("required_fields", []):
    if field not in request.payload:
      raise ValidationError(f"Missing required payload field: {field!r}")


def execute_workflow(
    request: ToolRequest,
    *,
    approved: bool = True,
    fail_once: bool = False,
) -> dict:
  """Execute a tool request with validation, approval gate, retry, and trace.

  Args:
      request: The tool call to execute.
      approved: Whether a human approver has authorised high-risk actions.
      fail_once: If True, the first execution attempt raises a simulated timeout
                 so the retry logic can be exercised.

  Returns:
      A trace dict with keys: status, attempts (int), trace (list of step dicts).
  """
  trace: list[dict] = []

  validate_request(request)
  trace.append({"step": "validated", "request": asdict(request)})

  if request.risk_level == "high":
    trace.append({"step": "approval_required", "approved": approved})
    if not approved:
      return {"status": "cancelled", "attempts": 0, "trace": trace}

  tool_fn = TOOL_REGISTRY[request.tool_name]

  for attempt in range(1, MAX_RETRIES + 1):
    trace.append({"step": "execute", "attempt": attempt})
    if fail_once and attempt == 1:
      trace.append({"step": "retryable_failure", "reason": "timeout"})
      continue
    result = tool_fn(request.payload)
    trace.append({"step": "verify", "result": result})
    return {"status": "completed", "attempts": attempt, "trace": trace}

  trace.append({"step": "escalate", "reason": "retry_budget_exhausted"})
  return {"status": "escalated", "attempts": MAX_RETRIES, "trace": trace}
