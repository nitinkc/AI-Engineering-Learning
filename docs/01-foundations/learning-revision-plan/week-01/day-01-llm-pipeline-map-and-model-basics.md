# Day 1 - LLM pipeline map and model basics

🟡 Intermediate

Pre-reading: [Week 1 Overview](./index.md) · [Learning and Revision Plan - Daily System](../index.md)

This page gives you one focused execution unit for today. You will align theory with implementation so your interview answers are backed by practical evidence and repeatable workflow habits.

## Learning Objectives

| Objective | Why it matters in interviews |
|---|---|
| Explain end-to-end LLM request flow | Demonstrates production-level reasoning and execution. |
| Compare base vs instruct models | Demonstrates production-level reasoning and execution. |
| Define context window and token limits | Demonstrates production-level reasoning and execution. |

## What to Learn

| Topic | Focus for today |
|---|---|
| Transformer components at a practical level | Understand enough to explain tradeoffs clearly. |
| Prompt-response lifecycle in an app | Understand enough to explain tradeoffs clearly. |
| Tokenization impact on cost and quality | Understand enough to explain tradeoffs clearly. |
| When to choose API models vs hosted models | Understand enough to explain tradeoffs clearly. |

## Theory to Practice

| Practice drill | Expected output |
|---|---|
| Draw architecture of a chat app with LLM | Short working note or runnable artifact. |
| Inspect token counts on 10 sample prompts | Short working note or runnable artifact. |
| Write a model selection note for one use case | Short working note or runnable artifact. |

## Labs to Practice

| Lab | Task | Deliverable |
|---|---|---|
| Token Budget Drill | Estimate and validate token usage for 5 real prompts | CSV with prompt, tokens, estimated cost |
| Architecture Sketch | Create one-page system diagram for LLM app flow | PNG or Mermaid diagram |

## Today's Material

| Start here | Why today |
|---|---|
| [Daily Material Map](../../../05-ai-engineer-playbook/08-daily-material-map.md) | Shows the exact Week 1 sequence and artifact for Day 1. |
| [01 Learning Path](../../../05-ai-engineer-playbook/01-learning-path.md) | Use the pipeline map, token budget walkthrough, and prompt-builder example. |
| [Week 1 RAG Foundations Lab](../../../06-mini-projects/01-week-1-rag-foundations-lab.md) | Follow the Day 1 modification guidance before moving to labs. |

## Starter Code and Assets

| Asset | Use it for |
|---|---|
| [week01_rag_foundations_lab.py](../../../06-mini-projects/code/week01_rag_foundations_lab.py) | Run the prompt builder and token estimate baseline. |
| [week01_sample_corpus.json](../../../06-mini-projects/code/week01_sample_corpus.json) | Inspect the small corpus and relate it to your architecture sketch. |

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

??? question "Interview Q: How does Day 1 connect to production outcomes?"
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
