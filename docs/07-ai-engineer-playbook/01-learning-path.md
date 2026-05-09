# 01 - Step-by-Step Learning Path

This module is a continuation of `ai_engineer_learning_revision_plan.md` and keeps the same baseline order and depth targets.

## Learning Goal

Build interview-ready confidence in four capability layers:

- Architecture and system design for LLM apps
- RAG quality and debugging
- Agent reliability and tool orchestration
- Evals, production operations, and communication

## Priority Ladder (Aligned to Baseline)

| Priority | Focus Area | Why It Matters in Interviews |
|---|---|---|
| P0 | LLM architecture + RAG | Most frequent system design and debugging questions |
| P0 | Agent workflows + tool calling | Tests reliability mindset and real-world control |
| P1 | Evals + observability | Demonstrates production ownership and quality gates |
| P1 | Deployment + reliability patterns | Shows engineering maturity beyond notebooks |
| P2 | Framework breadth (CrewAI/AutoGen/SK) | Helpful differentiator, but secondary |

## 4-Week Baseline Progression

### Week 1 - LLM Architecture + RAG Fundamentals

- Design the request-to-response mental model end to end.
- Explain ingestion, chunking, embeddings, retrieval, reranking, grounding, and citation.
- Practice the baseline 10-step RAG debugging sequence.

**Checkpoint:** answer "How do you debug wrong RAG answers?" in 2 to 3 minutes with a clear sequence.

### Week 2 - Agents, Tools, and State Management

- Compare workflow, chain, and agent patterns.
- Implement tool schemas, validation, retries, fallbacks, and idempotency.
- Use a hybrid deterministic-plus-LLM orchestration model.

**Checkpoint:** draw a stateful flow with approval, retry, escalation, and completion paths.

### Week 3 - Evals, Observability, and Production Readiness

- Build a golden dataset and regression loop.
- Track retrieval, generation, agent, and operations metrics.
- Define deployment gates, rollback strategy, and incident handling.

**Checkpoint:** present deploy/no-deploy criteria with measurable thresholds.

### Week 4 - Portfolio and Interview Conversion

- Convert technical work into STAR+T stories.
- Prepare 90-second and 3-minute answer variants.
- Run mock loops and tighten weak responses.

**Checkpoint:** deliver an 8-story bank with metrics, tradeoffs, and lessons learned.

## Daily Study Loop (60-90 Minutes)

1. Concept refresh (15 min)
2. Build or debug task (25-30 min)
3. Recall drill from memory (10 min)
4. Interview translation to STAR bullets (10 min)
5. Mistake log and next action (5 min)

## Retention Pattern (1-3-7-14)

- Day 1: learn and implement
- Day 3: first recall and correction
- Day 7: second recall with verbal explanation
- Day 14: full interview-quality answer

## Exit Criteria for This Module

- [ ] I can explain the production LLM mental model without notes.
- [ ] I can run a repeatable RAG debugging sequence.
- [ ] I can justify hybrid deterministic-plus-agent design choices.
- [ ] I can define quality, reliability, and cost metrics for deployment decisions.

---

Next: [02 RAG Debugging and Quality](02-rag-debugging-quality.md)

--8<-- "_abbreviations.md"

