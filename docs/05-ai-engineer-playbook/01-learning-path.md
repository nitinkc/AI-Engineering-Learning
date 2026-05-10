# 01 - Learning Path Companion

> **Level:** Intermediate
> **Pre-reading:** [Daily Learning Plan](../01-foundations/learning-revision-plan/index.md) · [Step-by-Step Learning Path](../01-foundations/step-by-step-learning-path.md)

---

This page is the reference companion to the daily plan, not a second primary schedule. Use it when you want the capability ladder, weekly checkpoints, and example code behind the 4-week learning system.

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

## Week 1 Execution Pack

Use this page together with the Week 1 daily plan when you want concrete study flow instead of high-level goals.

| Day | Focus | Primary material | Output to produce |
|---|---|---|---|
| Day 1 | LLM pipeline map and model basics | This page + [02 RAG Debugging and Quality](02-rag-debugging-quality.md) | Mermaid diagram of request flow |
| Day 2 | Prompting patterns and guardrails | This page + [02 RAG Debugging and Quality](02-rag-debugging-quality.md) | Prompt template with refusal rules |
| Day 3 | Embeddings and retrieval basics | [02 RAG Debugging and Quality](02-rag-debugging-quality.md) | Chunking and top-k experiment notes |
| Day 4 | RAG architecture and grounding | [02 RAG Debugging and Quality](02-rag-debugging-quality.md) | Minimal grounded QA script |
| Day 5 | RAG quality debugging | [02 RAG Debugging and Quality](02-rag-debugging-quality.md) + [07 Incremental Learning Labs](07-incremental-learning-labs.md) | Failure taxonomy table |
| Day 6 | Multimodal and long-context strategies | This page + [07 Incremental Learning Labs](07-incremental-learning-labs.md) | Long-document summarizer scaffold |
| Day 7 | Consolidation and retrieval drill | [07 Incremental Learning Labs](07-incremental-learning-labs.md) | One-page RAG playbook |

## Step-by-Step Foundations Flow

| Step | What to do | Why it matters |
|---|---|---|
| 1 | Sketch request -> context -> model -> validation -> response | It forces system thinking before prompt tweaking. |
| 2 | Estimate token usage for real prompts | It connects architecture choices to cost and latency. |
| 3 | Turn one task into a reusable prompt template | It improves repeatability and output consistency. |
| 4 | Build a tiny retrieval loop | It shows the boundary between retrieval and generation. |
| 5 | Record one failure and one fix | It creates interview-ready evidence, not vague study notes. |

## Example Code: Prompt Builder and Token Budget

```python
from dataclasses import dataclass


@dataclass
class LLMRequest:
	system: str
	user: str
	context_blocks: list[str]


def estimate_tokens(text: str) -> int:
	return max(1, len(text.split()) * 4 // 3)


def build_prompt(request: LLMRequest) -> str:
	context = "\n\n".join(
		f"Source {index + 1}: {block}"
		for index, block in enumerate(request.context_blocks)
	)
	return (
		f"SYSTEM:\n{request.system}\n\n"
		f"CONTEXT:\n{context}\n\n"
		f"USER:\n{request.user}\n\n"
		"Return a grounded answer and refuse if the context is insufficient."
	)


request = LLMRequest(
	system="You answer only from approved internal knowledge.",
	user="How do we reset an expired API key?",
	context_blocks=[
		"API keys rotate every 90 days and expired keys must be revoked.",
		"Users reset keys from the security portal after identity verification.",
	],
)

prompt = build_prompt(request)
print(prompt)
print({"estimated_tokens": estimate_tokens(prompt)})
```

## Example Code: Long-Context Map-Reduce Scaffold

```python
def chunk_text(text: str, chunk_size: int = 800) -> list[str]:
	words = text.split()
	return [" ".join(words[index:index + chunk_size]) for index in range(0, len(words), chunk_size)]


def summarize_chunk(chunk: str) -> str:
	sentences = chunk.split(".")
	return ". ".join(sentence.strip() for sentence in sentences[:2] if sentence.strip())


def summarize_document(text: str) -> str:
	chunk_summaries = [summarize_chunk(chunk) for chunk in chunk_text(text)]
	return summarize_chunk(". ".join(chunk_summaries))
```

??? question "Interview Q: How do you move from prompt experiments to a real LLM system?"
	**Model Answer:**
	I define the full request path first: context construction, model call, validation, and logging. That lets me isolate cost, retrieval, and prompt issues separately instead of treating the whole system as one prompt box.

	**Why this matters:**
	Interviewers want architecture discipline, not trial-and-error prompting.

??? question "Interview Q: Why do token budgets matter so early in design?"
	**Model Answer:**
	Token budgets shape cost, latency, and retrieval strategy. If I estimate them early, I can decide whether I need summarization, pruning, smaller models, or staged context assembly before the system becomes expensive and slow.

	**Why this matters:**
	This shows production thinking, not just model familiarity.

## Exit Criteria for This Module

- [ ] I can explain the production LLM mental model without notes.
- [ ] I can run a repeatable RAG debugging sequence.
- [ ] I can justify hybrid deterministic-plus-agent design choices.
- [ ] I can define quality, reliability, and cost metrics for deployment decisions.

---

Next: [02 RAG Debugging and Quality](02-rag-debugging-quality.md)

--8<-- "_abbreviations.md"

