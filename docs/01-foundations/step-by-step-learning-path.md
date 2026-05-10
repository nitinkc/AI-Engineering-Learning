# Step-by-Step Learning Path

## Goal

Build interview-ready depth in:

- LLM system design
- RAG quality and debugging
- Agent reliability and tool orchestration
- Production operations, evals, and tradeoffs

## Daily Systematic Plan (New)

Use the structured day-by-day plan to execute this path with concrete daily objectives, theory drills, and labs.

| Resource           | Link                                                                         |
|:-------------------|:-----------------------------------------------------------------------------|
| 4-Week daily index | [Learning and Revision Plan - Daily System](learning-revision-plan/index.md) |
| Week 1 pages       | [Week 1 - LLM and RAG Core](learning-revision-plan/week-01/index.md)         |
| Week 2 pages       | [Week 2 - Agents and LangGraph](learning-revision-plan/week-02/index.md)     |
| Week 3 pages       | [Week 3 - Evals and Production](learning-revision-plan/week-03/index.md)     |
| Week 4 pages       | [Week 4 - Interview Conversion](learning-revision-plan/week-04/index.md)     |

### Daily Loop (60-90 min)

1. Concept refresh
2. Build or debugging task
3. Recall drill from memory
4. Interview translation into STAR bullets
5. Error log update

## 4-Week Path

### Week 1: LLM Architecture + RAG Core

- Build request -> retrieval -> response mental model.
- Practice identifying retrieval misses vs generation misses.
- Explain exact-match failure (`Order #1766` vs `Order #1767`).

### Week 2: Agents + Tool Reliability

- Compare workflow vs agent.
- Design schema-first tool calling.
- Add retries, timeout, escalation, and approval gates.

### Week 3: Evals + Observability + Deployment

- Build a golden dataset.
- Track quality, latency, and cost.
- Define deploy gates and rollback rules.

### Week 4: Interview Conversion

- Build 8 reusable STAR+T stories.
- Practice 90-second and 3-minute forms.
- Run mock loops with scoring and correction.

## 4. Four-Week Learning and Revision Plan

This plan assumes you already know AI/ML basics and need interview-focused industry readiness.

## Week 1: LLM App Architecture + RAG

Goal : Become confident designing, explaining, and debugging RAG-based LLM applications.

### Day 1: LLM System Design Basics

Revise:

- Chatbot architecture
- Prompt pipeline
- Context builder
- Model gateway
- Output parser
- Guardrails
- Logs and traces

Practice:

```text
Design an enterprise chatbot over internal documents.
```

### Day 2: RAG Pipeline

Revise:

- Document loaders
- Chunking
- Embeddings
- Vector stores
- Retrieval
- Reranking
- Grounded generation

Build or revise:

```text
PDF/docs → chunks → embeddings → vector DB → retriever → answer with citations
```

### Day 3: RAG Debugging

Focus on failure modes:

- Retrieval miss
- Bad chunking
- Hallucination
- Stale documents
- Weak embeddings
- Poor metadata
- Context overload
- Conflicting documents

Prepare an answer for:

```text
How would you improve RAG answer quality?
```

### Day 4: Prompt Engineering for Production

Revise:

- System prompts
- Developer instructions
- Few-shot examples
- Structured output
- JSON schemas
- Refusal behavior
- Context compression
- Prompt versioning

Key framing:

```text
Prompt engineering in production is instruction design + context design + output constraints + evaluation.
```

### Day 5: Vector DBs and Search

Revise:

- FAISS
- Pinecone
- Chroma
- Weaviate
- OpenSearch
- Metadata filtering
- Hybrid search
- Reranking

Interview-level understanding is enough.

### Day 6: Mini System Design Practice

Prepare 3 architectures:

```text
1. Retail product assistant using POS/CRM/e-commerce data
2. Learning assistant with memory and adaptive questioning
3. Internal engineering knowledge assistant
```

### Day 7: Revision and Mock Interview

Prepare concise answers:

