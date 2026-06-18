from config.gemini import client


def decision_agent(state):

    prompt = f"""
    You are a senior investment committee member.

    Review the following reports.

    RESEARCH REPORT:
    {state['research_report']}

    FINANCIAL REPORT:
    {state['financial_report']}

    Based on both reports:

    1. Summarize key positives
    2. Summarize key risks
    3. Give an investment recommendation

    Recommendation must be one of:

    BUY
    HOLD
    SELL

    Explain your reasoning clearly.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    state["final_recommendation"] = response.text

    return state