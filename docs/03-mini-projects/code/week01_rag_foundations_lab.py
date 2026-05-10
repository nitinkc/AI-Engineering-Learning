from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
CORPUS_PATH = BASE_DIR / "week01_sample_corpus.json"


@dataclass
class Chunk:
    chunk_id: str
    source: str
    text: str


def load_corpus() -> list[dict]:
    return json.loads(CORPUS_PATH.read_text())


def estimate_tokens(text: str) -> int:
    return max(1, len(text.split()) * 4 // 3)


def chunk_text(source: str, text: str, chunk_size: int = 18) -> list[Chunk]:
    words = text.split()
    chunks = []
    for index in range(0, len(words), chunk_size):
        chunk_words = words[index:index + chunk_size]
        chunks.append(Chunk(
            chunk_id=f"{source}-{index // chunk_size}",
            source=source,
            text=" ".join(chunk_words),
        ))
    return chunks


def score(query: str, chunk: Chunk) -> int:
    query_terms = set(query.lower().replace("?", "").split())
    chunk_terms = set(chunk.text.lower().replace(".", "").split())
    return len(query_terms & chunk_terms)


def retrieve(query: str, chunks: list[Chunk], top_k: int = 3) -> list[Chunk]:
    ranked = sorted(chunks, key=lambda chunk: score(query, chunk), reverse=True)
    return [chunk for chunk in ranked if score(query, chunk) > 0][:top_k]


def build_prompt(system: str, user_question: str, context_chunks: list[Chunk]) -> str:
    context = "\n\n".join(
        f"Source {chunk.chunk_id}: {chunk.text}" for chunk in context_chunks
    )
    return (
        f"SYSTEM:\n{system}\n\n"
        f"CONTEXT:\n{context}\n\n"
        f"USER:\n{user_question}\n\n"
        "Return a grounded answer with citations. Refuse if the context is insufficient."
    )


def answer_question(question: str, chunks: list[Chunk]) -> dict:
    retrieved = retrieve(question, chunks)
    prompt = build_prompt(
        system="You answer only from approved internal knowledge.",
        user_question=question,
        context_chunks=retrieved,
    )
    citations = [chunk.chunk_id for chunk in retrieved]
    answer = " ".join(chunk.text for chunk in retrieved) or "Insufficient context to answer safely."
    return {
        "question": question,
        "prompt_tokens": estimate_tokens(prompt),
        "retrieved": [asdict(chunk) for chunk in retrieved],
        "answer": answer,
        "citations": citations,
    }


def summarize_long_document(text: str, chunk_size: int = 20) -> dict:
    chunk_summaries = []
    for chunk in chunk_text("longdoc", text, chunk_size=chunk_size):
        summary = ". ".join(sentence.strip() for sentence in chunk.text.split(".")[:2] if sentence.strip())
        chunk_summaries.append(summary)
    final_summary = ". ".join(chunk_summaries[:3])
    return {
        "chunk_summaries": chunk_summaries,
        "final_summary": final_summary,
    }


def main() -> None:
    corpus = load_corpus()
    chunks = []
    for document in corpus:
        chunks.extend(chunk_text(document["source"], document["text"]))

    result = answer_question("How do I reset an expired API key?", chunks)
    summary = summarize_long_document(corpus[-1]["text"])

    print("=== Retrieval Result ===")
    print(json.dumps(result, indent=2))
    print("\n=== Long Context Summary ===")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
