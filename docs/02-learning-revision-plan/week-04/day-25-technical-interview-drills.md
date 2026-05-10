# Day 25 — Technical Interview Drills — Learn & Revise

> **Pre-reading:** [Week 4 Overview](./index.md) · [Learning Plan](../index.md)

---

## 🎯 What You'll Master Today

Technical interviews for AI engineering roles test five distinct categories of skill, each requiring
a different response strategy. Today you will learn the five question categories, master the RADSS
framework for LLM system design interviews, and work through five fully answered technical question
pairs covering RAG design, debugging, evaluation, agent systems, and tradeoff analysis. By end of
day you will have a repeatable answer structure for every technical question type you are likely to
face.

---

## 📖 Core Concepts

### The Five Categories of AI Engineer Technical Interviews

| Category                | What Is Being Tested                                    | Example Prompt                                                              |
|-------------------------|---------------------------------------------------------|-----------------------------------------------------------------------------|
| **System Design**       | Architecture thinking, scalability, component selection | "Design a RAG system for a legal document Q&A platform"                     |
| **Coding**              | Implementation skill, data handling, eval code          | "Write a function to chunk a PDF and compute chunk-level similarity scores" |
| **Concept Explanation** | Depth of understanding, communication clarity           | "Explain how attention works and when it is a bottleneck"                   |
| **Debugging**           | Systematic diagnosis, production reasoning              | "This RAG system is returning hallucinated answers. What do you check?"     |
| **Trade-off Analysis**  | Judgment, awareness of real-world constraints           | "When would you choose fine-tuning over RAG?"                               |

Most AI engineering interviews are heavy on system design and trade-off analysis at the senior
level. Coding interviews for AI roles lean toward evaluation code, data pipelines, and simple
retrieval logic — not algorithm puzzles.

### System Design: The RADSS Framework

RADSS is a five-step framework for answering LLM system design questions in a structured and
complete way:

| Step                 | Focus                                                 | Output                                                |
|----------------------|-------------------------------------------------------|-------------------------------------------------------|
| **R — Requirements** | Clarify functional and non-functional requirements    | "What volume? What latency SLO? What domain?"         |
| **A — Architecture** | Sketch the high-level component diagram               | Ingestion → Retrieval → Generation → Response         |
| **D — Data**         | Discuss data sources, chunking, indexing, updates     | Index freshness, chunk strategy, embedding model      |
| **S — Scale**        | Address volume, concurrency, and reliability concerns | Caching, async processing, replication                |
| **S — Safety**       | Cover guardrails, content moderation, eval gates      | Hallucination detection, PII handling, output filters |

Always start with Requirements. Interviewers penalise candidates who jump to architecture before
clarifying scope. A good clarifying question demonstrates senior thinking; a missing one signals
that you will build the wrong thing.

### Concept Explanation Pattern

Use this four-step structure for any concept explanation question:

1. **Define** — one sentence, plain language
2. **Example** — one concrete example from production or practice
3. **Tradeoff** — what does this approach sacrifice?
4. **Production consideration** — what would change at scale or in a real system?

This structure takes 60–90 seconds and covers everything an interviewer is scoring.

### Coding Interviews for AI Roles

AI engineering coding interviews test:

- **Data processing** — chunking, cleaning, batching documents
- **Evaluation code** — computing recall@K, precision, RAGAS-style metrics
- **Pipeline logic** — chaining retrieval, prompt construction, and parsing
- **Simple retrieval** — cosine similarity search, reranking logic

They do not typically test: graph algorithms, dynamic programming, or tree traversal. If you
encounter those, the role is likely ML infrastructure, not applied AI.

### Debugging LLM Systems

A systematic debugging approach for a RAG system returning bad results:

```
1. Check the query — is the question well-formed? Out of domain?
2. Check retrieval — run the query against the index. Are relevant chunks in the top-K?
3. Check chunk quality — are chunks well-formed? Do they contain the answer?
4. Check the prompt — is the context being injected correctly? Is the instruction clear?
5. Check the model — is the model version correct? Is temperature appropriate?
6. Check the output — is the failure a retrieval miss or a generation error?
```

