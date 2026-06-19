from app.config.gemini import client


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

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    state["bear_case"] = response.text

    return state