from tools.financial_tool import get_financial_data
from config.gemini import client


def financial_agent(ticker):

    financial_data = get_financial_data(ticker)

    prompt = f"""
    You are a senior equity research analyst.

    Analyze the following financial information.

    Financial Data:

    Revenue: {financial_data.get('revenue')}
    Net Income: {financial_data.get('net_income')}
    Cash: {financial_data.get('cash')}
    Debt: {financial_data.get('debt')}
    Operating Cash Flow: {financial_data.get('operating_cash_flow')}
    P/E Ratio: {financial_data.get('pe_ratio')}
    Profit Margin: {financial_data.get('profit_margin')}

    Create a professional report with:

    1. Revenue Analysis
    2. Profitability Analysis
    3. Debt Analysis
    4. Cash Flow Analysis
    5. Overall Financial Health

    Explain in simple but professional language.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text