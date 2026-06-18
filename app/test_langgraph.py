from graph.workflow import graph

initial_state = {
    "ticker": "NVDA",
    "company_name": "NVIDIA",
    "research_report": "",
    "financial_report": "",
    "final_recommendation": "",
    "news_report": ""
}

result = graph.invoke(initial_state)

print("\n")
print("=" * 50)
print("FINAL RESULT")
print("=" * 50)

print(result["final_recommendation"])