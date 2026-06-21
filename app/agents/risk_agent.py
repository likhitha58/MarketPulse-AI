from app.config.groq_client import client
from app.utils.llm_helper import safe_generate


def risk_agent(state):

    prompt = f"""
You are a hedge fund risk analyst.

Research:
{state["research_report"]}

Financial:
{state["financial_report"]}

News:
{state["news_report"]}

Rules:
- Maximum 80 words

Return:

Risk Score: X/10

Key Risks:
- point
- point
- point
"""

    state["risk_report"] = safe_generate(
        client,
        prompt
    )

    return state