Always separate retrieval failures from generation failures. They have different root causes and
different fixes.

---

## 🗺️ Strategy Map

```mermaid
graph LR
    A["Hear Question"] --> B["Clarify Requirements"]
    B --> C["Sketch Architecture"]
    C --> D["Explain Tradeoffs"]
    D --> E["Discuss Scale"]
    E --> F["Address Safety"]

    style A fill:#1976d2,color:#fff
    style B fill:#1976d2,color:#fff
    style C fill:#ff9800,color:#fff
    style D fill:#ff9800,color:#fff
    style E fill:#2e7d32,color:#fff
    style F fill:#2e7d32,color:#fff
```

---

## ⚡ Key Facts — Quick Revision Table

| Concept                     | One-Line Definition                                                       | Why It Matters                                        |
|-----------------------------|---------------------------------------------------------------------------|-------------------------------------------------------|
| RADSS                       | Requirements, Architecture, Data, Scale, Safety — system design framework | Ensures completeness in LLM system design answers     |
| Five question categories    | System design, coding, concept explanation, debugging, trade-off analysis | Each needs a different answer strategy                |
| Concept explanation pattern | Define, Example, Tradeoff, Production consideration                       | Covers everything an interviewer scores in 90 seconds |
| Retrieval failure           | Bad results caused by missing or wrong chunks in top-K                    | First thing to check in a RAG debugging scenario      |
| Generation failure          | Bad results caused by the LLM misusing correct context                    | Requires prompt or model-level fix                    |
| Retrieval confidence filter | Threshold below which the system declines to answer                       | Prevents hallucination when retrieval quality is low  |
| Chunking strategy           | How documents are split before indexing                                   | Major driver of retrieval quality                     |
| Hybrid retrieval            | Combining BM25 and dense retrieval with fusion                            | Handles both lexical and semantic query types         |
| Eval gate                   | Automated quality check that blocks deployment on regression              | Standard practice in production AI systems            |
| Trade-off question          | Question asking you to compare two valid approaches                       | Tests senior judgment, not just knowledge             |

---

## 🔬 Deep Dive with Examples

### Q1 — System Design: Design a RAG System for Legal Document Q&A

**Question:** "Design a RAG system for a legal document question-answering use case."

**Model Answer:**

**Requirements (clarify first):**

- Expected query volume: 1,000 queries/day initially, scaling to 50,000
- Latency SLO: P95 under 3 seconds
- Domain: contracts, case law, internal legal policies
- Accuracy requirements: high — wrong answers in a legal context have serious consequences
- Update frequency: documents updated weekly

**Architecture:**

```
Documents → PDF Extraction → Chunking → Embedding → Vector Store
Query → Embedding → Hybrid Retrieval (BM25 + Dense) → Reranker → Top-5 Chunks
Top-5 Chunks + Query → Prompt Construction → LLM → Output Filter → Response
```

**Data layer:**

- Chunk size: 512 tokens with 10% overlap (legal documents have long paragraphs)
- Embedding model: domain-adapted legal embeddings if available, otherwise text-embedding-3-large
- Index: FAISS with HNSW for fast ANN search; separate BM25 index for term matching

**Scale:**

- Cache frequently repeated queries using a semantic cache (embedding similarity threshold)
- Async ingestion pipeline for document updates with index consistency checks
- Load-balanced serving layer with health checks

**Safety:**

- Retrieval confidence filter: decline to answer if top chunk score < 0.70
- Output filter: NLI-based hallucination detection for answers in high-stakes categories
- Citation requirement: every answer must cite the source document and section
- Audit log: all queries and responses logged for compliance review

---

### Q2 — Debugging: RAG System Returning Hallucinated Answers

**Question:** "Here is a RAG system returning hallucinated answers. What would you check?"

**Model Answer:**

Step 1: **Isolate the failure type.** Run the query against the retrieval stage in isolation. Are
the retrieved chunks relevant? If not, the failure is in retrieval, not generation.

