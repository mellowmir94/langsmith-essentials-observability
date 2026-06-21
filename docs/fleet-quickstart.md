# Quickstart: LangSmith Fleet

This module is represented as a practical Fleet-style agent playbook plus a traced Python workflow.

## Lesson Coverage

| Lesson | Portfolio Artifact |
| --- | --- |
| Building An Agent | `fleet_meta_ads_agent` orchestrates campaign monitoring. |
| Human-In-The-Loop | Safety guardrail requires human approval before any campaign action. |
| What Can Agents Do? | Agent classifies performance, computes metrics, and recommends an action. |
| Skills | Cost, quality, safety, and decision logic are separated as callable capabilities. |
| MCP | Documented as the integration layer for external tools. This repo does not require a live MCP server. |
| Ambient Agents | Agent can be scheduled later for recurring campaign monitoring. |
| Sub-Agents | Cost, quality, safety, and decision sub-agents are traced as child runs. |
| Computer Use / Sandboxes | Documented as optional UI/browser automation; not required for this read-only monitoring agent. |
| Templates | This project acts as a reusable template for monitored business agents. |

## Architecture

```text
Fleet Meta Ads Agent
  -> Cost Monitor Sub-Agent
  -> Quality Monitor Sub-Agent
  -> Safety Guardrail Sub-Agent
  -> Decision Engine Sub-Agent
  -> Recommendation
```

## Why This Exists

Fleet is about operating agents, not only writing prompts. For a portfolio, the important signal is that the agent is observable, decomposed into smaller responsibilities, and safe by default.

This implementation keeps the agent read-only:

- no campaign edits
- no budget changes
- no automatic pausing
- human approval required before any real-world action

## Run The Fleet Demo

```powershell
python -m observability.run_fleet_agent
```

Expected LangSmith behavior:

- parent trace: `fleet_meta_ads_agent`
- child traces:
  - `cost_monitor_sub_agent`
  - `quality_monitor_sub_agent`
  - `safety_guardrail_sub_agent`
  - `decision_engine_sub_agent`

## Commit Message

```text
feat: add langsmith fleet agent workflow
```
