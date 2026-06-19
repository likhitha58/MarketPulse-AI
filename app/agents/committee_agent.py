from app.config.gemini import client


def committee_agent(state):

    prompt = f"""
You are Head of the Investment Committee.

Bull Case:
{state["bull_case"]}

Bear Case:
{state["bear_case"]}

Risk Assessment:
{state["risk_report"]}

Provide:

Recommendation: BUY/HOLD/SELL

Confidence Score: XX%

Summary:
Maximum 3 sentences.

Why:
- Point 1
- Point 2
- Point 3

Keep total response under 150 words.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    state["final_recommendation"] = response.text

    return state