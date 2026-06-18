from agents.bear_agent import bear_agent

state = {
    "research_report": "NVIDIA dominates AI chips.",
    "financial_report": "Revenue and profit growing rapidly.",
    "news_report": "Strong AI demand continues.",
    "bear_case": ""
}

result = bear_agent(state)

print(result["bear_case"])