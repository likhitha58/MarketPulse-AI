from config.gemini import client


def risk_agent(state):

    prompt = f"""
You are a professional Risk Analyst at a hedge fund.

Analyze the company using:

Research Report:
{state['research_report']}

Financial Report:
{state['financial_report']}

News Report:
{state['news_report']}

Provide:

1. Financial Risk
2. Competitive Risk
3. Market Risk
4. Valuation Risk
5. Geopolitical Risk
6. Overall Risk Score (1-10)
7. Risk Summary

Be objective and focus only on risk.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    state["risk_report"] = response.text

    return state