# 06 - Interview Sprint Loops

This module gives you a repeatable prep routine for stronger recall and delivery.

## Weekly Sprint Structure

### Sprint A - Technical Clarity

- Explain one architecture from memory.
- Whiteboard one failure mode and fix sequence.
- Answer one system-design question in 3 minutes.

### Sprint B - Story Quality

- Deliver 2 STAR+T stories.
- Add or refine one metric in each story.
- Tighten tradeoff explanation.

### Sprint C - Realism and Pressure

- Run 30-minute mock interview.
- Review weak answers and rewrite.
- Re-attempt same questions after 24 hours.

## Mock Interview Question Bank

- How do you debug bad RAG answers?
- How do you design reliable tool-calling agents?
- How do you evaluate prompt/model changes?
- How do you balance latency, cost, and quality?
- How do you productionize an LLM workflow?
- How do you use AI coding tools safely?

Add these baseline finals:

- Tell me about an LLM system you built end to end.
- How do you handle tool-call failures in production?
- How would you design an MCP-based coding pilot?

## Feedback Rubric

Score each answer from 1 to 5 on:

- Technical depth
- Clarity and structure
- Metrics and measurable impact
- Tradeoff reasoning
- Production realism

## Week 4 Alignment

| Day | Use this page for | Deliverable |
|---|---|---|
| Day 25 | Technical drill structure and answer framework | Drill score sheet |
| Day 26 | Behavioral communication and translation | Stakeholder-friendly answer set |
| Day 27 | Full mock loop and revision cycle | Mock transcript and fixes |
| Day 28 | Final launch plan and warm-up cadence | 2-week interview calendar |

## Step-by-Step Mock Loop Runbook

| Step | Action | Output |
|---|---|---|
| 1 | Pick 3 technical questions and 2 behavioral questions | Question set |
| 2 | Answer each in 90 seconds | Baseline delivery |
| 3 | Re-answer the weakest one in 3 minutes | Deep-dive version |
| 4 | Score with the rubric | Gap list |
| 5 | Rewrite one weak answer and retry next day | Improvement loop |

## Example Code: 90-Second Drill Runner

```python
import time


questions = [
	"How do you debug a bad RAG answer?",
	"How do you design reliable tool-calling agents?",
	"How do you evaluate a prompt change before release?",
]


for question in questions:
	print(f"Question: {question}")
	print("Start speaking now")
	time.sleep(2)
	print("Checkpoint: 30 seconds")
	time.sleep(2)
	print("Checkpoint: 60 seconds")
	time.sleep(2)
	print("Stop at 90 seconds and score yourself")
```

## Example Scorecard

```yaml
candidate: self-review
question: How do you debug bad RAG answers?
scores:
  technical_depth: 4
  clarity: 3
  metrics: 2
  tradeoffs: 3
  production_realism: 4
next_fix: Add one metric and shorten the opening by one sentence.
```

??? question "Interview Q: What is the fastest way to improve weak interview answers?"
	**Model Answer:**
	Record the answer, score it against a fixed rubric, and rewrite only the weakest part instead of starting over. That creates measurable iteration instead of random practice.

	**Why this matters:**
	This shows you can improve performance with an engineering-style feedback loop.

??? question "Interview Q: Why prepare both 90-second and 3-minute versions?"
	**Model Answer:**
	The short version proves clarity and structure, while the longer version proves depth and tradeoff reasoning. Together they prepare you for both recruiter screens and technical interviews.

	**Why this matters:**
	Interview success depends on adapting answer depth to the round.

## Retention Trick: Mistake Ledger

After each mock:

- Write the top 3 misses.
- Write improved phrasing.
- Rehearse corrected answers after 1 day and 1 week.

## Weekly Cadence

- Round 1 (Mon/Tue): 90-second clarity answers
- Round 2 (Thu): 3-minute deep dive answers
- Round 3 (Weekend): 30-minute mixed mock loop

## Quick Lab (20 min)

<details>
<summary>Mock loop lab</summary>

- Pick any 3 questions from the bank.
- Answer each in 90 seconds.
- Re-answer one question in 3 minutes.
- Grade yourself with the rubric and update one story.

</details>

---

Next: [07 Incremental Learning Labs](07-incremental-learning-labs.md)

--8<-- "_abbreviations.md"

