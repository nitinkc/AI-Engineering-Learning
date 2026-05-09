# Day 2 - Prompting patterns and guardrails

🟡 Intermediate

Pre-reading: [Week 1 Overview](./index.md) · [Learning and Revision Plan - Daily System](../index.md)

This page gives you one focused execution unit for today. You will align theory with implementation so your interview answers are backed by practical evidence and repeatable workflow habits.

## Learning Objectives

| Objective | Why it matters in interviews |
|---|---|
| Use reusable prompt templates | Demonstrates production-level reasoning and execution. |
| Reduce hallucinations with constraints | Demonstrates production-level reasoning and execution. |
| Apply structured output patterns | Demonstrates production-level reasoning and execution. |

## What to Learn

| Topic | Focus for today |
|---|---|
| Role and instruction layering | Understand enough to explain tradeoffs clearly. |
| Few-shot examples for format stability | Understand enough to explain tradeoffs clearly. |
| JSON schema prompting basics | Understand enough to explain tradeoffs clearly. |
| Prompt anti-patterns to avoid | Understand enough to explain tradeoffs clearly. |

## Theory to Practice

| Practice drill | Expected output |
|---|---|
| Refactor weak prompts into templates | Short working note or runnable artifact. |
| Add explicit refusal and uncertainty rules | Short working note or runnable artifact. |
| Test output validity against JSON schema | Short working note or runnable artifact. |

## Labs to Practice

| Lab | Task | Deliverable |
|---|---|---|
| Prompt Rewrite Sprint | Rewrite 8 noisy prompts into robust templates | Prompt library file with before-after pairs |
| Schema Output Test | Generate structured responses for 20 inputs | Pass rate report and failed cases |

## Today's Material

| Start here | Why today |
|---|---|
| [Daily Material Map](../../../05-ai-engineer-playbook/08-daily-material-map.md) | Shows the exact Week 1 sequence and artifact for Day 2. |
| [01 Learning Path](../../../05-ai-engineer-playbook/01-learning-path.md) | Use the prompt-builder example and the step-by-step foundations flow. |
| [Week 1 RAG Foundations Lab](../../../06-mini-projects/01-week-1-rag-foundations-lab.md) | Apply refusal and grounding constraints to the starter project. |

## Starter Code and Assets

| Asset | Use it for |
|---|---|
| [week01_rag_foundations_lab.py](../../../06-mini-projects/code/week01_rag_foundations_lab.py) | Strengthen the system prompt and add output constraints. |
| [week01_sample_corpus.json](../../../06-mini-projects/code/week01_sample_corpus.json) | Test prompt behavior on multiple document sources. |

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

??? question "Interview Q: How does Day 2 connect to production outcomes?"
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