```text
- What is RAG?
- How do you debug RAG?
- How do you evaluate RAG?
- When would you fine-tune instead of using RAG?
- How do you reduce hallucination?
```

## Week 2: Agents, LangGraph, Tool Calling, A2A

Goal : Become strong in agentic workflow interviews.

### Day 8: Agent Basics

Revise:

- Agent vs chain vs workflow
- Tool calling
- ReAct
- Planner-executor
- Reflection
- Memory
- State

Key interview line:

```text
Agents are useful when the path is dynamic, but production reliability often requires constraining them with deterministic workflows.
```

### Day 9: Tool Calling and Function Calling

Revise:

- Tool schemas
- JSON arguments
- Tool validation
- Tool result injection
- Error handling
- Permission checks
- Dry-run mode

Prepare example:

```text
User asks to cancel subscription
→ agent identifies intent
→ checks user identity
→ calls subscription API
→ verifies cancellation
→ logs action
→ confirms result
```

### Day 10: LangGraph

Focus heavily here.

Understand:

- Nodes
- Edges
- Conditional edges
- State
- Checkpointing
- Retries
- Human approval
- Tool node
- Error node

Practice explaining:

```text
Start
 → classify task
 → retrieve context
 → call tool
 → verify result
 → if failed retry/escalate
 → final response
```


### Day 11: Multi-Agent / A2A Patterns

Revise:

- Manager-worker
- Planner-executor
- Critic-reviewer
- Specialist agents
- Debate pattern
- Delegation
- Shared state
- Message passing

Know the risks:

- Infinite loops
- Conflicting instructions
- Tool misuse
- High cost
- Latency
- Poor observability


### Day 12: Automation Systems

Revise:

- Triggers
- Workflow engines
- Browser automation
- API integrations
- Webhooks
- Queues
- State transitions
- Retry policies
- Idempotency

Core pattern:

```text
Trigger
 → classify
 → plan
 → execute tool/API call
 → verify
 → retry/fallback
 → notify/log
```

### Day 13: Guardrails

Revise:

- Input validation
- Output validation
- PII protection
- Prompt injection defense
- Tool permissioning
- Rate limits
- Human approval
- Policy checks
- Secure secrets handling


### Day 14: Mock Agent System Design

Practice:

```text
1. Build an AI agent that handles customer subscription changes.
2. Build a browser automation agent for internal operations.
3. Build a learning tutor agent with memory and quizzes.
```

## Week 3: Production LLMOps, Evaluation, Cloud, AI Coding Tools

Goal : Shift from “I can build demos” to “I can own production AI systems.”

### Day 15: LLM Observability

Revise:

- Traces
- Spans
- Prompt logs
- Tool call logs
- Latency
- Cost
- Token usage
- Failure rates
- User feedback

Tools:

```text
- LangSmith
- Langfuse
- MLflow
- Weights & Biases
- OpenTelemetry
```

---

### Day 16: Evaluation

Revise deeply.

Types of evals:

```text
1. Unit tests for deterministic code
2. Prompt regression tests
3. RAG retrieval tests
4. LLM answer quality tests
5. Agent task completion tests
6. Human review
7. Online A/B tests
```

Prepare example:

```text
I would create a golden dataset of representative queries, expected source documents, acceptable answer patterns, and refusal cases. Then I would run evals on every prompt/model/retriever change.
```

---

### Day 17: Cost, Latency, and Reliability

Revise:

- Caching
- Smaller models
- Model routing
- Batch calls
- Streaming
- Prompt compression
- Context pruning
- Timeouts
- Retry with backoff
- Fallback providers

Interview answer:

```text
For simple classification I would use a cheaper/faster model; for complex reasoning I would route to a stronger model. I would track cost per successful task, not just cost per token.
```

---

### Day 18: Cloud Deployment

Revise:

### Azure

- Azure OpenAI
- Azure AI Search
- App Service
- Functions
- Container Apps
- Key Vault
- Monitor

### GCP

