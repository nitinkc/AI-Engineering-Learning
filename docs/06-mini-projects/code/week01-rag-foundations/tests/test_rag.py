"""Tests for the RAG Foundations Lab."""
from __future__ import annotations

import sys
from pathlib import Path

# Allow importing sibling modules directly (no package install needed)
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from chunker import Chunk, chunk_text, estimate_tokens
from grounding import answer_question, build_prompt
from retriever import retrieve, score
from summarizer import summarize_long_document


# ---------------------------------------------------------------------------
# chunker
# ---------------------------------------------------------------------------

class TestChunkText:
    def test_basic_split(self):
        chunks = chunk_text("doc", "a b c d e f", chunk_size=3)
        assert len(chunks) == 2
        assert chunks[0].text == "a b c"
        assert chunks[1].text == "d e f"

    def test_chunk_ids(self):
        chunks = chunk_text("src", "w1 w2 w3 w4", chunk_size=2)
        assert chunks[0].chunk_id == "src-0"
        assert chunks[1].chunk_id == "src-1"

    def test_partial_last_chunk(self):
        chunks = chunk_text("doc", "a b c d e", chunk_size=3)
        assert len(chunks) == 2
        assert chunks[-1].text == "d e"

    def test_empty_text_returns_empty(self):
        chunks = chunk_text("doc", "", chunk_size=5)
        assert chunks == []


class TestEstimateTokens:
    def test_positive(self):
        assert estimate_tokens("hello world") == 2

    def test_single_word(self):
        assert estimate_tokens("hello") >= 1

    def test_never_zero(self):
        assert estimate_tokens("") >= 1


# ---------------------------------------------------------------------------
# retriever
# ---------------------------------------------------------------------------

class TestScore:
    def _make_chunk(self, text: str) -> Chunk:
        return Chunk(chunk_id="c0", source="s", text=text)

    def test_overlap(self):
        chunk = self._make_chunk("reset expired api key")
        assert score("reset api", chunk) == 2

    def test_no_overlap(self):
        chunk = self._make_chunk("completely unrelated content")
        assert score("reset api", chunk) == 0

    def test_case_insensitive(self):
        chunk = self._make_chunk("RESET API KEY")
        assert score("reset api", chunk) > 0


class TestRetrieve:
    def _make_chunks(self) -> list[Chunk]:
        return [
            Chunk(chunk_id="a-0", source="a", text="reset expired api key security"),
            Chunk(chunk_id="b-0", source="b", text="unrelated topic about cats"),
            Chunk(chunk_id="c-0", source="c", text="api key rotation policy"),
        ]

    def test_returns_relevant_only(self):
        results = retrieve("reset api key", self._make_chunks())
        ids = [c.chunk_id for c in results]
        assert "b-0" not in ids

    def test_top_k_limit(self):
        results = retrieve("api key", self._make_chunks(), top_k=1)
        assert len(results) <= 1

    def test_empty_query_no_crash(self):
        results = retrieve("", self._make_chunks())
        assert isinstance(results, list)


# ---------------------------------------------------------------------------
# grounding
# ---------------------------------------------------------------------------

class TestBuildPrompt:
    def test_contains_system(self):
        chunk = Chunk(chunk_id="x-0", source="x", text="some context")
        prompt = build_prompt("SYSTEM_MSG", "user question?", [chunk])
        assert "SYSTEM_MSG" in prompt

    def test_contains_user_question(self):
        chunk = Chunk(chunk_id="x-0", source="x", text="some context")
        prompt = build_prompt("sys", "my question?", [chunk])
        assert "my question?" in prompt

    def test_contains_chunk_id(self):
        chunk = Chunk(chunk_id="doc-1", source="doc", text="relevant text")
        prompt = build_prompt("sys", "q?", [chunk])
        assert "doc-1" in prompt


class TestAnswerQuestion:
    def _make_chunks(self) -> list[Chunk]:
        return [
            Chunk(chunk_id="a-0", source="a", text="reset expired api key using the portal"),
            Chunk(chunk_id="b-0", source="b", text="escalate high risk requests for review"),
        ]

    def test_returns_dict_keys(self):
        result = answer_question("reset api key?", self._make_chunks())
        assert {"question", "prompt_tokens", "retrieved", "answer", "citations"}.issubset(result)

    def test_no_match_safe_fallback(self):
        result = answer_question("xyzzy unknown query", self._make_chunks())
        assert "Insufficient" in result["answer"]

    def test_citations_match_retrieved(self):
        result = answer_question("reset api key?", self._make_chunks())
        assert result["citations"] == [c["chunk_id"] for c in result["retrieved"]]


# ---------------------------------------------------------------------------
# summarizer
# ---------------------------------------------------------------------------

class TestSummarizeLongDocument:
    def test_returns_keys(self):
        result = summarize_long_document("This is a sentence. Another sentence here.", chunk_size=5)
        assert "chunk_summaries" in result
        assert "final_summary" in result

    def test_final_summary_nonempty(self):
        text = " ".join(f"word{i}" for i in range(100))
        result = summarize_long_document(text)
        assert result["final_summary"]

    def test_chunk_count(self):
        text = " ".join(["word"] * 20)
        result = summarize_long_document(text, chunk_size=10)
        assert len(result["chunk_summaries"]) == 2
