# Day 27 — Full Mock Loop and Feedback Integration — Learn & Revise

> **Level:** 🔴 Advanced
> **Pre-reading:** [Week 4 Overview](./index.md) · [Learning Plan](../index.md)

---

## 🎯 What You'll Master Today

A mock interview loop is the highest-fidelity preparation tool available before a real interview. Today you will learn how to run a structured full-length mock loop, how to map competencies to question types so your practice covers everything you will actually be scored on, and how to integrate feedback systematically rather than just noting "I need to improve." By end of day you will have scored your own mock performance and produced a prioritised improvement plan for Day 28.

---

## 📖 Core Concepts

### Mock Interview Structure and Timing

A full AI engineering interview loop typically spans 5–6 rounds. This is the structure to simulate:

| Round | Type | Duration | What Is Scored |
|---|---|---|---|
| Recruiter screen | Verbal — motivation, background | 30 min | Communication, role fit |
| Technical phone screen | System design or concept | 45 min | Technical depth, communication |
| System design | LLM system architecture | 60 min | RADSS coverage, tradeoff thinking |
| Coding | Eval code or data pipeline | 45 min | Code clarity, problem solving |
| Behavioral 1 | STAR stories, leadership | 45 min | Influence, ambiguity, communication |
| Behavioral 2 | Cross-functional, collaboration | 45 min | Stakeholder, decision-making |

For a solo mock session, simulate one round at a time. For a partner mock, run 2–3 rounds back to back to build stamina.

### Mock Session Rules

- **No pausing or restarting** — treat it as real. If you stumble, recover naturally.
- **Record audio or video** — you will miss things in retrospect that are obvious on playback.
- **Time every answer** — most candidates run over by 30–60 seconds on STAR stories and under on system design.
- **No notes open during answer delivery** — reviewing your notes is fine in the prep phase, not answer phase.

### Competency-to-Question Mapping

Use this table to ensure your mock loop covers all tested competencies:

| Competency | Question Type | Sample Question |
|---|---|---|
| RAG system design | System design | "Design a document Q&A system for a regulated industry" |
| LLM evaluation | Concept + coding | "How would you measure hallucination in a production RAG system?" |
| Debugging | Debugging | "A RAG system returns wrong answers for 30% of date queries. What do you check?" |
| Fine-tuning vs RAG | Trade-off | "When would you choose fine-tuning over RAG for a legal application?" |
| Agent design | System design | "Design a ReAct agent for an IT help desk with ticket creation capability" |
| Production incident | Behavioral | "Tell me about a time an AI system in production failed and how you handled it" |
| Influence without authority | Behavioral | "Describe a time you changed a technical decision you didn't control" |
| Navigating ambiguity | Behavioral | "Tell me about a project where requirements were unclear at the start" |
| Stakeholder communication | Behavioral | "How do you explain a model failure to a non-technical executive?" |
| Gap identification | Meta | "What is your biggest technical weakness as an AI engineer?" |

Run at least one question from each row in your mock session.

### Sample Technical Questions with Model Answers

#### "How would you measure hallucination in a production RAG system?"

A complete answer covers four layers:

1. **Offline eval:** RAGAS faithfulness score against a golden dataset. Faithfulness measures whether the answer is supported by the retrieved context. Set a minimum threshold before any deployment.
2. **NLI-based detection:** For high-stakes domains, use a fine-tuned NLI model (e.g., DeBERTa-v3) to perform premise-hypothesis classification where the retrieved context is the premise and each sentence of the LLM output is the hypothesis. Flag any CONTRADICTION labels.
3. **Production sampling:** Sample 5% of live queries and run both RAGAS and NLI checks. Write results to a monitoring dashboard with alert thresholds.
4. **LLM-as-judge for edge cases:** For queries that trigger borderline scores, route to a GPT-4 evaluator with a structured rubric. Use this sparingly — it is expensive at scale.

#### "Design a ReAct agent for customer service with escalation capability"

