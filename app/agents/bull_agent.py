from app.config.groq_client import client
from app.utils.llm_helper import safe_generate


def bull_agent(state):

    prompt = f"""
You are a bullish equity analyst.

Research:
{state["research_report"]}

Financial:
{state["financial_report"]}

News:
{state["news_report"]}

Rules:
- Maximum 5 bullets
- Each bullet under 15 words
- No introduction
- No conclusion

Return only bullets.
"""

    state["bull_case"] = safe_generate(
        client,
        prompt
    )

    return state