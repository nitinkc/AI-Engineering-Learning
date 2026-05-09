# Day 9 - Planning, memory, and state management

🟡 Intermediate

Pre-reading: [Week 2 Overview](./index.md) · [Learning and Revision Plan - Daily System](../index.md)

This page gives you one focused execution unit for today. You will align theory with implementation so your interview answers are backed by practical evidence and repeatable workflow habits.

## Learning Objectives

| Objective | Why it matters in interviews |
|---|---|
| Implement short-term and long-term memory | Demonstrates production-level reasoning and execution. |
| Track agent state explicitly | Demonstrates production-level reasoning and execution. |
| Prevent context drift | Demonstrates production-level reasoning and execution. |

## What to Learn

| Topic | Focus for today |
|---|---|
| Conversation memory strategies | Understand enough to explain tradeoffs clearly. |
| Task decomposition methods | Understand enough to explain tradeoffs clearly. |
| State snapshots and checkpoints | Understand enough to explain tradeoffs clearly. |
| Memory compaction techniques | Understand enough to explain tradeoffs clearly. |

## Theory to Practice

| Practice drill | Expected output |
|---|---|
| Store and retrieve task context safely | Short working note or runnable artifact. |
| Use explicit state objects in code | Short working note or runnable artifact. |
| Validate memory relevance per turn | Short working note or runnable artifact. |

## Labs to Practice

| Lab | Task | Deliverable |
|---|---|---|
| Stateful Agent Loop | Implement planner with persistent state across steps | State transition log and code |
| Memory Prune Test | Add memory pruning and compare response quality | Ablation note with examples |

## Today's Material

| Start here | Why today |
|---|---|
| [Daily Material Map](../../../05-ai-engineer-playbook/08-daily-material-map.md) | Shows the exact Week 2 sequence and artifact for Day 9. |
| [03 Agentic Workflows](../../../05-ai-engineer-playbook/03-agentic-workflows.md) | Use the stateful workflow example and day-alignment table. |
| [Week 2 Agent Reliability Lab](../../../06-mini-projects/02-week-2-agent-reliability-lab.md) | Add or inspect state fields while tracing workflow execution. |

## Starter Code and Assets

| Asset | Use it for |
|---|---|
| [week02_agent_reliability_lab.py](../../../06-mini-projects/code/week02_agent_reliability_lab.py) | Track how approval, attempts, and status evolve in the state. |
| [03 Agentic Workflows](../../../05-ai-engineer-playbook/03-agentic-workflows.md) | Use the step-by-step agent build flow as your checklist. |

## Daily Execution Flow

```mermaid
graph LR
    A["Refresh Key Concept"] --> B["Do Theory Drill"]
    B --> C["Run Lab 1"]
    C --> D["Run Lab 2"]
    D --> E["Capture Interview Notes"]

    style A fill:#1976d2,color:#fff
    style C fill:#ff9800,color:#fff
    style E fill:#2e7d32,color:#fff
```

??? question "Interview Q: What did you improve today and why?"
    **Model Answer:**
    I improved reliability by making one measurable change to the pipeline and validating it with a focused test set. I can explain the baseline issue, the change, and the observed impact in quality, latency, or cost.

    **Why this matters:**
    Interviewers look for evidence-driven improvement, not generic claims.

??? question "Interview Q: How does Day 9 connect to production outcomes?"
    **Model Answer:**
    The work done today reduces operational risk and improves repeatability. It gives me artifacts like traces, configs, and evaluation notes that I can use to justify architecture choices.

    **Why this matters:**
    Strong candidates connect technical activity to reliability, user experience, and business impact.

## End-of-Day Checklist

| Item | Status |
|---|---|
| Theory drills completed | ☐ |
| Both labs run and documented | ☐ |
| One 60-second interview answer recorded | ☐ |
| One weak area logged for revision | ☐ |

--8<-- "_abbreviations.md"
