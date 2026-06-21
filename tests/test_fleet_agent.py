from observability.fleet_agent import (
    CampaignInput,
    cost_monitor_sub_agent,
    fleet_meta_ads_agent,
    quality_monitor_sub_agent,
)


def test_fleet_agent_returns_nested_monitoring_decision() -> None:
    output = fleet_meta_ads_agent(
        {
            "spend": 100,
            "leads": 5,
            "clicks": 80,
            "impressions": 4000,
        }
    )

    assert output["agent"] == "fleet_meta_ads_agent"
    assert output["decision"] == "keep_running"
    assert output["safety"]["read_only"] is True
    assert output["cost_analysis"]["cpl"] == 20.0
    assert output["quality_analysis"]["ctr"] == 2.0


def test_cost_sub_agent_flags_high_cpl() -> None:
    output = cost_monitor_sub_agent(
        campaign=CampaignInput(spend=200.0, leads=4, clicks=50, impressions=3000)
    )

    assert output["status"] == "high_cpl"
    assert output["cpl"] == 50.0


def test_quality_sub_agent_flags_low_ctr() -> None:
    output = quality_monitor_sub_agent(
        campaign=CampaignInput(spend=100.0, leads=1, clicks=5, impressions=2000)
    )

    assert output["status"] == "low_ctr"
    assert output["ctr"] == 0.25
