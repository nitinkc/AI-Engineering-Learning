# Evals, Observability, and Production

## Production Gate

A change should ship only when eval thresholds pass.

| Layer | Example Metrics |
|---|---|
| Retrieval | hit rate, MRR |
| Generation | faithfulness, relevance, citation accuracy |
| Agent | task success rate, retry rate |
| Ops | P95 latency, error rate, cost per task |

## Observability Minimum

- Prompt and model version logs
- Retrieved context logs
- Tool call input/output logs
- Trace IDs across requests
- Alerting for latency and cost spikes

## Deployment Readiness

- Secrets manager for credentials
- Retry and timeout defaults
- Fallback behavior defined
- CI checks and rollback steps documented

## Micro-Lab

- Build a 10-question golden set.
- Define 3 pass thresholds.
- Compare baseline vs changed pipeline.
- Write a deploy/no-deploy decision.

--8<-- "_abbreviations.md"

