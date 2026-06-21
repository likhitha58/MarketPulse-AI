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

Rules:
- Maximum 100 words
- Professional tone
- No fluff

Return EXACTLY:

Recommendation: BUY/HOLD/SELL

Confidence Score: XX%

Investment Thesis:
2 sentences

Top Reasons:
- point
- point
- point
"""

    state["final_recommendation"] = safe_generate(
        client,
        prompt
    )

    return state