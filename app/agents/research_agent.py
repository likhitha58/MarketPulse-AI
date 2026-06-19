from app.tools.yfinance_tool import get_company_info
from app.config.gemini import client


def research_agent(ticker):

    company_data = get_company_info(ticker)

    prompt = f"""
    You are a professional equity research analyst.

    Analyze the following company:

    Company Name: {company_data['name']}
    Sector: {company_data['sector']}
    Industry: {company_data['industry']}
    Market Cap: {company_data['market_cap']}

    Business Summary:
    {company_data['summary']}

    Create a research report with:

    1. Company Overview
    2. Industry Position
    3. Key Strengths
    4. Potential Concerns
    5. Competitor Discussion

    Keep the report professional.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text