Step 2: **Check retrieval quality.** Look at the top-5 chunks for the failing query. Do any contain
the correct answer? If yes — retrieval is working but generation is ignoring it. If no — retrieval
is the root cause.

Step 3: **If retrieval is the root cause:** Check chunk boundaries — is the answer split across
chunks? Check the embedding model — is the query terminology in-domain? Run BM25 as a cross-check —
if BM25 retrieves correctly but dense does not, the issue is the embedding model.

Step 4: **If generation is the root cause:** Check whether the LLM output is contradicting the
retrieved context (retrieval contains the answer but the model ignores or contradicts it). This
indicates a prompt grounding issue. Add an explicit instruction: "Answer only using facts from the
provided context."

Step 5: **Add instrumentation.** Log the retrieved context alongside every response. Without this,
you cannot diagnose the failure type at scale.

---

### Q3 — Evaluation: How Would You Design an Eval System for an LLM Pipeline?

**Question:** "Walk me through how you would design an evaluation system for an LLM pipeline in
production."

**Model Answer:**

I design evals in three layers: offline, online, and continuous.

**Offline:** Before any deployment, I build a golden dataset of 200–500 representative queries with
human-labelled ground truth answers. I measure retrieval metrics (recall@K, precision@K) separately
from generation metrics (faithfulness, answer relevance, RAGAS scores). This dataset is locked
before experimentation begins.

**Online:** Once in production, I add a sampling-based quality monitor that runs the LLM-as-judge
evaluation on 5% of live queries. Scores are written to a dashboard. Alert thresholds trigger when
any metric drops more than 2% below the deployment baseline.

**Continuous:** Every pull request that touches prompt files, retrieval logic, or model
configuration triggers the full offline eval suite in CI/CD. A regression on any metric blocks the
merge. This is the automated eval pipeline pattern.

---

### Q4 — Agent Design: Design an Agent for an Internal IT Help Desk

**Question:** "Design an LLM agent for an internal IT help desk that can answer questions AND create
tickets."

**Model Answer:**

**Architecture:** ReAct-style agent with three tools: (1) Knowledge search — RAG over IT
documentation, (2) Ticket creation — write to the ticketing API, (3) Ticket status lookup — read
from the ticketing API.

**Control flow:** The agent receives the user query, decides whether a knowledge search is
sufficient or whether ticket creation is needed, executes the appropriate tool sequence, and returns
a response with a ticket number if created.

**Guardrails:** Before ticket creation, the agent must confirm intent with the user. Ticket creation
is a write operation and requires a confirmation step to prevent accidental duplicates. All tool
calls are logged for audit.

**Failure modes to address:** Infinite loops (if the agent keeps searching without finding an
answer — add a max-iterations limit), tool failure (ticket API goes down — add graceful fallback
with a manual link), and scope creep (agent tries to solve problems outside IT scope — add a topic
classifier as a guardrail before routing to the agent).

---

### Q5 — Trade-off: Fine-tuning vs RAG

**Question:** "What are the tradeoffs between fine-tuning and RAG?"

**Model Answer:**

| Dimension          | Fine-tuning                                                     | RAG                                                       |
|--------------------|-----------------------------------------------------------------|-----------------------------------------------------------|
| When to use        | Teaching the model new behaviour or style                       | Grounding answers in specific documents                   |
| Cost               | High — requires training compute and labelled data              | Lower — retrieval infrastructure, no training             |
| Freshness          | Stale — requires retraining to update                           | Dynamic — update the index, not the model                 |
| Explainability     | Low — reasoning is in weights                                   | High — can cite retrieved source                          |
| Hallucination risk | Moderate — model may confabulate learned "facts"                | Lower — grounded in retrieved context                     |
| Best for           | Code generation style, instruction following, domain vocabulary | Document Q&A, knowledge lookup, citation-required answers |

