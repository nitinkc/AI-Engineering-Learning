# 07 - Incremental Learning Labs (Memory-First)

> **Level:** Intermediate
> **Pre-reading:** [Daily Learning Plan](../01-foundations/learning-revision-plan/index.md) · [02 RAG Debugging and Quality](02-rag-debugging-quality.md) · [03 Agentic Workflows](03-agentic-workflows.md)

---

These labs are short, repeatable drills designed to make concepts stick. Each lab forces you to build something small, explain it from memory, and turn the result into an interview-ready artifact.

## How the Labs Reinforce Learning

```mermaid
graph LR
	A[Learn a concept] --> B[Run a short lab]
	B --> C[Create one artifact]
	C --> D[Explain it from memory]
	D --> E[Convert it into interview evidence]

	style A fill:#1976d2,color:#fff
	style B fill:#ff9800,color:#fff
	style E fill:#2e7d32,color:#fff
```

## How to Run These Labs

| Variable | Default |
|---|---|
| Duration | 20 to 45 minutes |
| Cadence | 3 labs per week |
| Method | build -> explain -> recall -> interview translation |
| Output | one artifact plus one STAR bullet |

## Lab Sequence

### Lab A - RAG Diagnosis Sprint

**Goal:** classify failures quickly.

- Use 5 failed Q&A examples.
- Label each as `coverage`, `retrieval`, `prompt`, or `validation`.
- Propose one concrete fix per case.

**Output:** one-page troubleshooting table.

### Lab B - Retrieval Quality Sprint

**Goal:** connect retrieval settings to answer quality.

- Vary chunk size and top-k.
- Compare semantic vs hybrid retrieval.
- Record metric movement.

**Output:** before/after metric snapshot.

### Lab C - Tool Reliability Sprint

**Goal:** enforce safe execution boundaries.

- Define 2 tools with schemas.
- Add validation, timeout, retry, and escalation.
- Simulate one risky action requiring approval.

**Output:** workflow state diagram plus error policy.

### Lab D - Eval Gate Sprint

**Goal:** decide deploy or no-deploy from evidence.

- Create a 10-question golden set.
- Define pass thresholds.
- Run one baseline and one changed version.

**Output:** release decision note with metrics.

### Lab E - STAR Story Sprint

**Goal:** improve interview delivery quality.

- Select one project.
- Write STAR+T bullets.
- Prepare 90-second and 3-minute versions.

**Output:** polished interview script.

## Best Companion Modules

| Lab | Best module to pair with | Why it fits |
|---|---|---|
| Lab A | [02 RAG Debugging and Quality](02-rag-debugging-quality.md) | It gives you the failure taxonomy and debug order. |
| Lab B | [02 RAG Debugging and Quality](02-rag-debugging-quality.md) | It supplies the retrieval metrics and prototype flow. |
| Lab C | [03 Agentic Workflows](03-agentic-workflows.md) | It defines schemas, approvals, retries, and escalation. |
| Lab D | [04 Evals, Observability, Production](04-evals-observability-production.md) | It provides the release-gate and trace mindset. |
| Lab E | [05 STAR Story System](05-star-story-system.md) and [06 Interview Sprints and Mock Loops](06-interview-sprints-and-mock-loops.md) | They turn lab outputs into interview-ready stories. |

## Day-by-Day Reinforcement Map

| Day | Best lab to run | Output |
|---|---|---|
| Day 5 | Lab A - RAG Diagnosis Sprint | Root-cause table |
| Day 7 | Lab B - Retrieval Quality Sprint | Metric snapshot |
| Day 13 | Lab C - Tool Reliability Sprint | Workflow policy diagram |
| Day 16 | Lab D - Eval Gate Sprint | Release decision note |
| Day 21 | Lab D + review checklist | Readiness scorecard |
| Day 23 | Lab E - STAR Story Sprint | Story script |
| Day 27 | Lab E + full mock loop | Revised interview answer set |

## Step-by-Step Lab Output Templates

### Failure Table Template

| Question | Root cause | First fix | Metric |
|---|---|---|---|
| Example question | retrieval | add hybrid retrieval | hit rate |

### Release Gate Template

```yaml
change: reranker-v2
baseline:
  faithfulness: 0.82
  retrieval_hit_rate: 0.76
candidate:
  faithfulness: 0.89
  retrieval_hit_rate: 0.84
decision: deploy
reason: all threshold metrics improved and latency remained within budget
```

### Story Compression Template

```text
Project context
-> your ownership
-> main change
-> metric movement
-> tradeoff and lesson
```

??? question "Interview Q: Why are these short labs useful if you already know the theory?"
	**Model Answer:**
	They force retrieval from memory, artifact creation, and explanation under time pressure. That is closer to interview performance and production troubleshooting than passive review.

	**Why this matters:**
	Strong preparation depends on repeated transfer, not one-time reading.

??? question "Interview Q: What makes a lab output interview-worthy?"
	**Model Answer:**
	A lab becomes interview-worthy when it produces evidence such as a metrics table, a workflow diagram, or a release decision backed by tradeoffs. The artifact matters more than the time spent reading.

	**Why this matters:**
	Interviewers respond to proof of execution, not vague study claims.

??? question "Interview Q: How do you keep labs from becoming random practice?"
	**Model Answer:**
	I tie each lab to one module, one day in the plan, one artifact, and one follow-up recall drill. That creates a small but repeatable system instead of disconnected exercises.

	**Why this matters:**
	Structured repetition is what turns short practice into long-term retention.

## 4-Week Retention Plan

| Week | Focus | Repeat |
|---|---|---|
| 1 | Labs A + B | 2 cycles |
| 2 | Labs C + D | 2 cycles |
| 3 | Labs E + mixed weak areas | 3 cycles |
| 4 | Full mock loop + final review | 2 full runs |

## Continuation Rule

After each lab output, add two artifacts:

1. One regression test case you will keep.
2. One interview-ready STAR bullet that captures the lesson.

## Completion Criteria

- [ ] I can diagnose RAG failures without guessing.
- [ ] I can define agent guardrails and recovery paths.
- [ ] I can justify deployment decisions with metrics.
- [ ] I can deliver 8 STAR+T stories confidently.

---

Next: [08 Daily Material Map](08-daily-material-map.md)

--8<-- "_abbreviations.md"

