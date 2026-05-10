"""Grounding — prompt construction and citation-grounded answering."""
from __future__ import annotations

from dataclasses import asdict

from chunker import Chunk, estimate_tokens
from retriever import retrieve


def build_prompt(system: str, user_question: str,
    context_chunks: list[Chunk]) -> str:
  """Assemble a grounded prompt with context and citation instruction."""
  context = "\n\n".join(
      f"Source {chunk.chunk_id}: {chunk.text}" for chunk in context_chunks
  )
  return (
    f"SYSTEM:\n{system}\n\n"
    f"CONTEXT:\n{context}\n\n"
    f"USER:\n{user_question}\n\n"
    "Return a grounded answer with citations. "
    "Refuse if the context is insufficient."
  )


def answer_question(question: str, chunks: list[Chunk]) -> dict:
  """Retrieve relevant chunks and produce a citation-grounded answer dict.

  Returns a dict with keys: question, prompt_tokens, retrieved, answer, citations.
  """
  retrieved = retrieve(question, chunks)
  prompt = build_prompt(
      system="You answer only from approved internal knowledge.",
      user_question=question,
      context_chunks=retrieved,
  )
  citations = [chunk.chunk_id for chunk in retrieved]
  answer = (
      " ".join(chunk.text for chunk in retrieved)
      or "Insufficient context to answer safely."
  )
  return {
    "question": question,
    "prompt_tokens": estimate_tokens(prompt),
    "retrieved": [asdict(chunk) for chunk in retrieved],
    "answer": answer,
    "citations": citations,
  }
