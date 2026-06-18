# app/test_decision_only.py

from agents.decision_agent import decision_agent

state = {
    "research_report": "test",
    "financial_report": "test",
    "news_report": "test",
    "final_recommendation": ""
}

print(decision_agent(state))