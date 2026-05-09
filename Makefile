.PHONY: mini-tests

mini-tests:
	python3 -m pytest docs/08-mini-projects/code/week01-rag-foundations/tests/ docs/08-mini-projects/code/week02-agent-reliability/tests/ docs/08-mini-projects/code/week03-eval-observability/tests/ -v
