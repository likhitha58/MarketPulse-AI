from agents.risk_agent import risk_agent

state = {
    "research_report": "NVIDIA dominates AI chips.",
    "financial_report": "Revenue and profit growing rapidly.",
    "news_report": "Strong AI demand continues.",
    "risk_report": ""
}

result = risk_agent(state)

print(result["risk_report"])