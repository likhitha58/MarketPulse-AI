from app.config.groq_client import client
from app.utils.llm_helper import safe_generate


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

    state["final_recommendation"] = safe_generate(
        client,
        prompt
    )

    return state