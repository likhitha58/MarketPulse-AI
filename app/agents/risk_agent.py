from app.config.groq_client import client
from app.utils.llm_helper import safe_generate


def risk_agent(state):

    prompt = f"""
You are a hedge fund risk analyst.

Analyze:

Research Report:
{state["research_report"]}

Financial Report:
{state["financial_report"]}

News Report:
{state["news_report"]}

Return:

Risk Score: X/10

Key Risks:
- Risk 1
- Risk 2
- Risk 3

Maximum 100 words.
"""

    state["risk_report"] = safe_generate(
        client,
        prompt
    )

    return state