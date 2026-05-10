# Day 23 — STAR Story Bank for AI Projects — Learn & Revise

> **Pre-reading:** [Week 4 Overview](./index.md) · [Learning Plan](../index.md)

---

## 🎯 What You'll Master Today

Behavioural interviews for AI engineering roles require more than a generic STAR answer —
interviewers expect technical depth woven into the story, real numbers, and evidence that you
understand why your decisions worked. Today you will learn the STAR+T framework (Situation, Task,
Action, Result, Technical depth), build a story selection system, and walk through three fully
worked STAR+T stories covering the most common AI engineering scenarios. By end of day you will have
a personal story bank ready to adapt on demand.

---

## 📖 Core Concepts

### The STAR+T Framework

The classic STAR framework (Situation, Task, Action, Result) is a solid foundation but it leaves a
gap for technical roles. Interviewers for AI engineering positions will follow up every Result
with "how did you measure that?" or "what was the technical mechanism?" The +T layer adds a *
*Technical depth** component that pre-empts those follow-ups.

| Layer          | What to Cover                                                                  | Length        |
|----------------|--------------------------------------------------------------------------------|---------------|
| **Situation**  | Context — team, product, business problem                                      | 2–3 sentences |
| **Task**       | Your specific responsibility or objective                                      | 1–2 sentences |
| **Action**     | What you did, step by step, with technical specifics                           | 4–6 sentences |
| **Result**     | Measurable outcome tied to a metric                                            | 2–3 sentences |
| **+Technical** | Mechanism, architecture decision, or eval method that explains *why* it worked | 2–3 sentences |

Total target length: 2.5 to 3.5 minutes spoken at a calm pace.

### Story Selection Criteria

Not every project makes a good interview story. Filter by four criteria:

| Criterion         | Why it Matters                                    | Red Flag                                        |
|-------------------|---------------------------------------------------|-------------------------------------------------|
| **Impact**        | Interviewers want evidence of value, not activity | "I worked on it" with no outcome                |
| **Recency**       | Recent work reflects current skills and norms     | Stories older than 3–4 years need justification |
| **Relevance**     | Matches the competency cluster being tested       | A deep ML training story for an LLM role        |
| **Measurability** | Numbers make claims credible                      | Vague qualitative outcomes only                 |

A story that scores high on all four is a tier-1 story. Aim for 5–6 tier-1 stories in your bank
covering different competency clusters.

### Quantifying Results in AI Projects

Typical measurable outcomes for AI engineering work:

| Metric Type        | Example                                                                         |
|--------------------|---------------------------------------------------------------------------------|
| Retrieval quality  | "Recall@10 improved from 62% to 87%"                                            |
| Generation quality | "Hallucination rate dropped from 18% to 4% measured by NLI contradiction score" |
| Latency            | "P95 response time reduced from 4.2s to 1.8s"                                   |
| Cost               | "Inference cost reduced by 35% via model distillation"                          |
| Eval coverage      | "Automated eval pipeline caught 3 regressions before shipping in 8 weeks"       |
| User impact        | "Customer satisfaction score on AI assistant increased from 3.2 to 4.4 / 5"     |

If you have no production metrics, use evaluation metrics from a rigorous offline benchmark. If you
have neither, explain the methodology you used and the signal it gave — methodology evidence is
better than no evidence.

### Adapting One Story to Multiple Question Types

A single project can answer many different question types. The key is knowing which part of the
story to emphasise:

| Question Type                                      | Which Part to Lead With                                                      |
|----------------------------------------------------|------------------------------------------------------------------------------|
| "Tell me about a time you improved quality"        | Lead with baseline metric, then Action focused on eval design                |
| "Tell me about a production incident"              | Lead with the incident trigger, then Action focused on debugging             |
| "How have you measured success in an LLM project?" | Lead with the metric design, then Action focused on instrumentation          |
| "Describe a technical challenge"                   | Lead with the hardest architectural decision in the Action                   |
| "Tell me about cross-team collaboration"           | Lead with stakeholder context in Situation, then Result focused on alignment |

---

## 🗺️ Strategy Map

```mermaid
graph LR
    A["Story Bank"] --> B["Select Story"]
    B --> C["Map to Question"]
    C --> D["Adapt Framing"]
    D --> E["Deliver with +T Depth"]
    E --> F["Validate with Numbers"]

    style A fill:#1976d2,color:#fff
    style B fill:#1976d2,color:#fff
    style C fill:#ff9800,color:#fff
    style D fill:#ff9800,color:#fff
    style E fill:#2e7d32,color:#fff
    style F fill:#2e7d32,color:#fff
```

---

## ⚡ Key Facts — Quick Revision Table

