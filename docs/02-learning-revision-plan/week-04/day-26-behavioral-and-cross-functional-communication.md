# Day 26 — Behavioral and Cross-functional Communication — Learn & Revise

> **Pre-reading:** [Week 4 Overview](./index.md) · [Learning Plan](../index.md)

---

## 🎯 What You'll Master Today

At the senior level, behavioral interviews in AI engineering are not a soft skills check — they are
a leadership capability assessment. Interviewers want to see that you can influence technical
direction without formal authority, communicate AI risks to non-technical stakeholders, and navigate
ambiguity without losing progress. Today you will master the four core behavioral themes tested in
senior AI roles, learn frameworks for cross-functional communication, and walk through three fully
worked STAR+ stories covering the hardest behavioral scenarios AI engineers face.

---

## 📖 Core Concepts

### Why Behavioral Interviews Matter at Senior AI Levels

At L4, a strong technical answer is sufficient to pass a behavioral round. At L5 and above, the bar
shifts: the interviewer is calibrating whether you can operate beyond your own individual
contribution. Senior AI engineers face situations where the right technical path conflicts with
business pressure, where a model risk needs to be communicated to people who do not understand
probability, and where alignment across ML, product, legal, and leadership must be built through
influence rather than hierarchy.

Behavioral interviews at senior levels are testing leadership, not just execution. Every story you
tell should show a moment where you shaped an outcome — not just completed a task.

### Core Behavioral Themes in Senior AI Roles

| Theme                                      | What Interviewers Are Scoring                                        | Signal to Demonstrate                                                  |
|--------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------|
| **Influence without authority**            | Can you change technical direction without being the decision-maker? | Built consensus through data and persuasion, not mandate               |
| **Navigating ambiguity**                   | Can you make progress when requirements are unclear?                 | Defined scope proactively, shipped incrementally, updated stakeholders |
| **Stakeholder communication**              | Can you represent technical work to non-engineers clearly?           | Translated risk into business terms, received non-technical alignment  |
| **Technical-to-non-technical translation** | Can a PM or executive understand your explanation?                   | Used analogy, avoided jargon, focused on consequences not mechanism    |

These four themes cover approximately 80% of behavioral questions in senior AI engineering
interviews. Prepare one strong story per theme minimum.

### Cross-functional Communication: Explaining LLM Risks

Explaining AI system risks to PMs, legal, or executives requires a deliberate communication
strategy. The common failure mode is over-explaining mechanism and under-explaining consequence.

**Framework for AI risk communication:**

1. **Lead with consequence, not mechanism** — "This means one in thirty answers could cite a law
   that doesn't apply to the user's case" is more actionable than "our hallucination rate is 3.2%."
2. **Anchor to a comparable known risk** — "This is similar to the disclaimer we put on medical
   advice — we flag uncertainty rather than presenting it as fact."
3. **Quantify the exposure** — Specific numbers are more credible than adjectives. "Based on our
   eval set, the error rate is 3.2% and it clusters in multi-jurisdiction queries."
4. **Propose the control** — "The recommended control is a retrieval confidence filter that declines
   to answer when the system is uncertain. This would reduce the error rate to under 0.5%."
5. **Define the decision you need** — "I need approval to add the decline-to-answer behaviour, which
   will affect approximately 8% of queries."

This five-step pattern works for any audience: PM, legal, exec.

### Handling Disagreement and Pushback

Senior engineers regularly face moments where they must disagree with a product decision, a
technical direction, or a deployment plan. The failure modes are: silent compliance (leading to bad
outcomes) or unproductive escalation (damaging relationships).

**Framework for principled disagreement:**

1. **Separate the person from the decision** — "I want to flag a concern with the plan" not "I think
   this decision is wrong."
2. **State your position with evidence** — "Based on our eval data, shipping without the confidence
   filter increases the hallucination-visible-to-user rate from 3% to 18%."
3. **Acknowledge the constraint** — "I understand the Q2 deadline is fixed and the rollback cost is
   significant."
