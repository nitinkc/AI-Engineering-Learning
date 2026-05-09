# Day 5 - RAG quality debugging

🟡 Intermediate

Pre-reading: [Week 1 Overview](./index.md) · [Learning and Revision Plan - Daily System](../index.md)

This page gives you one focused execution unit for today. You will align theory with implementation so your interview answers are backed by practical evidence and repeatable workflow habits.

## Learning Objectives

| Objective | Why it matters in interviews |
|---|---|
| Diagnose bad answers quickly | Demonstrates production-level reasoning and execution. |
| Trace errors to retrieval or generation | Demonstrates production-level reasoning and execution. |
| Create repeatable debug checklist | Demonstrates production-level reasoning and execution. |

## What to Learn

| Topic | Focus for today |
|---|---|
| Golden set design for RAG | Understand enough to explain tradeoffs clearly. |
| Attribution checks for groundedness | Understand enough to explain tradeoffs clearly. |
| Prompt-context interaction pitfalls | Understand enough to explain tradeoffs clearly. |
| Regression testing for fixes | Understand enough to explain tradeoffs clearly. |

## Theory to Practice

| Practice drill | Expected output |
|---|---|
| Label failure cases by root cause | Short working note or runnable artifact. |
| Adjust chunking and prompt in controlled tests | Short working note or runnable artifact. |
| Track improvement across iterations | Short working note or runnable artifact. |

## Labs to Practice

| Lab | Task | Deliverable |
|---|---|---|
| Failure Taxonomy | Classify 30 failed answers into root-cause buckets | Annotated spreadsheet |
| Fix and Re-test | Apply two targeted fixes and re-run eval set | Before-after metrics summary |

## Today's Material

| Start here | Why today |
|---|---|
| [Daily Material Map](../../../05-ai-engineer-playbook/08-daily-material-map.md) | Shows the exact Week 1 sequence and artifact for Day 5. |
| [02 RAG Debugging and Quality](../../../05-ai-engineer-playbook/02-rag-debugging-quality.md) | Use the failure logging example and debugging sequence directly. |
| [07 Incremental Learning Labs](../../../05-ai-engineer-playbook/07-incremental-learning-labs.md) | Run Lab A to classify failures and propose fixes. |

## Starter Code and Assets

| Asset | Use it for |
|---|---|
| [week01_rag_foundations_lab.py](../../../06-mini-projects/code/week01_rag_foundations_lab.py) | Produce a failure and inspect retrieval artifacts before fixing it. |
| [Week 1 RAG Foundations Lab](../../../06-mini-projects/01-week-1-rag-foundations-lab.md) | Capture the matching lab outputs and turn one into a regression seed. |

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

??? question "Interview Q: How does Day 5 connect to production outcomes?"
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
