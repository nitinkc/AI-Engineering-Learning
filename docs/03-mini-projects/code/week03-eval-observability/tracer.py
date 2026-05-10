"""Tracer — structured trace collection and span logging."""
from __future__ import annotations

import time
from contextlib import contextmanager
from dataclasses import dataclass, field, asdict
from typing import Generator


@dataclass
class Span:
  name: str
  start_ms: float
  end_ms: float = 0.0
  metadata: dict = field(default_factory=dict)
  status: str = "ok"

  @property
  def duration_ms(self) -> float:
    return round(self.end_ms - self.start_ms, 2)


@dataclass
class Trace:
  trace_id: str
  spans: list[Span] = field(default_factory=list)

  def add_span(self, span: Span) -> None:
    self.spans.append(span)

  def to_dict(self) -> dict:
    return {
      "trace_id": self.trace_id,
      "spans": [
        {**asdict(s), "duration_ms": s.duration_ms}
        for s in self.spans
      ],
      "total_ms": round(
          sum(s.duration_ms for s in self.spans), 2
      ),
    }


@contextmanager
def timed_span(
    trace: Trace, name: str, metadata: dict | None = None
) -> Generator[Span, None, None]:
  """Context manager that records start/end time for a named span.

  Usage::

      with timed_span(trace, "retrieval", {"top_k": 3}) as span:
          results = retrieve(query, chunks)
          span.metadata["hits"] = len(results)
  """
  span = Span(
      name=name,
      start_ms=time.monotonic() * 1000,
      metadata=metadata or {},
  )
  try:
    yield span
    span.status = "ok"
  except Exception as exc:
    span.status = f"error: {exc}"
    raise
  finally:
    span.end_ms = time.monotonic() * 1000
    trace.add_span(span)