I use RAG as the default for knowledge-grounding tasks because it is cheaper, fresher, and more
explainable. I use fine-tuning when I need to change model behaviour or style at a level that RAG
cannot reach — for example, teaching a model to produce a specific output format or to adopt a
domain's terminology consistently.

---

## 🧪 Practice Drills

**Drill 1 — RADSS Drill (30 minutes)**

1. Pick a system design question: "Design a customer support chatbot for an e-commerce company."
2. Set a timer for 5 minutes. Write Requirements only — do not move to Architecture yet.
3. After Requirements, sketch Architecture in bullet points (3 minutes).
4. Cover Data, Scale, Safety in sequence (2 minutes each).
5. Review: did you address all five RADSS components?

**Drill 2 — Concept Explanation Speed Drill (20 minutes)**

Practice these four topics using the Define → Example → Tradeoff → Production pattern:

- What is embedding similarity?
- What is HNSW?
- What is chain-of-thought prompting?
- What is a semantic cache?

Keep each answer to under 90 seconds.

**Drill 3 — Debugging Simulation (20 minutes)**

1. Imagine a RAG system where 30% of answers for "date-related" queries are wrong.
2. Write a systematic debug checklist following the six-step debugging structure.
3. What is your hypothesis about the root cause? How would you test it?

---

## 💬 Interview Q&A

??? question "Design a RAG system for a legal document Q&A use case."
I'd start with requirements: expected query volume, latency SLO, update frequency, and accuracy
requirements — legal Q&A has near-zero tolerance for hallucination. For architecture: documents go
through PDF extraction, chunking at 512 tokens with overlap, embedding with a domain-adapted model,
and storage in a vector index alongside a BM25 index. At query time I run hybrid retrieval — BM25
for exact legal citations, dense for semantics — fused with RRF, then a reranker to get top-5
chunks. The prompt enforces citation: every answer must reference the source document and section.
For safety I add a retrieval confidence filter — if similarity is below 0.70 the system says "I
cannot find a reliable answer" rather than hallucinating. For scale I add query-level semantic
caching since legal users often ask similar jurisdiction questions. All queries are logged for
compliance audit.

??? question "How would you debug a production LLM system returning hallucinated answers?"
I first isolate whether the failure is in retrieval or generation — these have different root
causes. I run the failing queries through just the retrieval stage and check whether the correct
answer is present in the top-K chunks. If not, I look at chunking — is the answer split across
boundaries? — and at embedding coverage — is the terminology in-domain? If retrieval is correct but
generation hallucinates, I check the prompt grounding instruction and look for cases where the model
is ignoring the context in favour of parametric memory. The fix for generation hallucination is
usually adding explicit grounding instructions and a retrieval confidence filter. I also instrument
the pipeline to log retrieved context alongside every response — without that data, reproducing and
categorising failures at scale is very difficult.

??? question "What are the tradeoffs between fine-tuning and RAG?"
The core tradeoff is between behaviour change and knowledge grounding. RAG is better for grounding
answers in specific, updateable documents — it is cheaper, fresher, and more explainable because you
can cite the retrieved source. Fine-tuning is better for changing how the model responds — style,
format, domain vocabulary, instruction-following patterns. Fine-tuning is expensive in training
compute and labelling cost, and it becomes stale the moment your knowledge base changes. I default
to RAG for knowledge tasks and only consider fine-tuning when I need something that RAG cannot
provide: consistent output format, domain terminology adoption at the vocabulary level, or
instruction-following improvements that prompting alone cannot achieve. In practice, the best
production systems often combine both — a fine-tuned model served with a RAG retrieval layer.

---

## ✅ End-of-Day Checklist

| Item                                                    | Status |
|---------------------------------------------------------|--------|
| Five question categories reviewed and understood        | ☐      |
| RADSS framework practised on one system design question | ☐      |
| Concept explanation pattern drilled on 4 topics         | ☐      |
| Debugging checklist written for a RAG failure scenario  | ☐      |
| Fine-tuning vs RAG tradeoff table reviewed              | ☐      |
| Drafted answers for all three interview Qs above        | ☐      |

--8<-- "_abbreviations.md"
