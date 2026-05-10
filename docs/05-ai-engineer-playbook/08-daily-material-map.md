# 08 - Daily Material Map for the 28-Day Plan

> **Level:** Intermediate
> **Pre-reading:** [Daily Learning Plan](../01-foundations/learning-revision-plan/index.md) · [01 Learning Path Companion](01-learning-path.md) · [07 Incremental Learning Labs](07-incremental-learning-labs.md)

---

This page turns the 28-day schedule into a usable study path. For each day, it points you to the exact supporting material, the example code to adapt, and the artifact you should produce by the end of the session.

```mermaid
graph LR
    A[Daily Plan] --> B[Playbook Module]
    B --> C[Code or Lab]
    C --> D[Artifact]
    D --> E[Interview Recall]

    style A fill:#1976d2,color:#fff
    style C fill:#ff9800,color:#fff
    style E fill:#2e7d32,color:#fff
```

## Week 1 - Foundations, RAG, and Retrieval

| Day | Focus | Primary material | Code or lab to use | End-of-day artifact |
|---|---|---|---|---|
| 1 | LLM pipeline map and model basics | [01 Learning Path](01-learning-path.md) | Prompt Builder and Token Budget | System diagram |
| 2 | Prompting patterns and guardrails | [01 Learning Path](01-learning-path.md) | Prompt Builder and Token Budget | Prompt template library |
| 3 | Embeddings and retrieval basics | [02 RAG Debugging and Quality](02-rag-debugging-quality.md) | Minimal Grounded Retrieval Prototype | Chunking experiment note |
| 4 | RAG architecture and grounding | [02 RAG Debugging and Quality](02-rag-debugging-quality.md) | Minimal Grounded Retrieval Prototype | Grounded QA script |
| 5 | RAG quality debugging | [02 RAG Debugging and Quality](02-rag-debugging-quality.md) | Failure Logging for RAG Debugging | Root-cause table |
| 6 | Multimodal and long-context strategies | [01 Learning Path](01-learning-path.md) | Long-Context Map-Reduce Scaffold | Long-doc summary scaffold |
| 7 | Consolidation and retrieval drill | [07 Incremental Learning Labs](07-incremental-learning-labs.md) | Lab A or Lab B | One-page debugging checklist |

## Week 2 - Agents, LangGraph, and Reliability

| Day | Focus | Primary material | Code or lab to use | End-of-day artifact |
|---|---|---|---|---|
| 8 | Agentic patterns and tool calling | [03 Agentic Workflows](03-agentic-workflows.md) | Tool Contract and Validator | Tool schema set |
| 9 | Planning, memory, and state management | [03 Agentic Workflows](03-agentic-workflows.md) | Stateful Workflow with Retry and Approval | State transition sketch |
| 10 | LangGraph fundamentals | [03 Agentic Workflows](03-agentic-workflows.md) | Stateful Workflow with Retry and Approval | Node-edge graph draft |
| 11 | Multi-agent coordination | [03 Agentic Workflows](03-agentic-workflows.md) | Supervisor-worker adaptation of workflow example | Multi-agent handoff design |
| 12 | Human-in-the-loop and approvals | [03 Agentic Workflows](03-agentic-workflows.md) | Stateful Workflow with Retry and Approval | Approval gate path |
| 13 | Reliability hardening for agents | [03 Agentic Workflows](03-agentic-workflows.md) + [07 Incremental Learning Labs](07-incremental-learning-labs.md) | Tool Reliability Sprint | Failure matrix |
| 14 | Consolidation and design review | [03 Agentic Workflows](03-agentic-workflows.md) + [07 Incremental Learning Labs](07-incremental-learning-labs.md) | Lab C output review | Architecture brief |

## Week 3 - Evals, Observability, and Production

| Day | Focus | Primary material | Code or lab to use | End-of-day artifact |
|---|---|---|---|---|
| 15 | Eval strategy and datasets | [04 Evals, Observability, and Production](04-evals-observability-production.md) | Tiny Eval Dataset and Gate | Starter eval set |
| 16 | Automated eval pipelines | [04 Evals, Observability, and Production](04-evals-observability-production.md) | Tiny Eval Dataset and Gate | Release gate policy |
| 17 | Observability and tracing | [04 Evals, Observability, and Production](04-evals-observability-production.md) | Structured Trace Record | Trace example |
| 18 | Safety and policy controls | [04 Evals, Observability, and Production](04-evals-observability-production.md) | Observability Checklist plus safety notes | Safety middleware checklist |
| 19 | Deployment, scaling, and SLOs | [04 Evals, Observability, and Production](04-evals-observability-production.md) | Release gate plus reliability checklist | SLO and rollout note |
| 20 | Postmortems and continuous improvement | [04 Evals, Observability, and Production](04-evals-observability-production.md) | Release gate retrospective | Postmortem draft |
| 21 | Readiness review | [04 Evals, Observability, and Production](04-evals-observability-production.md) + [07 Incremental Learning Labs](07-incremental-learning-labs.md) | Lab D and readiness checklist | Production scorecard |

## Week 4 - Portfolio, Stories, and Mock Loops

| Day | Focus | Primary material | Code or lab to use | End-of-day artifact |
|---|---|---|---|---|
| 22 | Role targeting and competency mapping | [05 STAR Story System](05-star-story-system.md) | Role-to-Evidence Matrix | Competency matrix |
| 23 | STAR story bank | [05 STAR Story System](05-star-story-system.md) | Story Card template | Six story draft |
| 24 | Portfolio assembly and narrative | [05 STAR Story System](05-star-story-system.md) | Story Card plus case-study framing | Case-study outline |
| 25 | Technical interview drills | [06 Interview Sprint Loops](06-interview-sprints-and-mock-loops.md) | 90-Second Drill Runner | Drill score sheet |
| 26 | Behavioral and cross-functional communication | [06 Interview Sprint Loops](06-interview-sprints-and-mock-loops.md) | Example Scorecard and stakeholder rewrite | Behavioral answer sheet |
| 27 | Full mock loop and feedback integration | [06 Interview Sprint Loops](06-interview-sprints-and-mock-loops.md) + [07 Incremental Learning Labs](07-incremental-learning-labs.md) | Lab E and mock loop | Revision log |
| 28 | Final synthesis and launch plan | [06 Interview Sprint Loops](06-interview-sprints-and-mock-loops.md) | Step-by-Step Mock Loop Runbook | Two-week interview calendar |

## How to Use This Map

| Step | Action |
|---|---|
| 1 | Open the current day in the learning plan. |
| 2 | Come here and open the mapped playbook module. |
| 3 | Run the code snippet or lab that matches the day. |
| 4 | Save the listed artifact so the session produces evidence. |
| 5 | Convert that artifact into one interview bullet before you stop. |

??? question "Interview Q: How do you turn a study plan into proof of capability?"
    **Model Answer:**
    I pair every study day with an artifact such as a script, a trace, an eval table, or a story card. That way the plan produces evidence I can reuse in interviews and portfolio discussion.

    **Why this matters:**
    Interview readiness depends on repeatable artifacts, not just reading completion.

??? question "Interview Q: Why map days to specific modules instead of reading broadly?"
    **Model Answer:**
    Mapping each day to one module reduces context switching and makes progress measurable. It also ensures that every study session ends with a concrete artifact instead of a vague sense of coverage.

    **Why this matters:**
    Focused repetition is easier to sustain and easier to explain in interviews.

--8<-- "_abbreviations.md"