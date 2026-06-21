from app.tools.yfinance_tool import get_company_info
from app.config.groq_client import client
from app.utils.llm_helper import safe_generate

def research_agent(ticker):

    company_data = get_company_info(ticker)

    prompt = f"""
    You are a professional equity research analyst.

    Analyze:

    Company Name: {company_data['name']}
    Sector: {company_data['sector']}
    Industry: {company_data['industry']}
    Market Cap: {company_data['market_cap']}

    Business Summary:
    {company_data['summary']}
    """

    report = safe_generate(
    client,
    prompt
    )

    return report