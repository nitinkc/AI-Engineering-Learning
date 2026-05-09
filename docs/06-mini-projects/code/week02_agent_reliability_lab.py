from __future__ import annotations

import json
from dataclasses import asdict, dataclass


@dataclass
class ToolRequest:
    tool_name: str
    user_id: str
    payload: dict
    idempotency_key: str
    risk_level: str = "low"


def validate_request(request: ToolRequest) -> None:
    if request.tool_name not in {"search_kb", "update_ticket", "cancel_subscription"}:
        raise ValueError("Unknown tool")
    if not request.user_id:
        raise ValueError("user_id is required")
    if not request.idempotency_key:
        raise ValueError("idempotency_key is required")


def execute_workflow(request: ToolRequest, approved: bool = True, fail_once: bool = True) -> dict:
    trace = []
    validate_request(request)
    trace.append({"step": "validated", "request": asdict(request)})

    if request.risk_level == "high":
        trace.append({"step": "approval_required", "approved": approved})
        if not approved:
            return {"status": "cancelled", "trace": trace}

    attempts = 0
    while attempts < 2:
        attempts += 1
        trace.append({"step": "execute", "attempt": attempts})
        if fail_once and attempts == 1:
            trace.append({"step": "retryable_failure", "reason": "timeout"})
            continue
        trace.append({"step": "verify", "result": "success"})
        return {"status": "completed", "attempts": attempts, "trace": trace}

    trace.append({"step": "escalate", "reason": "retry_budget_exhausted"})
    return {"status": "escalated", "attempts": attempts, "trace": trace}


def main() -> None:
    request = ToolRequest(
        tool_name="cancel_subscription",
        user_id="user-42",
        payload={"subscription_id": "sub-101"},
        idempotency_key="cancel-sub-101-user-42",
        risk_level="high",
    )
    result = execute_workflow(request=request, approved=True, fail_once=True)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
