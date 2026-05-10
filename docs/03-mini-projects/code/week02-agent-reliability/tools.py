"""Tools — schemas and stub implementations for each supported tool.

Each tool is a plain function that accepts a validated payload dict and returns
a result dict.  In a real system these would call external APIs.
"""
from __future__ import annotations

TOOL_SCHEMAS: dict[str, dict] = {
  "search_kb": {
    "name": "search_kb",
    "risk_level": "low",
    "required_fields": ["query"],
    "description": "Search the internal knowledge base.",
  },
  "update_ticket": {
    "name": "update_ticket",
    "risk_level": "low",
    "required_fields": ["ticket_id", "status"],
    "description": "Update the status of a support ticket.",
  },
  "cancel_subscription": {
    "name": "cancel_subscription",
    "risk_level": "high",
    "required_fields": ["subscription_id"],
    "description": "Cancel an active subscription (irreversible — requires approval).",
  },
}


def search_kb(payload: dict) -> dict:
  """Stub: return a fake KB article for the given query."""
  return {"articles": [f"KB: {payload.get('query', 'unknown')}"]}


def update_ticket(payload: dict) -> dict:
  """Stub: acknowledge ticket status change."""
  return {
    "ticket_id": payload["ticket_id"],
    "new_status": payload["status"],
    "updated": True,
  }


def cancel_subscription(payload: dict) -> dict:
  """Stub: mark a subscription as cancelled."""
  return {
    "subscription_id": payload["subscription_id"],
    "cancelled": True,
  }


TOOL_REGISTRY: dict[str, object] = {
  "search_kb": search_kb,
  "update_ticket": update_ticket,
  "cancel_subscription": cancel_subscription,
}