**Architecture:**
- Tools: (1) Knowledge search — RAG over product documentation, (2) Order status lookup — read-only API, (3) Escalate to human — write API to create a human handoff ticket.
- Control flow: ReAct loop — Thought → Action → Observation — with a max 8-step limit.
- Guardrails: Escalation requires a confidence check — if the agent cannot resolve after 4 steps, it escalates automatically. The escalation tool is the only write operation; all others are read-only.
- Memory: Short-term context window only; no persistent memory across sessions (compliance constraint).

**Safety:** All tool calls logged. Escalation triggers send the full conversation history to the human agent. PII fields masked in logs.

### Sample Behavioral Questions with Model STAR Answers

#### "Tell me about a time you had to make a technical decision under significant time pressure."

**S:** We were 48 hours from a product launch when our model evaluation revealed an unexpected drop in quality for a key query category.

**T:** I had to decide whether to delay the launch or ship with a known limitation. The decision needed to be made in 2 hours so the engineering team could act on the outcome.

**A:** I quickly scoped the impact: the quality drop affected 12% of expected query volume, and within that, 80% of the failures were recoverable with a simple prompt guard. I wrote a two-paragraph risk summary and proposed three options: (1) delay 48 hours and fix properly, (2) ship with the prompt guard covering the common failures (covers 80% of cases in 4 hours of work), (3) ship with a feature flag that disables the affected query category. I presented to the PM and CTO. We chose option 2.

**R:** We shipped on time. The prompt guard on-call showed the affected category's quality improved to acceptable levels. The 20% of failures not covered by the guard triggered human review. Post-launch we addressed the root cause in the following sprint.

**+T:** The prompt guard was a category classifier run before the main prompt — if the query matched the problematic category, a domain-specific system prompt addition was injected. It added under 100ms latency. The root cause was a distribution shift in how users were phrasing date-range queries; we fixed it by adding 200 examples to the fine-tuning dataset in the next training run.

---

## 🗺️ Strategy Map

```mermaid
graph LR
    A["Schedule Mock Loop"] --> B["Run Each Round Timed"]
    B --> C["Record and Review"]
    C --> D["Score Against Rubric"]
    D --> E["Identify Top 3 Gaps"]
    E --> F["Build Day 28 Fix Plan"]

    style A fill:#1976d2,color:#fff
    style B fill:#1976d2,color:#fff
    style C fill:#ff9800,color:#fff
    style D fill:#ff9800,color:#fff
    style E fill:#c62828,color:#fff
    style F fill:#2e7d32,color:#fff
```

---

## ⚡ Key Facts — Quick Revision Table

| Concept | One-Line Definition | Why It Matters |
|---|---|---|
| Mock loop | Full-length simulated interview with timed rounds | Highest-fidelity prep before a real interview |
| Round stamina | Ability to maintain quality across 4–6 interview rounds | Real loops are exhausting; practice builds resilience |
| Competency mapping | Table linking each competency to a question type and sample question | Ensures mock coverage is complete |
| Recording review | Watching your own mock interview playback | Catches issues (pace, filler words, structure) you miss in the moment |
| Rubric scoring | Scoring answers against defined dimensions | Converts vague "I did poorly" into specific fixes |
| Answer timing | Measuring STAR story duration and system design depth | Most candidates run over on stories and under on design |
| Top-3 gap list | Prioritised list of weakest answer areas | The input to Day 28's targeted revision |
| Recovery phrase | A scripted way to recover from a stumble | "Let me take a moment to think about that clearly" |
| Feedback integration | Converting feedback observations into specific practice actions | Feedback without action produces no change |
| Partner mock | Mock interview with another person asking questions | Forces you to perform without notes |

---

## 🔬 Deep Dive with Examples

### Feedback Integration Framework

Feedback is only useful if it leads to a specific practice action. Use this framework:

