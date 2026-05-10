# Week 01 — RAG Foundations Lab

A self-contained Python project demonstrating **Retrieval-Augmented Generation** fundamentals:
chunking, keyword retrieval, citation grounding, and long-document summarization.

## Project Structure

```
week01-rag-foundations/
├── __init__.py
├── chunker.py       # Fixed-size word chunker + token estimator
├── retriever.py     # Keyword overlap scorer and top-k selector
├── grounding.py     # Prompt assembly and citation-grounded answering
├── summarizer.py    # Map-reduce summarization for long documents
├── cli.py           # Argparse CLI (query / summarize sub-commands)
├── corpus.json      # Sample internal knowledge base
├── requirements.txt
└── tests/
    └── test_rag.py  # 20+ unit tests (pytest)
```

## Quick Start

```bash
# From this directory — no install needed

# Ask a question
python cli.py query "How do I reset an expired API key?"

# Summarize via stdin
echo "Long document text here..." | python cli.py summarize

# Custom corpus
python cli.py --corpus my_data.json query "What is the escalation policy?"
```

## Running Tests

```bash
python -m pytest tests/ -v
```

## Key Concepts Covered

| Concept       | Module          | Description                                 |
|---------------|-----------------|---------------------------------------------|
| Chunking      | `chunker.py`    | Splits docs into fixed-size word chunks     |
| Retrieval     | `retriever.py`  | Keyword overlap scoring, top-k selection    |
| Grounding     | `grounding.py`  | Citation-anchored prompt construction       |
| Summarization | `summarizer.py` | Map-reduce over chunk summaries             |
| CLI           | `cli.py`        | Argparse sub-commands: `query`, `summarize` |

## Requirements

- Python 3.9+
- No external dependencies (stdlib only)
