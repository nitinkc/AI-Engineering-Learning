# AI Engineer Reference Modules: Build, Debug, Explain

This section is the reusable reference layer for the site. The day-by-day execution now lives in the
learning revision plan, while these pages hold the durable deep dives, worked examples, and reusable
interview prep modules.

Use the daily plan when you want to know what to do next. Use these reference modules when you want
the fuller explanation, example code, or lab pattern behind that day.

## Who This Is For

Use this if you are targeting AI Engineer, Agent Engineer, GenAI Engineer, or LLMOps roles where
interviewers test build-debug-deploy ownership.

## Week 1 - Foundations, RAG, and Retrieval

| Day | Focus                                  | Primary material                                                                | Code or lab to use                   | End-of-day artifact          |
|-----|----------------------------------------|---------------------------------------------------------------------------------|--------------------------------------|------------------------------|
| 1   | LLM pipeline map and model basics      | [Foundations Overview](index.md)                                                | Prompt Builder and Token Budget      | System diagram               |
| 2   | Prompting patterns and guardrails      | [Foundations Overview](index.md)                                                | Prompt Builder and Token Budget      | Prompt template library      |
| 3   | Embeddings and retrieval basics        | [01 RAG Debugging and Quality](01-foundations/01-rag-debugging-quality.md)      | Minimal Grounded Retrieval Prototype | Chunking experiment note     |
| 4   | RAG architecture and grounding         | [01 RAG Debugging and Quality](01-foundations/01-rag-debugging-quality.md)      | Minimal Grounded Retrieval Prototype | Grounded QA script           |
| 5   | RAG quality debugging                  | [01 RAG Debugging and Quality](01-foundations/01-rag-debugging-quality.md)      | Failure Logging for RAG Debugging    | Root-cause table             |
| 6   | Multimodal and long-context strategies | [Foundations Overview](index.md)                                                | Long-Context Map-Reduce Scaffold     | Long-doc summary scaffold    |
| 7   | Consolidation and retrieval drill      | [Week 1 RAG Foundations Lab](03-mini-projects/01-week-1-rag-foundations-lab.md) | Lab A or Lab B                       | One-page debugging checklist |

## Week 2 - Agents, LangGraph, and Reliability

| Day | Focus                                  | Primary material                                                                                                                                     | Code or lab to use                               | End-of-day artifact        |
|-----|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|----------------------------|
| 8   | Agentic patterns and tool calling      | [02 Agentic Workflows](01-foundations/02-agentic-workflows.md)                                                                                       | Tool Contract and Validator                      | Tool schema set            |
| 9   | Planning, memory, and state management | [02 Agentic Workflows](01-foundations/02-agentic-workflows.md)                                                                                       | Stateful Workflow with Retry and Approval        | State transition sketch    |
| 10  | LangGraph fundamentals                 | [02 Agentic Workflows](01-foundations/02-agentic-workflows.md)                                                                                       | Stateful Workflow with Retry and Approval        | Node-edge graph draft      |
| 11  | Multi-agent coordination               | [02 Agentic Workflows](01-foundations/02-agentic-workflows.md)                                                                                       | Supervisor-worker adaptation of workflow example | Multi-agent handoff design |
| 12  | Human-in-the-loop and approvals        | [02 Agentic Workflows](01-foundations/02-agentic-workflows.md)                                                                                       | Stateful Workflow with Retry and Approval        | Approval gate path         |
| 13  | Reliability hardening for agents       | [02 Agentic Workflows](01-foundations/02-agentic-workflows.md) + [Week 2 Agent Reliability Lab](03-mini-projects/02-week-2-agent-reliability-lab.md) | Tool Reliability Sprint                          | Failure matrix             |
| 14  | Consolidation and design review        | [02 Agentic Workflows](01-foundations/02-agentic-workflows.md) + [Week 2 Agent Reliability Lab](03-mini-projects/02-week-2-agent-reliability-lab.md) | Lab C output review                              | Architecture brief         |

## Week 3 - Evals, Observability, and Production

| Day | Focus                                  | Primary material                                                                                                                                                                 | Code or lab to use                        | End-of-day artifact         |
|-----|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|-----------------------------|
| 15  | Eval strategy and datasets             | [03 Evals, Observability, and Production](01-foundations/03-evals-observability-production.md)                                                                                   | Tiny Eval Dataset and Gate                | Starter eval set            |
| 16  | Automated eval pipelines               | [03 Evals, Observability, and Production](01-foundations/03-evals-observability-production.md)                                                                                   | Tiny Eval Dataset and Gate                | Release gate policy         |
| 17  | Observability and tracing              | [03 Evals, Observability, and Production](01-foundations/03-evals-observability-production.md)                                                                                   | Structured Trace Record                   | Trace example               |
| 18  | Safety and policy controls             | [03 Evals, Observability, and Production](01-foundations/03-evals-observability-production.md)                                                                                   | Observability Checklist plus safety notes | Safety middleware checklist |
| 19  | Deployment, scaling, and SLOs          | [03 Evals, Observability, and Production](01-foundations/03-evals-observability-production.md)                                                                                   | Release gate plus reliability checklist   | SLO and rollout note        |
| 20  | Postmortems and continuous improvement | [03 Evals, Observability, and Production](01-foundations/03-evals-observability-production.md)                                                                                   | Release gate retrospective                | Postmortem draft            |
| 21  | Readiness review                       | [03 Evals, Observability, and Production](01-foundations/03-evals-observability-production.md) + [Week 3 Eval and Ops Lab](03-mini-projects/03-week-3-eval-observability-lab.md) | Lab D and readiness checklist             | Production scorecard        |

## Week 4 - Portfolio, Stories, and Mock Loops

| Day | Focus                                         | Primary material                                                                                                                         | Code or lab to use                        | End-of-day artifact         |
|-----|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|-----------------------------|
| 22  | Role targeting and competency mapping         | [04 STAR Story System](01-foundations/04-star-story-system.md)                                                                           | Role-to-Evidence Matrix                   | Competency matrix           |
| 23  | STAR story bank                               | [04 STAR Story System](01-foundations/04-star-story-system.md)                                                                           | Story Card template                       | Six story draft             |
| 24  | Portfolio assembly and narrative              | [04 STAR Story System](01-foundations/04-star-story-system.md)                                                                           | Story Card plus case-study framing        | Case-study outline          |
| 25  | Technical interview drills                    | [05 Interview Sprint Loops](01-foundations/05-interview-sprints-and-mock-loops.md)                                                       | 90-Second Drill Runner                    | Drill score sheet           |
| 26  | Behavioral and cross-functional communication | [05 Interview Sprint Loops](01-foundations/05-interview-sprints-and-mock-loops.md)                                                       | Example Scorecard and stakeholder rewrite | Behavioral answer sheet     |
| 27  | Full mock loop and feedback integration       | [05 Interview Sprint Loops](01-foundations/05-interview-sprints-and-mock-loops.md) + [Mini Projects Overview](03-mini-projects/index.md) | Lab E and mock loop                       | Revision log                |
| 28  | Final synthesis and launch plan               | [05 Interview Sprint Loops](01-foundations/05-interview-sprints-and-mock-loops.md)                                                       | Step-by-Step Mock Loop Runbook            | Two-week interview calendar |

--8<-- "_abbreviations.md"