| Concept                  | One-Line Definition                                             | Why It Matters                                           |
|--------------------------|-----------------------------------------------------------------|----------------------------------------------------------|
| STAR+T                   | STAR framework extended with a Technical depth layer            | Prevents follow-up questions from catching you off-guard |
| Story bank               | Curated set of 5–6 tier-1 interview stories                     | Ensures coverage of all competency clusters              |
| Story selection          | Filtering projects by impact, recency, relevance, measurability | Avoids weak stories that undermine credibility           |
| Quantified result        | A metric-backed outcome statement                               | Makes claims credible and memorable                      |
| Retrieval quality metric | Recall@K or precision@K for RAG systems                         | The primary eval signal for retrieval stages             |
| Hallucination rate       | % of outputs containing factual contradictions                  | Key quality metric for generative AI in production       |
| P95 latency              | 95th percentile response time                                   | Standard reliability metric for production APIs          |
| Story adaptation         | Reframing story emphasis to match the question competency       | One story can answer many different questions            |
| Tier-1 story             | A story scoring high on all four selection criteria             | The stories worth rehearsing until automatic             |
| Offline metric           | Evaluation metric measured on a fixed benchmark dataset         | Useful when production metrics are unavailable           |

---

## 🔬 Deep Dive with Examples

### Story 1 — Improved RAG Retrieval Quality from 62% to 87% Recall

**Situation:** I was working on an internal knowledge assistant at a B2B SaaS company. The assistant
was built to help support agents answer customer questions using a corpus of 40,000 product
documentation pages. Three months post-launch, support agents were ignoring it because the answers
were irrelevant. Our baseline recall@10 was 62%.

**Task:** I was given ownership of retrieval quality improvement with a target of hitting 80%
recall@10 within six weeks.

**Action:** I started by running an error analysis on 200 failed queries. I found three root
causes: (1) dense retrieval was failing on exact product name lookups, (2) chunk boundaries were
cutting off critical context mid-sentence, (3) the embedding model had not been fine-tuned on our
domain vocabulary. I introduced a hybrid retrieval layer combining BM25 for exact-match queries and
the dense model for semantic queries, merged with RRF. I then re-chunked the corpus using a sliding
window with 10% overlap. Finally, I ran RAGAS faithfulness and answer relevance evals on a
300-question test set to validate each change independently before combining them.

**Result:** After six weeks, recall@10 reached 87%. Support agent adoption increased from 12% to 61%
over the following month. Escalation volume dropped by 23%.

**+Technical:** The key mechanism was the hybrid retrieval fusion. BM25 handles lexical matches that
dense retrieval misses — named entities, product codes, version numbers. RRF gave a principled way
to merge the ranked lists without needing to tune a weight parameter per query type. The chunking
overlap change had a smaller but measurable effect: +3 percentage points on its own, tested by A/B
comparison on the eval set.

---

### Story 2 — Reduced LLM Agent Hallucination Rate in a Production Chatbot

**Situation:** I was the lead engineer on a customer-facing chatbot built on GPT-4 for an insurance
company. During a routine policy renewal, a user was told their policy covered a risk it did not.
The legal team flagged it. When we measured systematically, our hallucination rate — defined as
outputs that contradicted source documents, measured via NLI contradiction scoring — was 18%.

**Task:** I was responsible for reducing the hallucination rate to under 5% without degrading
response quality or increasing latency beyond 500ms.

**Action:** I approached the problem in layers. First, I instrumented the pipeline to log every LLM
output alongside the retrieved context for offline analysis. This let me categorise hallucinations:
60% were cases where the retrieved context was incomplete, 30% were prompt misinterpretation, and
10% were model confabulation with adequate context. For the retrieval gap, I added a retrieval
confidence filter — if the top chunk similarity score fell below 0.72, the system returned a "I
cannot find a reliable answer to that" response rather than hallucinating. For the prompt layer, I
rewrote the system prompt to add explicit grounding instructions: "Answer only using facts stated in
the context. If the context is silent on the question, say so." I added a post-generation
verification step using a smaller model as a self-consistency checker for high-stakes policy
questions.

**Result:** Hallucination rate dropped from 18% to 3.2% within four weeks. Legal approved the system
for expanded rollout. The retrieval confidence filter accounted for 8 percentage points of the
improvement; the prompt rewrite accounted for 5 points; the self-consistency checker caught the
remaining edge cases.

**+Technical:** The NLI contradiction scoring approach used a fine-tuned DeBERTa-v3 model to compare
each sentence in the LLM output against the source context. It ran in under 80ms per query, which
fit within our latency budget. This became our standard production eval harness — the same pipeline
now runs nightly regression tests against a golden dataset of 500 policy questions.

---

### Story 3 — Built an Automated Eval Pipeline that Caught a Prompt Regression Before It Shipped

**Situation:** Our team shipped prompt updates to a legal document summarisation product on an
ad-hoc basis. There was no systematic eval — engineers would test manually with 5–10 examples and
ship if it "looked good". After a near-miss incident where a prompt change caused summaries to drop
key liability clauses, the engineering lead asked me to create a proper eval pipeline.

**Task:** Design and implement an automated evaluation pipeline integrated into CI/CD that would
block any prompt change that degraded quality below threshold.

