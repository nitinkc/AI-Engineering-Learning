# RAG Debugging and Quality

## Pipeline-First Debugging

Treat RAG failures as staged system issues.

```mermaid
flowchart TD
  A[Bad answer] --> B{Source has answer?}
  B -- No --> C[Fix ingestion and coverage]
  B -- Yes --> D{Relevant chunk retrieved?}
  D -- No --> E[Fix chunking, filters, hybrid search]
  D -- Yes --> F{Prompt grounded on context?}
  F -- No --> G[Fix prompt and context ordering]
  F -- Yes --> H[Add validators, citations, refusal]
```

## Core Metrics

- Retrieval hit rate
- Context precision
- Faithfulness
- Citation accuracy
- P95 latency
- Cost per successful task

## Micro-Lab

- Pick 5 failed user questions.
- Label each root cause: `coverage`, `retrieval`, `prompt`, `validation`.
- Propose one measurable fix per failure.

--8<-- "_abbreviations.md"