- Vertex AI
- Cloud Run
- Cloud Functions
- Pub/Sub
- Secret Manager
- Cloud Logging

### Generic

- Docker
- CI/CD
- Env variables
- Secrets
- Autoscaling
- API gateway

---

### Day 19: AI Coding Tools + MCP

Focus on:

- Cursor
- Claude Code
- GitHub Copilot
- MCP servers
- Context injection
- Repo-aware coding
- Test generation
- Refactoring
- Documentation generation
- Secure usage standards

Prepare one good story:

```text
I would run an AI coding pilot by selecting a small engineering team, defining use cases like test generation, refactoring, documentation, and bug fixing, setting guardrails around secrets/security/code review, measuring productivity and defect rate, and publishing playbooks based on what works.
```


### Day 20: Engineering Playbooks

Prepare templates for:

- Prompt standards
- RAG implementation checklist
- Agent workflow checklist
- Tool-calling checklist
- Evaluation checklist
- AI coding assistant usage guide
- Security and governance standards

### Day 21: Revision

Mock questions:

```text
- How do you monitor LLM apps?
- How do you prevent prompt injection?
- How do you evaluate agents?
- How do you reduce LLM cost?
- How do you deploy a LangGraph app?
```

## Week 4: Portfolio, Interview Stories, System Design

Goal : Convert your knowledge into interview-ready proof.

### Day 22–24: Build or Polish One Portfolio Project

#### Best Project Option

```text
Production-Style Agentic RAG Workflow
```

Must include:

- Python FastAPI backend
- LangGraph orchestration
- RAG with vector DB
- Tool calling
- Memory/state
- Structured output
- Evals
- Logging/tracing
- Guardrails
- Docker
- README
- Architecture diagram

Example project:

```text
AI Operations Assistant

Capabilities:
- Answers internal policy questions using RAG
- Opens tickets through API tool
- Summarizes user issue
- Classifies urgency
- Routes to correct team
- Verifies ticket creation
- Logs trace
- Runs eval tests
```

This one project can support almost every job description.


### Day 25: Prepare STAR Stories

Create 6 interview stories:

```text
1. Built an LLM/RAG app
2. Debugged a production issue
3. Improved latency/cost
4. Improved answer quality
5. Designed evaluation framework
6. Used AI tools to accelerate engineering
```

Use this structure:

```text
Situation:
Task:
Action:
Result:
Metrics:
Tradeoffs:
What I would improve:
```

### Day 26: System Design Practice

Practice these:

```text
1. Design a customer-support AI agent.
2. Design a learning tutor with memory.
3. Design a retail GenAI assistant.
4. Design a multi-agent workflow for business automation.
5. Design an AI coding assistant pilot for an enterprise team.
6. Design a RAG system for compliance documents.
```

### Day 27: Framework Comparison Revision

| Framework       | Best For                                       | Interview Talking Point             |
|:----------------|:-----------------------------------------------|:------------------------------------|
| LangChain       | Chains, tools, retrievers                      | Broad ecosystem                     |
| LangGraph       | Stateful workflows                             | Best for controllable agents        |
| CrewAI          | Role-based multi-agent systems                 | Good for collaborative agents       |
| AutoGen         | Conversational multi-agent research/prototypes | Flexible agent conversations        |
| Semantic Kernel | Enterprise/Microsoft integration               | Good for plugin-based orchestration |
| Google ADK      | Google agent development ecosystem             | Useful for GCP/Vertex contexts      |


### Day 28: Final Mock Interview

Practice answering in 2–3 minutes:

```text
- Tell me about an LLM system you built.
- How do you design reliable agents?
- How do you debug bad RAG answers?
- How do you evaluate prompt changes?
- How do you handle tool-call failures?
- How do you reduce latency and cost?
- How do you use Cursor/Claude Code safely in enterprise?
- How would you design an MCP-based coding pilot?
```

Next: [Weekly Revision System](weekly-revision-system.md)

--8<-- "_abbreviations.md"