| Feedback Observation | Root Cause Category | Action |
|---|---|---|
| "Your STAR story ran 5 minutes" | Answer length | Time and cut — identify which section to compress |
| "I wasn't sure what your role was" | Situation clarity | Add one sentence: "My responsibility was X" before Action |
| "The system design was shallow" | RADSS coverage | Check which of the 5 RADSS components you skipped |
| "You used a lot of filler words" | Delivery habit | Record a 60-second answer. Count um/uh. Aim for zero. |
| "The technical depth was unclear" | +T layer | Write out the +T section of your weakest story on paper |
| "You didn't give numbers" | Quantification | For every Result, ask: what changed and by how much? |
| "The answer was too abstract" | Example density | Add one concrete example sentence in every Core Concepts section |
| "You seemed uncertain on trade-offs" | Trade-off practice | Run 3 trade-off questions using the comparison table format |

### Scoring Rubric — Mock Interview Dimensions

Score each answer 1–5 on the following dimensions:

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| **Clarity** | Hard to follow | Generally clear with some confusion | Crystal clear opening and closing |
| **Technical depth** | No mechanism explained | Mechanism mentioned | Mechanism + eval + tradeoff explained |
| **Quantification** | No numbers | One metric | Multiple metrics with baseline+outcome |
| **Structure** | Unstructured narrative | Loose STAR | Clean STAR+T with clear transitions |
| **Concision** | Over 4 minutes | 3–4 minutes | 2.5–3.5 minutes, no padding |

A score of 3+ on all dimensions is the pass bar. A 5 on technical depth + quantification is a strong hire signal.

---

## 🧪 Practice Drills

**Drill 1 — Timed Technical Round (45 minutes)**

1. Set a timer for 45 minutes.
2. Draw one question from each row of the competency mapping table: one system design, one concept/coding, one trade-off.
3. Answer each question aloud, timed. Do not stop or restart.
4. After all three, score yourself on the rubric. Write your scores down.

**Drill 2 — Timed Behavioral Round (45 minutes)**

1. Set a timer for 45 minutes.
2. Draw three questions from the behavioral rows of the competency table.
3. Answer each as a complete STAR+T story, timed.
4. Record if possible. Play back and count filler words in one answer.

**Drill 3 — Feedback Action Planning (20 minutes)**

1. Review your scores from Drills 1 and 2.
2. Identify the bottom two scores. For each, write the root cause category and the specific action from the Feedback Integration Framework.
3. This becomes your Day 28 priority list.

---

## 💬 Interview Q&A

??? question "How do you prepare for a technical interview loop for an AI engineering role?"
    I treat preparation as a five-layer process. First, I decode the JD to extract the 5–7 competency clusters being tested. Second, I build a story bank — 5–6 tier-1 STAR+T stories covering quality improvement, production incidents, cross-functional alignment, and technical decisions. Third, I run targeted technical drills: one system design question per day using RADSS, concept explanation drills using the Define-Example-Tradeoff-Production pattern, and trade-off comparison tables. Fourth, I run at least one full timed mock loop — recording if possible — and score myself against a rubric. Fifth, I run a gap-close sprint on the lowest-scoring dimensions before the real loop. The key principle is that mock loops with scoring are infinitely more effective than reading or reviewing without pressure.

??? question "What is your process for integrating interview feedback?"
    I start by categorising the feedback rather than reacting to it. Most feedback falls into one of eight root cause categories: answer length, situation clarity, RADSS coverage, delivery habits, technical depth in the +T layer, quantification, example density, or trade-off confidence. Once I have the category, the fix is specific — not "do better" but "time and cut the Action section of story 3" or "add the +T layer to the retrieval quality story." I log each fix as a practice action and run it within 24 hours of receiving the feedback. The common mistake is to write feedback down and then continue with the same preparation approach. Feedback should redirect practice, not just annotate it.

??? question "How do you manage nerves in a high-stakes technical interview?"
    I use three techniques. First, I prepare a recovery phrase for when I stumble: "Let me take a moment to organise my thinking on that" — this is far better than filling silence with uncertainty. Second, I connect the first answer of every interview to a story I have rehearsed until it is automatic — starting from a confident, fluent answer resets the emotional state. Third, I remind myself before the call that the interviewer is not adversarial — they are hoping I am a strong candidate because hiring is hard. Reframing the interaction as collaborative rather than evaluative significantly reduces the cortisol response. On the technical side, I also know my opening sentence for every major question type — RADSS starts with "Let me first clarify the requirements", STAR starts with the Situation in one sentence. Automatic opening sentences eliminate the moment of blankness that triggers anxiety.