**Action:** I designed a three-stage eval pipeline. Stage 1 ran RAGAS metrics (faithfulness, answer
relevance, context precision) against a curated 250-example golden dataset. Stage 2 ran a set of
targeted adversarial prompts designed to test specific failure modes — missing liability detection,
date extraction errors, party name confusion. Stage 3 ran a LLM-as-judge evaluation comparing the
new prompt output against a reference output from a known-good prompt version. I integrated this
into GitHub Actions so every pull request touching a prompt file triggered the full eval suite.
Results were posted as a PR comment showing a metric dashboard. Any regression of more than 2% on
any metric blocked the merge.

**Result:** In the eight weeks after launch, the pipeline blocked three prompt changes that would
have regressed quality. The most significant catch was a prompt rewrite that improved fluency scores
but dropped liability clause recall from 94% to 71% — a change that would have missed critical
content in live documents. We shipped that prompt after fixing the clause extraction issue.

**+Technical:** The LLM-as-judge step used a structured evaluation rubric with five dimensions
scored 1–5, with GPT-4 as the evaluator. I added inter-rater reliability calibration by having two
engineers score 50 examples, then checking correlation with the LLM scores. The correlation was
0.81 — sufficient for a blocking signal. The total pipeline runtime was under 4 minutes per PR,
which maintained developer workflow speed.

---

## 🧪 Practice Drills

**Drill 1 — Build Your Story Bank (60 minutes)**

1. List 8–10 projects or contributions from your recent work.
2. Score each against the four selection criteria (impact, recency, relevance, measurability) on a
   1–3 scale.
3. Total each score. The top 5–6 projects become your story bank candidates.
4. For each candidate, write the R (Result) sentence first — if you cannot write a measurable
   result, investigate whether this story is strong enough.

**Drill 2 — Write One Full STAR+T Story (45 minutes)**

1. Pick your strongest story bank candidate.
2. Write each layer: S, T, A, R, +T.
3. Time yourself reading it aloud — target 2.5–3.5 minutes.
4. If it runs over, cut Action detail. If under, add one more technical mechanism to +T.

**Drill 3 — Story Adaptation (20 minutes)**

1. Take the story you wrote in Drill 2.
2. Write three different opening sentences — one for a quality question, one for a challenge
   question, one for a collaboration question.
3. Identify which part of the Action you would emphasise for each variant.

---

## 💬 Interview Q&A

??? question "Tell me about a time you improved an AI system's quality."
I owned retrieval quality for an internal knowledge assistant supporting 200 customer support
agents. The baseline recall@10 was 62%, which was too low for agents to trust the system. I ran an
error analysis on 200 failed queries and found three root causes — dense retrieval failing on exact
product names, poor chunk boundaries, and vocabulary mismatch with the embedding model. I
implemented hybrid BM25 and dense retrieval merged with RRF, re-chunked with overlap, and validated
each change independently using RAGAS on a 300-question eval set. Recall@10 reached 87% after six
weeks. Agent adoption went from 12% to 61% and escalation volume dropped 23%. The key technical
insight was that BM25 recovers the lexical matches that dense retrieval systematically misses —
named entities and product codes — and RRF provides a weight-free fusion method that is robust
across query types.

??? question "Describe a production incident in an AI system you worked on."
We had a customer-facing chatbot for an insurance company where legal flagged a response that told a
user their policy covered a risk it did not. When I measured systematically, our hallucination rate
was 18%. I categorised the failures — 60% came from retrieval gaps, 30% from prompt
misinterpretation, 10% from model confabulation. I added a retrieval confidence filter, rewrote the
system prompt with explicit grounding instructions, and added a self-consistency checking step for
high-stakes policy questions. Within four weeks the rate dropped from 18% to 3.2%. The retrieval
filter alone accounted for 8 percentage points. I also built an NLI-based monitoring system that now
runs nightly regression tests so that class of failure has ongoing detection in production.

??? question "How have you measured success in an LLM project?"
I prefer a layered measurement approach. For retrieval stages I use recall@K and precision@K
measured against a human-labelled ground truth dataset. For generation quality I use RAGAS metrics —
faithfulness and answer relevance — and for high-stakes domains I add an NLI-based hallucination
detector. For production systems I add latency percentiles (P95) and error rates. For business
impact I connect to the closest available proxy metric — support ticket volume, user satisfaction
scores, or adoption rate. The most important principle is to define the eval set before running
experiments, not after, so you cannot cherry-pick results. When I built the eval pipeline for our
legal summarisation product, I locked the golden dataset before any prompt experimentation, which
gave us a clean comparison baseline for every change we shipped.

---

## ✅ End-of-Day Checklist

| Item                                                   | Status |
|--------------------------------------------------------|--------|
| Story bank candidates listed and scored                | ☐      |
| At least one full STAR+T story written                 | ☐      |
| Story timed at 2.5–3.5 minutes spoken                  | ☐      |
| Three opening-sentence variants written for adaptation | ☐      |
| Quantified result identified for each story            | ☐      |
| Drafted one answer for each interview Q above          | ☐      |

--8<-- "_abbreviations.md"
