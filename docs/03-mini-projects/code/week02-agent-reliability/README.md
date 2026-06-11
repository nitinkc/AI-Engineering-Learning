# Week 02 — Agent Reliability Lab

A self-contained Python project demonstrating **agentic workflow reliability**: tool schema
validation, approval gates for high-risk actions, retry logic with trace logging, and escalation on
budget exhaustion.

## Project Structure

```
week02-agent-reliability/
├── __init__.py
├── tools.py         # Tool schemas and stub implementations
├── agent.py         # Validation, approval gate, retry loop, trace logging
├── cli.py           # Argparse CLI (search_kb / update_ticket / cancel_subscription)
├── requirements.txt
└── tests/
    └── test_agent.py  # 12 unit tests (pytest)
```

## Quick Start

```bash
# From this directory — no install needed

# Cancel a subscription (high-risk, prompts approval gate):
04-python cli.py cancel_subscription --user-id user-42 --subscription-id sub-101

# Search KB (low-risk, no gate):
04-python cli.py search_kb --user-id user-7 --query "password reset procedure"

# Simulate a retry:
04-python cli.py cancel_subscription --user-id user-42 --subscription-id sub-101 --fail-once

# Reject the approval gate:
04-python cli.py cancel_subscription --user-id user-42 --subscription-id sub-101 --no-approve
```

## Running Tests

```bash
04-python -m pytest tests/ -v
```

## Key Concepts Covered

| Concept       | Module     | Description                                                       |
|---------------|------------|-------------------------------------------------------------------|
| Tool schemas  | `tools.py` | Structured input contracts per tool                               |
| Validation    | `agent.py` | Pre-flight checks: unknown tool, missing fields                   |
| Approval gate | `agent.py` | High-risk actions blocked until approved                          |
| Retry + trace | `agent.py` | Up to MAX_RETRIES with step-by-step trace                         |
| Escalation    | `agent.py` | Elevates to human when retry budget exhausted                     |
| CLI           | `cli.py`   | Sub-commands: `search_kb`, `update_ticket`, `cancel_subscription` |

## Requirements

- Python 3.9+
- No external dependencies (stdlib only)