---

## ✅ End-of-Day Checklist

| Item | Status |
|---|---|
| Mock loop structure reviewed and scheduled | ☐ |
| Competency-to-question mapping table reviewed | ☐ |
| Timed technical round completed (Drill 1) | ☐ |
| Timed behavioral round completed (Drill 2) | ☐ |
| Self-scored on rubric — all dimensions | ☐ |
| Top 3 gaps identified with specific fix actions | ☐ |
| Day 28 priority list written | ☐ |

---

## 🐍 Bonus: Mock Interview Answer Scorer (Python)

```python
"""
mock_scorer.py
Score a mock interview answer against the 5-dimension rubric.
Run interactively: python mock_scorer.py
"""

from dataclasses import dataclass, field
from typing import List

DIMENSIONS = [
    "Clarity",
    "Technical depth",
    "Quantification",
    "Structure (STAR+T)",
    "Concision",
]

PASS_BAR = 3
HIRE_SIGNAL_DIMS = ["Technical depth", "Quantification"]
HIRE_SIGNAL_SCORE = 5


@dataclass
class AnswerScore:
    question: str
    scores: dict = field(default_factory=dict)

    def overall(self) -> float:
        return sum(self.scores.values()) / len(self.scores) if self.scores else 0.0

    def passed(self) -> bool:
        return all(v >= PASS_BAR for v in self.scores.values())

    def strong_hire_signal(self) -> bool:
        return all(
            self.scores.get(d, 0) >= HIRE_SIGNAL_SCORE for d in HIRE_SIGNAL_DIMS
        )

    def gaps(self) -> List[str]:
        return [dim for dim, score in self.scores.items() if score < PASS_BAR]


def score_answer(question: str) -> AnswerScore:
    print(f"\n📋 Scoring: '{question}'")
    result = AnswerScore(question=question)
    for dim in DIMENSIONS:
        while True:
            try:
                score = int(input(f"  {dim} (1–5): "))
                if 1 <= score <= 5:
                    result.scores[dim] = score
                    break
                print("  Please enter a number between 1 and 5.")
            except ValueError:
                print("  Invalid input — enter a number.")
    return result


def print_report(scores: List[AnswerScore]) -> None:
    print("\n" + "=" * 50)
    print("📊 MOCK INTERVIEW SCORE REPORT")
    print("=" * 50)
    for s in scores:
        status = "✅ PASS" if s.passed() else "❌ GAP"
        hire = " 🌟 STRONG HIRE SIGNAL" if s.strong_hire_signal() else ""
        print(f"\n{status}{hire}")
        print(f"  Question: {s.question}")
        print(f"  Overall: {s.overall():.1f}/5")
        for dim, score in s.scores.items():
            bar = "█" * score + "░" * (5 - score)
            print(f"  {dim:<25} {bar} {score}/5")
        if s.gaps():
            print(f"  ⚠️  Gaps: {', '.join(s.gaps())}")

    all_gaps = {}
    for s in scores:
        for g in s.gaps():
            all_gaps[g] = all_gaps.get(g, 0) + 1

    if all_gaps:
        print("\n🎯 TOP GAPS TO FIX (by frequency):")
        for dim, count in sorted(all_gaps.items(), key=lambda x: -x[1]):
            print(f"  {dim}: appeared in {count} answer(s)")


def main():
    print("🎤 Mock Interview Answer Scorer")
    print("Enter your questions and score each dimension 1–5.\n")
    questions = []
    while True:
        q = input("Enter a question (or press Enter to finish): ").strip()
        if not q:
            break
        questions.append(q)

    if not questions:
        print("No questions entered. Exiting.")
        return

    scores = [score_answer(q) for q in questions]
    print_report(scores)


if __name__ == "__main__":
    main()
```

Usage:
```bash
python mock_scorer.py
```
Enter each question you answered in your mock session, then score each dimension. The script prints a gap report and identifies your priority fix areas.

