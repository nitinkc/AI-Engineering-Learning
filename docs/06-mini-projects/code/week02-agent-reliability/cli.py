"""CLI entry point for the Agent Reliability Lab.

Usage examples
--------------
  # Cancel a subscription (high-risk, approval required):
  python cli.py cancel_subscription --user-id user-42 --subscription-id sub-101

  # Search the knowledge base (low-risk, no approval):
  python cli.py search_kb --user-id user-7 --query "password reset procedure"

  # Simulate a retry by injecting a first-attempt failure:
  python cli.py cancel_subscription --user-id user-42 --subscription-id sub-101 --fail-once

  # Reject the approval gate:
  python cli.py cancel_subscription --user-id user-42 --subscription-id sub-101 --no-approve
"""
from __future__ import annotations

import argparse
import json
import sys

from agent import ToolRequest, ValidationError, execute_workflow


def _make_idempotency_key(tool_name: str, user_id: str, payload: dict) -> str:
    parts = [tool_name, user_id] + [f"{k}-{v}" for k, v in sorted(payload.items())]
    return "-".join(parts)


def cmd_search_kb(args: argparse.Namespace) -> dict:
    payload = {"query": args.query}
    request = ToolRequest(
        tool_name="search_kb",
        user_id=args.user_id,
        payload=payload,
        idempotency_key=_make_idempotency_key("search_kb", args.user_id, payload),
        risk_level="low",
    )
    return execute_workflow(request, approved=True, fail_once=args.fail_once)


def cmd_update_ticket(args: argparse.Namespace) -> dict:
    payload = {"ticket_id": args.ticket_id, "status": args.status}
    request = ToolRequest(
        tool_name="update_ticket",
        user_id=args.user_id,
        payload=payload,
        idempotency_key=_make_idempotency_key("update_ticket", args.user_id, payload),
        risk_level="low",
    )
    return execute_workflow(request, approved=True, fail_once=args.fail_once)


def cmd_cancel_subscription(args: argparse.Namespace) -> dict:
    payload = {"subscription_id": args.subscription_id}
    request = ToolRequest(
        tool_name="cancel_subscription",
        user_id=args.user_id,
        payload=payload,
        idempotency_key=_make_idempotency_key("cancel_subscription", args.user_id, payload),
        risk_level="high",
    )
    return execute_workflow(
        request,
        approved=not args.no_approve,
        fail_once=args.fail_once,
    )


def _add_common_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--user-id", required=True, help="Requesting user ID.")
    parser.add_argument(
        "--fail-once",
        action="store_true",
        help="Simulate a first-attempt timeout to exercise retry logic.",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Agent Reliability Lab — tool execution with validation, approval, and retry.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # search_kb
    p = subparsers.add_parser("search_kb", help="Search the knowledge base.")
    _add_common_args(p)
    p.add_argument("--query", required=True, help="Search query string.")
    p.set_defaults(func=cmd_search_kb)

    # update_ticket
    p = subparsers.add_parser("update_ticket", help="Update a support ticket status.")
    _add_common_args(p)
    p.add_argument("--ticket-id", required=True, dest="ticket_id")
    p.add_argument("--status", required=True, choices=["open", "in_progress", "resolved"])
    p.set_defaults(func=cmd_update_ticket)

    # cancel_subscription
    p = subparsers.add_parser("cancel_subscription", help="Cancel a subscription (high-risk).")
    _add_common_args(p)
    p.add_argument("--subscription-id", required=True, dest="subscription_id")
    p.add_argument(
        "--no-approve",
        action="store_true",
        help="Reject the approval gate (simulates denied authorisation).",
    )
    p.set_defaults(func=cmd_cancel_subscription)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    try:
        result = args.func(args)
        print(json.dumps(result, indent=2))
    except ValidationError as exc:
        print(f"Validation error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
