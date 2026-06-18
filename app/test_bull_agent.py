from agents.bull_agent import bull_agent

state = {
    "research_report": "NVIDIA dominates AI chips.",
    "financial_report": "Revenue and profit growing rapidly.",
    "news_report": "Strong AI demand continues.",
    "bull_case": ""
}

result = bull_agent(state)

print(result["bull_case"])