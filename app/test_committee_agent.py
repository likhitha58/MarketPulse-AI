from agents.committee_agent import committee_agent

state = {

    "bull_case": """
NVIDIA dominates AI chips.
Strong revenue growth.
Huge future demand.
""",

    "bear_case": """
Stock is overvalued.
Competition increasing.
China restrictions risk.
""",

    "final_recommendation": ""
}

result = committee_agent(state)

print(result["final_recommendation"])