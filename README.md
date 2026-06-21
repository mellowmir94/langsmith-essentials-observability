# LangSmith Essentials Observability

LangSmith observability and evaluation project for tracing, debugging, datasets, experiments, feedback, and production monitoring of AI agents.

This repo is aligned to **Quickstart: LangSmith Essentials** and demonstrates the practical pieces teams need before running AI agents in production.

## What It Covers

- Tracing agent runs
- Debugging failed or low-quality outputs
- Creating evaluation datasets
- Running experiments
- Capturing feedback
- Producing monitoring summaries
- CI checks for quality gates

## Architecture

```text
User Input
  -> Demo Agent
  -> LangSmith Trace
  -> Dataset Examples
  -> Experiment Evaluators
  -> Feedback Records
  -> Monitoring Summary
```

The demo agent is deterministic and API-free. LangSmith sync/experiment scripts require a LangSmith API key in local `.env`.

## Setup

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Add your LangSmith key only to local `.env`.

## Run Local Demo

```bash
python -m observability.cli
```

## Run Checks

```bash
python -m ruff check .
python -m pytest
python -m observability.monitoring
```

## Optional LangSmith Commands

```bash
python -m observability.sync_dataset
python -m observability.run_experiment
```

## Course Docs

- [Module 1 - Tracing](docs/module-1-tracing.md)
- [Module 2 - Datasets](docs/module-2-datasets.md)
- [Module 3 - Experiments](docs/module-3-experiments.md)
- [Module 4 - Feedback](docs/module-4-feedback.md)
- [Module 5 - Monitoring](docs/module-5-monitoring.md)
- [Capstone](docs/capstone.md)
