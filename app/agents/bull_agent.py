from app.config.gemini import client


def bull_agent(state):

    prompt = f"""
You are a highly optimistic Wall Street Bull Analyst.

Your job is to build the strongest possible investment case.

Research Report:
{state['research_report']}

Financial Report:
{state['financial_report']}

News Report:
{state['news_report']}

Create:

1. Investment Thesis
2. Growth Drivers
3. Competitive Advantages
4. Reasons This Stock Can Outperform

Be persuasive and bullish.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    state["bull_case"] = response.text

    return state