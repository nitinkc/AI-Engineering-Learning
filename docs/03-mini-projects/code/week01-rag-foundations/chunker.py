"""Chunker — splits documents into fixed-size word chunks."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Chunk:
    chunk_id: str
    source: str
    text: str


def chunk_text(source: str, text: str, chunk_size: int = 18) -> list[Chunk]:
    """Split *text* into non-overlapping word chunks of *chunk_size* words.

    Args:
        source: Identifier for the originating document.
        text: Raw document text to split.
        chunk_size: Maximum words per chunk (default 18).

    Returns:
        Ordered list of :class:`Chunk` objects.
    """
    words = text.split()
    chunks: list[Chunk] = []
    for index in range(0, len(words), chunk_size):
        chunk_words = words[index : index + chunk_size]
        chunks.append(
            Chunk(
                chunk_id=f"{source}-{index // chunk_size}",
                source=source,
                text=" ".join(chunk_words),
            )
        )
    return chunks


def estimate_tokens(text: str) -> int:
    """Rough token estimate: word_count × 4/3."""
    return max(1, len(text.split()) * 4 // 3)
