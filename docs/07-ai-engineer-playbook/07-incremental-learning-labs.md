# 07 - Incremental Learning Labs (Memory-First)

These labs are short, repeatable drills designed to make concepts stick.

## How to Run These Labs

- Duration: 20-45 minutes each
- Cadence: 3 labs per week
- Method: build -> explain -> recall -> interview translation

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

**Goal:** decide deploy/no-deploy from evidence.

- Create 10-question golden set.
- Define pass thresholds.
- Run one baseline and one changed version.

**Output:** release decision note with metrics.

### Lab E - STAR Story Sprint

**Goal:** improve interview delivery quality.

- Select one project.
- Write STAR+T bullets.
- Prepare 90-second and 3-minute versions.

**Output:** polished interview script.

## Integration With Existing Notebooks

Pair these drills with existing site modules (continuation flow):

- [RAG Debugging and Quality](../02-technical-depth/rag-debugging-and-quality.md)
- [Agentic Workflows and Tools](../02-technical-depth/agentic-workflows-and-tools.md)
- [Evals, Observability, and Production](../02-technical-depth/evals-observability-and-production.md)
- [Mock Loop and Answer Drills](../03-interview-system/mock-loop-and-answer-drills.md)
- [Incremental Learning Labs](../04-labs-retention/incremental-learning-labs.md)

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

You can now revisit [Incremental Learning Labs](../04-labs-retention/incremental-learning-labs.md) with an interview-first mindset.

--8<-- "_abbreviations.md"