4. **Propose an alternative** — "My proposal is to ship with the filter enabled — it adds 3 days of
   work but keeps the launch date."
5. **Commit to the decision** — "If we decide to proceed without the filter, I will prioritise the
   post-launch monitoring dashboard to catch issues as quickly as possible."

The RFC (Request for Comment) process in many engineering cultures is the formal channel for this
pattern. An informal RFC — a written document with your position and supporting evidence — is
professionally appropriate in most contexts.

---

## 🗺️ Strategy Map

```mermaid
graph LR
    A["Situation"] --> B["Identify Behavioral Theme"]
    B --> C["STAR Frame"]
    C --> D["Add Technical Depth"]
    D --> E["State Stakeholder Impact"]
    E --> F["Confirm Level Signal"]

    style A fill:#1976d2,color:#fff
    style B fill:#1976d2,color:#fff
    style C fill:#ff9800,color:#fff
    style D fill:#ff9800,color:#fff
    style E fill:#2e7d32,color:#fff
    style F fill:#2e7d32,color:#fff
```

---

## ⚡ Key Facts — Quick Revision Table

| Concept                         | One-Line Definition                                               | Why It Matters                                                |
|---------------------------------|-------------------------------------------------------------------|---------------------------------------------------------------|
| Influence without authority     | Changing direction through persuasion and data, not mandate       | Tested heavily at L5+ levels                                  |
| Navigating ambiguity            | Making progress when requirements are unclear or contested        | AI projects are frequently unclear at the outset              |
| Stakeholder communication       | Translating technical work for non-engineering audiences          | Non-technical alignment is often the bottleneck               |
| Consequence-first communication | Lead with business impact, not technical mechanism                | Non-technical audiences respond to outcome, not process       |
| Quantified risk                 | Stating failure rates as specific numbers with context            | More credible and actionable than qualitative claims          |
| Principled disagreement         | Expressing a technical objection with evidence and an alternative | Senior engineers are expected to voice informed disagreement  |
| RFC                             | Written document presenting a technical position for review       | Formal channel for principled disagreement                    |
| Level signal                    | Story element that demonstrates senior-level thinking             | Every story should contain at least one                       |
| STAR+ for behavioral            | STAR story with added stakeholder and business impact layer       | Differentiates technical leaders from individual contributors |
| Cross-functional alignment      | Getting ML, product, legal, and business to agree on a direction  | A key L5 competency in AI engineering                         |

---

## 🔬 Deep Dive with Examples

### Story 1 — Disagreed with a Product Decision About Deploying an Unsafe Model Feature

**Situation:** The product team wanted to ship a new legal document summarisation feature without
any hallucination control. The go-live date was set for two weeks out. Our eval data showed an
answer faithfulness score of 0.71 on the RAGAS benchmark — meaning roughly 29% of answers contained
at least one unsupported claim. In a legal product, this was unacceptable, but the timeline pressure
was real.

**Task:** I needed to communicate the risk clearly enough that the team would either delay to add
controls or accept a reduced scope at launch, without creating a conflict that slowed down the
feature itself.

**Action:** I prepared a one-page risk brief — not a long technical doc. I translated the 0.71
faithfulness score into: "Based on our current eval set, approximately 1 in 3.5 summaries contains
at least one legal claim not found in the source document. For users relying on these summaries in
contract review, this could lead to a missed liability clause." I attached three specific examples
from our evaluation where the model produced plausible but incorrect legal statements. I shared this
with the PM, legal lead, and engineering director in a 30-minute meeting, not a Slack message. I
proposed two alternatives: (1) add a retrieval confidence filter + source citation system (3 days of
work) and ship without the summarisation feature for complex multi-party contracts, or (2) delay the
full launch by 5 days to implement and test the filter properly.

**Result:** The team chose option 2. We implemented the retrieval confidence filter and mandatory
source citations. The launch was 5 days later than originally planned. Post-launch faithfulness
score improved to 0.94. Legal approved expanded rollout to enterprise customers, which was blocked
on the safety controls.

