from app.config.gemini import client


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

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    state["risk_report"] = response.text

    return state