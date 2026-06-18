from config.gemini import client


def bear_agent(state):

    prompt = f"""
You are a highly skeptical Wall Street Bear Analyst.

Your job is to build the strongest possible argument AGAINST investing.

Research Report:
{state['research_report']}

Financial Report:
{state['financial_report']}

News Report:
{state['news_report']}

Create:

1. Investment Risks
2. Competitive Threats
3. Financial Concerns
4. Reasons This Stock Can Underperform

Be persuasive and bearish.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    state["bear_case"] = response.text

    return state