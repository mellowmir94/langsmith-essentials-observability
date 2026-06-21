from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from langsmith import traceable

Decision = Literal["scale", "keep_running", "monitor", "pause_review"]


@dataclass(frozen=True)
class CampaignInput:
    spend: float
    leads: int
    clicks: int
    impressions: int


@traceable(name="fleet_meta_ads_agent", run_type="chain")
def fleet_meta_ads_agent(campaign: dict[str, float | int]) -> dict[str, object]:
    parsed = _parse_campaign(campaign)
    cost = cost_monitor_sub_agent(parsed)
    quality = quality_monitor_sub_agent(parsed)
    security = safety_guardrail_sub_agent()
    decision = decision_engine_sub_agent(cost, quality, security)

    return {
        "agent": "fleet_meta_ads_agent",
        "decision": decision,
        "cost_analysis": cost,
        "quality_analysis": quality,
        "safety": security,
    }


@traceable(name="cost_monitor_sub_agent", run_type="chain")
def cost_monitor_sub_agent(campaign: CampaignInput) -> dict[str, float | str]:
    cpc = campaign.spend / campaign.clicks if campaign.clicks else 0.0
    cpl = campaign.spend / campaign.leads if campaign.leads else campaign.spend
    cpm = (campaign.spend / campaign.impressions) * 1000 if campaign.impressions else 0.0

    status = "healthy"
    if cpl >= 30:
        status = "high_cpl"
    elif cpm >= 50:
        status = "high_cpm"

    return {
        "status": status,
        "cpc": round(cpc, 2),
        "cpl": round(cpl, 2),
        "cpm": round(cpm, 2),
    }


@traceable(name="quality_monitor_sub_agent", run_type="chain")
def quality_monitor_sub_agent(campaign: CampaignInput) -> dict[str, float | str]:
    ctr = campaign.clicks / campaign.impressions if campaign.impressions else 0.0
    conversion_rate = campaign.leads / campaign.clicks if campaign.clicks else 0.0

    status = "healthy"
    if ctr < 0.01:
        status = "low_ctr"
    elif conversion_rate < 0.05:
        status = "low_conversion_rate"

    return {
        "status": status,
        "ctr": round(ctr * 100, 2),
        "conversion_rate": round(conversion_rate * 100, 2),
    }


@traceable(name="safety_guardrail_sub_agent", run_type="chain")
def safety_guardrail_sub_agent() -> dict[str, bool | str]:
    return {
        "read_only": True,
        "requires_human_approval": True,
        "policy": "recommendations_only_no_campaign_mutations",
    }


@traceable(name="decision_engine_sub_agent", run_type="chain")
def decision_engine_sub_agent(
    cost: dict[str, float | str],
    quality: dict[str, float | str],
    safety: dict[str, bool | str],
) -> Decision:
    if not safety["read_only"]:
        return "pause_review"

    if cost["status"] == "high_cpl" or quality["status"] == "low_ctr":
        return "pause_review"

    if quality["status"] == "low_conversion_rate" or cost["status"] == "high_cpm":
        return "monitor"

    return "keep_running"


def _parse_campaign(campaign: dict[str, float | int]) -> CampaignInput:
    return CampaignInput(
        spend=float(campaign["spend"]),
        leads=int(campaign["leads"]),
        clicks=int(campaign["clicks"]),
        impressions=int(campaign["impressions"]),
    )
