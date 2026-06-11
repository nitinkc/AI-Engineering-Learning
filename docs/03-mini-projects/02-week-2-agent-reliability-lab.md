# Week 2 Mini Project - Agent Reliability Lab

Pre-reading: [02 Agentic Workflows](../01-foundations/02-agentic-workflows.md)

This mini project gives Week 2 a stateful workflow you can inspect and extend. It models schema
validation, approval gates, retries, escalation, and trace logging using deterministic Python so you
can focus on reliability behavior before adding an LLM.

Run the commands below from an activated project venv.

## What You Will Build

| Capability             | Output                         |
|------------------------|--------------------------------|
| Tool schema validation | Safe tool invocation checks    |
| Approval gate          | High-risk action control       |
| Retry policy           | Recoverable failure handling   |
| Escalation path        | Non-retryable outcome          |
| Trace log              | Step-by-step execution history |

## How to Run

```bash
cd docs/03-mini-projects/code/week02-agent-reliability

# High-risk action with approval gate
python cli.py cancel_subscription --user-id user-42 --subscription-id sub-101

# Simulate retry path
python cli.py cancel_subscription --user-id user-42 --subscription-id sub-101 --fail-once

# Run tests
python -m pytest tests/ -v
```

## Portfolio Structure

```text
code/week02-agent-reliability/
├── tools.py
├── agent.py
├── cli.py
└── tests/test_agent.py
```

## What to Modify Across the Week

| Day    | Suggested change                                     |
|--------|------------------------------------------------------|
| Day 8  | Add or remove one tool from the registry.            |
| Day 9  | Add one state field and trace how it changes.        |
| Day 10 | Draw the workflow as graph nodes and edges.          |
| Day 11 | Split one step into supervisor and worker roles.     |
| Day 12 | Tighten approval rules for risky actions.            |
| Day 13 | Force more failures and compare retry vs escalation. |
| Day 14 | Write the architecture brief from your final trace.  |

## Starter Assets

| Asset                                                                                             | Purpose                                              |
|---------------------------------------------------------------------------------------------------|------------------------------------------------------|
| [week02-agent-reliability/cli.py](code/week02-agent-reliability/cli.py)                           | CLI entry point for tool workflows                   |
| [week02-agent-reliability/tools.py](code/week02-agent-reliability/tools.py)                       | Tool schemas and stub implementations                |
| [week02-agent-reliability/agent.py](code/week02-agent-reliability/agent.py)                       | Validation, approval, retry, and escalation workflow |
| [week02-agent-reliability/tests/test_agent.py](code/week02-agent-reliability/tests/test_agent.py) | Unit tests for reliability controls                  |
| [week02_agent_reliability_output.json](output/week02_agent_reliability_output.json)               | Sample trace showing approval, retry, and success    |

## Matching Lab Outputs

| Output                        | Why keep it                                      |
|-------------------------------|--------------------------------------------------|
| Trace log                     | Lets you explain state transitions in interviews |
| Tool schema notes             | Documents control boundaries                     |
| Approval and escalation paths | Shows safety design                              |
| Failure matrix                | Feeds Week 2 review and Week 4 stories           |

## Portfolio Checklist

| Item                                                       | Done? |
|------------------------------------------------------------|-------|
| Save one approved high-risk flow trace.                    | [ ]   |
| Save one denied approval trace and expected behavior note. | [ ]   |
| Save one retry-to-success trace with attempt counts.       | [ ]   |
| Write one STAR-ready bullet on reliability guardrails.     | [ ]   |

--8<-- "_abbreviations.md"
