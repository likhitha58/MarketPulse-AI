from app.config.gemini import client


def bull_agent(state):

    prompt = f"""
You are a bullish equity analyst.

Based on:

Research Report:
{state["research_report"]}

Financial Report:
{state["financial_report"]}

News Report:
{state["news_report"]}

Create the strongest bull case.

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

    state["bull_case"] = response.text

    return state