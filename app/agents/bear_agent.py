from app.config.groq_client import client
from app.utils.llm_helper import safe_generate


def bear_agent(state):

    prompt = f"""
You are a bearish equity analyst.

Based on:

Research Report:
{state["research_report"]}

Financial Report:
{state["financial_report"]}

News Report:
{state["news_report"]}

Create the strongest bear case.

Rules:
- Maximum 5 bullet points
- Each bullet under 20 words
- No introduction
- No conclusion
- Be concise
"""

    state["bear_case"] = safe_generate(
        client,
        prompt
    )

    return state