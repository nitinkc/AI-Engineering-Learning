"""CLI entry point for the RAG Foundations Lab.

Usage examples
--------------
  # Ask a question against the default corpus:
  04-python cli.py query "How do I reset an expired API key?"

  # Summarize a document passed via stdin:
  echo "Long document text here..." | 04-python cli.py summarize

  # Use a custom corpus file:
  04-python cli.py --corpus my_corpus.json query "What is the escalation policy?"
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from chunker import chunk_text
from grounding import answer_question
from summarizer import summarize_long_document

DEFAULT_CORPUS = Path(__file__).resolve().parent / "corpus.json"


def load_corpus(path: Path) -> list[dict]:
  return json.loads(path.read_text())


def build_index(corpus: list[dict]):
  chunks = []
  for document in corpus:
    chunks.extend(chunk_text(document["source"], document["text"]))
  return chunks


def cmd_query(args: argparse.Namespace) -> None:
  corpus = load_corpus(args.corpus)
  chunks = build_index(corpus)
  result = answer_question(args.question, chunks)
  print(json.dumps(result, indent=2))


def cmd_summarize(args: argparse.Namespace) -> None:
  text = sys.stdin.read() if args.text == "-" else args.text
  result = summarize_long_document(text, chunk_size=args.chunk_size)
  print(json.dumps(result, indent=2))


def build_parser() -> argparse.ArgumentParser:
  parser = argparse.ArgumentParser(
      description="RAG Foundations Lab — query and summarize internal documents.",
      formatter_class=argparse.RawDescriptionHelpFormatter,
  )
  parser.add_argument(
      "--corpus",
      type=Path,
      default=DEFAULT_CORPUS,
      metavar="PATH",
      help="Path to corpus JSON file (default: corpus.json)",
  )

  subparsers = parser.add_subparsers(dest="command", required=True)

  # query sub-command
  query_parser = subparsers.add_parser("query",
                                       help="Answer a question from the corpus.")
  query_parser.add_argument("question",
                            help="Natural-language question to answer.")
  query_parser.set_defaults(func=cmd_query)

  # summarize sub-command
  summarize_parser = subparsers.add_parser("summarize",
                                           help="Summarize a long document.")
  summarize_parser.add_argument(
      "text",
      nargs="?",
      default="-",
      help="Document text to summarize, or '-' to read from stdin (default).",
  )
  summarize_parser.add_argument(
      "--chunk-size",
      type=int,
      default=20,
      dest="chunk_size",
      help="Words per intermediate chunk (default: 20).",
  )
  summarize_parser.set_defaults(func=cmd_summarize)

  return parser


def main() -> None:
  parser = build_parser()
  args = parser.parse_args()
  args.func(args)


if __name__ == "__main__":
  main()
