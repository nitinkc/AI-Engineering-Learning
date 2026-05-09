"""Summarizer — map-reduce summarization for long documents."""
from __future__ import annotations

from chunker import chunk_text


def summarize_long_document(text: str, chunk_size: int = 20) -> dict:
    """Produce a hierarchical summary using map-reduce over chunks.

    Each chunk is summarized to its first two sentences, then the first
    three chunk summaries are joined into a final summary.

    Args:
        text: Raw document text (can be arbitrarily long).
        chunk_size: Words per intermediate chunk (default 20).

    Returns:
        Dict with keys: chunk_summaries (list[str]), final_summary (str).
    """
    chunk_summaries: list[str] = []
    for chunk in chunk_text("longdoc", text, chunk_size=chunk_size):
        summary = ". ".join(
            sentence.strip()
            for sentence in chunk.text.split(".")[:2]
            if sentence.strip()
        )
        chunk_summaries.append(summary)

    final_summary = ". ".join(chunk_summaries[:3])
    return {
        "chunk_summaries": chunk_summaries,
        "final_summary": final_summary,
    }
