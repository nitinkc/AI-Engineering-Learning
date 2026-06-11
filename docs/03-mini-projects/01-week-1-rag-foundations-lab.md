# Week 1 Mini Project - RAG Foundations Lab

Pre-reading: [Foundations Overview](../01-foundations/index.md) · [01 RAG Debugging and Quality](../01-foundations/01-rag-debugging-quality.md)

This mini project gives Week 1 a runnable baseline. It uses only the Python standard library so you
can focus on the pipeline shape: source data, chunking, retrieval, grounded answers, token
budgeting, and long-context summarization.

Run the commands below from an activated project venv.

## What You Will Build

| Capability          | Output                    |
|---------------------|---------------------------|
| Prompt builder      | Context-aware prompt text |
| Chunker             | Document slices with IDs  |
| Retriever           | Ranked chunks for a query |
| Grounded answerer   | Answer plus citations     |
| Long-doc summarizer | Map-reduce style summary  |

## How to Run

```bash
cd docs/03-mini-projects/code/week01-rag-foundations

# Ask a question
04-python cli.py query "How do I reset an expired API key?"

# Summarize long text from stdin
echo "Long document text here." | 04-python cli.py summarize

# Run tests
04-python -m pytest tests/ -v
```

## Portfolio Structure

```text
code/week01-rag-foundations/
├── chunker.py
├── retriever.py
├── grounding.py
├── summarizer.py
├── cli.py
├── corpus.json
└── tests/test_rag.py
```

## What to Modify Across the Week

| Day   | Suggested change                                       |
|-------|--------------------------------------------------------|
| Day 1 | Change the system prompt and inspect token estimates.  |
| Day 2 | Add stronger refusal and output constraints.           |
| Day 3 | Change chunk size and compare retrieval ranking.       |
| Day 4 | Change citation formatting and context ordering.       |
| Day 5 | Log one failure and classify the root cause.           |
| Day 6 | Replace the long document text and compare summaries.  |
| Day 7 | Create a one-page debugging checklist from your notes. |

## Starter Assets

| Asset                                                                                     | Purpose                                                        |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| [week01-rag-foundations/cli.py](code/week01-rag-foundations/cli.py)                       | CLI entry point for query and summarize flows                  |
| [week01-rag-foundations/chunker.py](code/week01-rag-foundations/chunker.py)               | Chunking and token estimation utilities                        |
| [week01-rag-foundations/retriever.py](code/week01-rag-foundations/retriever.py)           | Ranking and top-k retrieval logic                              |
| [week01-rag-foundations/grounding.py](code/week01-rag-foundations/grounding.py)           | Grounded prompt and citation answer pipeline                   |
| [week01-rag-foundations/summarizer.py](code/week01-rag-foundations/summarizer.py)         | Long-context map-reduce summarizer                             |
| [week01-rag-foundations/corpus.json](code/week01-rag-foundations/corpus.json)             | Tiny document set for retrieval                                |
| [week01-rag-foundations/tests/test_rag.py](code/week01-rag-foundations/tests/test_rag.py) | Unit test suite for RAG building blocks                        |
| [week01_rag_foundations_output.txt](output/week01_rag_foundations_output.txt)             | Sample retrieval and long-context output from a successful run |

## Matching Lab Outputs

| Output                     | Why keep it                                     |
|----------------------------|-------------------------------------------------|
| Retrieval ranking snapshot | Helps explain why an answer failed or succeeded |
| Token estimate summary     | Connects design decisions to cost and latency   |
| Failure record             | Becomes a regression test seed                  |
| Long-doc summary           | Shows handling of context compression           |

## Portfolio Checklist

| Item                                                     | Done? |
|----------------------------------------------------------|-------|
| Save one retrieval result with chunk IDs and citations.  | [ ]   |
| Save one failed query case and root-cause notes.         | [ ]   |
| Capture one chunk-size comparison and trade-off summary. | [ ]   |
| Write one STAR-ready bullet using this project evidence. | [ ]   |

--8<-- "_abbreviations.md"
