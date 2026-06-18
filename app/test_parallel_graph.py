from graph.workflow import graph

initial_state = {

    "ticker": "NVDA",

    "company_name": "NVIDIA",

    "research_report": "NVIDIA dominates AI chips.",

    "financial_report": "Revenue and profit growing rapidly.",

    "news_report": "Strong AI demand continues.",

    "bull_case": "",

    "bear_case": "",

    "final_recommendation": ""
}

result = graph.invoke(initial_state)

print(result["final_recommendation"])