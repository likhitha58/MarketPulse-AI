from app.config.gemini import client


def committee_agent(state):

    prompt = f"""
You are the Head of an Investment Committee.

You have received:

BULL CASE:
{state['bull_case']}

BEAR CASE:
{state['bear_case']}

Risk Assessment:
{state["risk_report"]}
Evaluate the bull case, bear case, and risk assessment objectively.

Provide:

1. Strongest Bull Arguments
2. Strongest Bear Arguments
3. Final Recommendation

Recommendation must be:

BUY
HOLD
SELL

Explain your reasoning.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    state["final_recommendation"] = response.text

    return state