**+Technical:** The confidence filter worked by measuring cosine similarity between the query
embedding and the top retrieved chunk. If the score fell below 0.72, the system appended "I am not
able to find a reliable answer to this specific question" rather than generating. This pattern was
adopted as a standard in two other features the team shipped in the following quarter.

---

### Story 2 — Led Alignment Across ML, Product, and Legal on a Policy Control Rollout

**Situation:** We were adding content policy controls to a customer-facing chatbot for a financial
services client. The technical implementation was straightforward — an output classifier to detect
and block certain response categories. The challenge was that ML, product, and legal had
fundamentally different views of acceptable false-positive rates. ML wanted precision above 99%;
legal wanted recall above 99%; product wanted to block less than 2% of queries.

**Task:** I was the technical lead and needed to drive alignment to a single configuration that all
three teams could accept, on a deadline of four weeks before an external compliance audit.

**Action:** I recognised that the disagreement was not a technical problem — it was a values
conflict about which type of error was worse. I facilitated a three-way meeting where I presented
the precision-recall tradeoff curve for the classifier visually, showing what each team's preferred
threshold would mean in practice. For ML's 99% precision threshold: "This would miss 40% of policy
violations, which legal cannot accept." For legal's 99% recall threshold: "This would block 12% of
legitimate queries — 600 user sessions per day would see an error message when asking valid
questions." I then proposed a middle position: 98.5% precision with a human review queue for
borderline cases, reducing legal's exposure to missed violations while keeping the false-positive
block rate at under 3%. I wrote this up as a one-page decision memo and circulated it with a 48-hour
comment window before the final call.

**Result:** All three teams signed off on the middle configuration. The human review queue — staffed
by a rotational compliance team member — resolved 15–20 borderline cases per week. We passed the
compliance audit. The decision memo became the model for how cross-team technical tradeoffs were
documented on the team going forward.

**+Technical:** The classifier was a fine-tuned DeBERTa-v3-base model on a 1,200-example labelled
dataset. The precision-recall curve analysis was generated using scikit-learn's
`classification_report` across 10 threshold values, presented as a table showing block rate,
violation miss rate, and user impact at each threshold. Visualising the tradeoff as concrete user
impact numbers — instead of abstract F1 scores — was what unlocked the alignment.

---

### Story 3 — Communicated a Production Incident to Non-Technical Stakeholders

**Situation:** Our AI-powered claims triage system at an insurance company misclassified a
high-urgency claim as low-priority, delaying the response by 36 hours. The customer escalated to the
exec team. The CEO asked for an incident explanation in 2 hours.

**Task:** I was the engineer on call and needed to produce an accurate, honest, non-technical
explanation of what happened, why, and what we were doing about it — for an audience that included
the CEO, the Head of Customer Experience, and the General Counsel.

**Action:** I wrote a one-page incident summary using plain language. I avoided all ML terminology
in the body of the document. The structure was: (1) What happened — the claim was filed at 11pm on a
Friday and the model classified it incorrectly; (2) Why it happened — the model had a known weakness
for claims with unusual descriptions that differed from its training data; (3) What we did — we
manually reclassified the claim and called the customer within 2 hours of identifying the error; (4)
What we are changing — we are adding a human review step for all claims filed outside business hours
with low confidence scores until we retrain the model; (5) Timeline — the human review step will be
live by Monday. I did not use words like "embedding", "classifier threshold", or "confidence score"
in the document. I included one analogy: "This is similar to a new employee who has not yet
encountered this type of case — they flagged it as routine when it required escalation." I presented
it verbally in a 15-minute meeting and offered to provide a technical appendix separately.

**Result:** The CEO approved the interim human review step immediately. The General Counsel
appreciated the incident be framed clearly and asked for a formal process for AI system incident
notification. The customer received a personal apology and their claim was expedited. The incident
summary format I wrote became the template for subsequent AI incident reports.

---

## 🧪 Practice Drills

**Drill 1 — Behavioral Theme Classification (15 minutes)**

Read the following questions and identify which of the four behavioral themes each is testing:

1. "Tell me about a time you pushed back on a timeline."
2. "Describe a project where the requirements changed after you started."
3. "How do you explain model risk to a non-technical executive?"
4. "Tell me about a time you influenced a decision you did not control."

Answers: (1) Principled disagreement, (2) Navigating ambiguity, (3) Technical-to-non-technical
translation, (4) Influence without authority.

**Drill 2 — Consequence-First Translation Exercise (20 minutes)**

Take each of the following technical metrics and write a one-sentence consequence-first translation
targeting a PM or executive:

1. Hallucination rate: 3.2%
2. Retrieval recall@10: 62%
3. P95 latency: 4.2 seconds
4. Model confidence filter block rate: 8%

Practice making each sentence specific, non-jargon, and action-oriented.

**Drill 3 — Principled Disagreement Roleplay (30 minutes)**

1. Set up this scenario: "Your PM wants to ship a new AI feature next week. Your eval shows the
   model fails on 15% of edge case inputs that are common in your user base."
2. Write out your principled disagreement following the five-step framework: separate person from
   decision, state position with evidence, acknowledge constraint, propose alternative, commit to
   outcome.
3. Read it aloud. Does it sound respectful, specific, and solution-oriented?

---

## 💬 Interview Q&A

??? question "Tell me about a time you influenced a technical decision without formal authority."
We were building content policy controls for a financial chatbot and ML, product, and legal had
conflicting views on the acceptable threshold for the output classifier. ML wanted 99% precision,
legal wanted 99% recall, and product wanted under 2% false positives. These were mathematically
incompatible. I ran the precision-recall curve analysis and presented the concrete implications of
each team's preferred threshold — not in abstract F1 terms but as user sessions blocked per day and
policy violations missed per week. I wrote a one-page decision memo proposing a middle configuration
with a human review queue for borderline cases, circulated it with a 48-hour comment window, and
brought the three teams together to align on the decision. All teams agreed. I did not have
authority over any of those teams — what I had was the analysis, a clear proposal, and a structured
process for the conversation.

??? question "How do you explain complex AI risks to a non-technical audience?"
I follow a five-step pattern. First, I lead with consequence, not mechanism — "one in thirty answers
could cite a law that doesn't apply" lands better than "our hallucination rate is 3.2%." Second, I
anchor to a comparable familiar risk — analogies make abstract probabilities concrete. Third, I
quantify the exposure specifically — adjectives like "sometimes" or "occasionally" erode
credibility. Fourth, I propose the control in plain language — "we add a step where the system says
it cannot find a reliable answer rather than guessing." Fifth, I state the decision I need — "I need
approval to add this step, which affects 8% of queries." This pattern works for any audience and
usually produces alignment faster than a technical explanation because it puts the audience in the
position of making an informed decision rather than decoding jargon.

??? question "Describe a time you navigated ambiguity in an AI project."
We were asked to build a claims triage model for an insurance company but the definition of "
urgency" was different across three business units — and no one had formally defined it. Rather than
waiting for alignment that was not coming, I ran a three-day discovery sprint: I interviewed 6
claims adjusters, extracted 15 proxy signals that they used to judge urgency manually, and built a
preliminary scoring rubric. I shared the rubric with the business units as a working draft and asked
them to tell me where it was wrong rather than asking them to define urgency from scratch. This
produced actionable feedback in two days. We launched with a model trained on the proxy signals,
with an explicit plan to retrain after 60 days of production labels. The model was live in 6 weeks
instead of the 14 weeks the original scope suggested. The lesson was: when requirements are
ambiguous, build a draft and ask stakeholders to react to something concrete.

---

## ✅ End-of-Day Checklist

| Item                                                  | Status |
|-------------------------------------------------------|--------|
| Four core behavioral themes reviewed                  | ☐      |
| Three STAR+ stories read and understood               | ☐      |
| Consequence-first translation exercise completed      | ☐      |
| Principled disagreement script written for a scenario | ☐      |
| Behavioral theme identified for 4 practice questions  | ☐      |
| Drafted answers for all three interview Qs above      | ☐      |

--8<-- "_abbreviations.md"
