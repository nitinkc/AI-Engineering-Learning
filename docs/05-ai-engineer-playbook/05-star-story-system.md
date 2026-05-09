# 05 - STAR Story System for AI Engineer Interviews

This module helps you convert technical depth into clear interview stories.

## Use STAR+T

- **Situation**: Context and constraints
- **Task**: Your ownership and success criteria
- **Action**: What you designed, built, debugged, and measured
- **Result**: Quantified impact
- **Tradeoffs**: Why this approach, what you rejected

## Build an 8-Story Bank

Use one story for each capability:

1. Built RAG application
2. Debugged poor AI quality
3. Built tool-calling/agentic workflow
4. Improved latency and cost
5. Created evaluation and monitoring loop
6. Deployed to production
7. Led AI coding workflow with guardrails
8. Created standards/playbook

At minimum, keep the baseline six ready at all times:

1. Built an LLM or RAG system
2. Debugged a production quality issue
3. Improved latency or cost
4. Designed evaluation framework
5. Deployed and operated in production
6. Used AI coding tools to accelerate delivery safely

## Story Mapping Matrix

| Story | Signals You Demonstrate |
|---|---|
| RAG build | architecture, retrieval quality, grounding |
| Debugging | trace literacy, diagnosis, reliability mindset |
| Agent workflow | orchestration, safety, control boundaries |
| Cost/latency | pragmatic optimization and model routing |
| Evals/monitoring | measurable quality ownership |
| Production deployment | operational maturity |
| AI coding pilot | modern developer workflow leadership |
| Standards/playbook | scaling practices across teams |

## Week 4 Alignment

| Day | Use this page for | Deliverable |
|---|---|---|
| Day 22 | Role targeting and evidence mapping | Competency matrix |
| Day 23 | STAR story drafting and compression | Six story bank |
| Day 24 | Portfolio narrative and case-study framing | Case-study outline |

## Step-by-Step Story Build Sequence

| Step | Action | Output |
|---|---|---|
| 1 | Pick one project with real constraints | Story candidate |
| 2 | Write facts before writing polish | Raw notes |
| 3 | Name your ownership clearly | Strong Task section |
| 4 | Add metrics, latency, cost, or quality impact | Quantified Result |
| 5 | Explain one decision you rejected | Tradeoff line |
| 6 | Compress to 90 seconds, then expand to 3 minutes | Interview-ready pair |

## Example Template: Story Card

```markdown
## Story: Improved RAG Answer Quality

Situation:
The support assistant was returning incomplete answers for account-security questions.

Task:
I owned retrieval quality and needed to improve grounded answer accuracy before launch.

Action:
I logged retrieved chunks, reworked chunking boundaries, added hybrid retrieval, and introduced citation-only answer rules.

Result:
Retrieval hit rate improved from 0.61 to 0.84, faithfulness increased by 11 points, and support review time dropped by 22 percent.

Tradeoff:
Hybrid retrieval added some latency, so I limited reranking to high-value queries.
```

## Example Table: Role-to-Evidence Matrix

| Role signal | Evidence to attach |
|---|---|
| LLM architecture | diagram, API flow, prompt builder |
| RAG quality | eval table, failure log, citations |
| Agent reliability | workflow state diagram, approval gate |
| Production ops | release gate, trace record, postmortem |

## 90-Second Formula

```text
Project and context
-> your ownership
-> architecture and implementation
-> core challenge and tradeoff
-> measurable result
-> key lesson
```

## STAR+T Scoring Rubric

Before using a story in interviews, check:

- [ ] Includes concrete scope and constraints
- [ ] Names your specific ownership
- [ ] Includes 1 to 3 measurable outcomes
- [ ] Explains one design tradeoff clearly
- [ ] Ends with learning and next improvement

## 3-Minute Deep Dive Formula

```text
Context and constraints
-> architecture details
-> failure modes
-> evaluation and metrics
-> deployment and reliability
-> what you would improve next
```

## Quick Lab (15 min)

<details>
<summary>STAR compression lab</summary>

- Pick one project.
- Write STAR+T in 8 bullet points.
- Convert it to a 90-second answer.
- Record yourself once and tighten language.

</details>

??? question "Interview Q: What makes a STAR story credible for an AI engineer role?"
	**Model Answer:**
	A credible story includes technical constraints, your explicit ownership, measurable outcomes, and one clear tradeoff. Without those, it sounds like summary language instead of evidence from real engineering work.

	**Why this matters:**
	Interviewers use stories to test both substance and judgment.

??? question "Interview Q: How do you avoid sounding vague when describing AI projects?"
	**Model Answer:**
	I anchor the story in artifacts and metrics such as retrieval hit rate, latency, evaluation gates, or deployment outcomes. That keeps the answer concrete and makes the impact testable.

	**Why this matters:**
	Clear evidence separates practiced answers from real execution.

---

Next: [06 Interview Sprint Loops](06-interview-sprints-and-mock-loops.md)

--8<-- "_abbreviations.md"

