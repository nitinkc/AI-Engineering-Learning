"""Retriever — keyword overlap scorer and top-k selector."""
from __future__ import annotations

from chunker import Chunk


def score(query: str, chunk: Chunk) -> int:
    """Count token overlap between *query* and *chunk* text."""
    query_terms = set(query.lower().replace("?", "").split())
    chunk_terms = set(chunk.text.lower().replace(".", "").split())
    return len(query_terms & chunk_terms)


def retrieve(query: str, chunks: list[Chunk], top_k: int = 3) -> list[Chunk]:
    """Return up to *top_k* chunks with non-zero query overlap, ranked by score.

    Args:
        query: Natural-language question from the user.
        chunks: Flat list of all indexed chunks.
        top_k: Maximum number of chunks to return.

    Returns:
        Ranked list of matching :class:`Chunk` objects (may be fewer than top_k).
    """
    ranked = sorted(chunks, key=lambda c: score(query, c), reverse=True)
    return [c for c in ranked if score(query, c) > 0][:top_k]
