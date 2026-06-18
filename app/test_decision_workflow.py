from agents.research_agent import research_agent
from agents.financial_agent import financial_agent
from agents.decision_agent import decision_agent

state = {
    "ticker": "NVDA",
    "company_name": "NVIDIA",
    "research_report": "",
    "financial_report": "",
    "final_recommendation": ""
}

print("Running Research Agent...")
state["research_report"] = research_agent("NVDA")

print("Running Financial Agent...")
state["financial_report"] = financial_agent("NVDA")

print("Running Decision Agent...")
state = decision_agent(state)

print("\n")
print("=" * 50)
print("FINAL INVESTMENT COMMITTEE REPORT")
print("=" * 50)

print(state["final_recommendation"])