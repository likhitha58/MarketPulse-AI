import yfinance as yf


def get_financial_data(ticker):

    stock = yf.Ticker(ticker)

    info = stock.info

    financials = stock.financials
    balance_sheet = stock.balance_sheet
    cashflow = stock.cashflow

    data = {
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE"),
        "profit_margin": info.get("profitMargins")
    }

    try:
        data["revenue"] = financials.loc["Total Revenue"].iloc[0]
    except:
        data["revenue"] = None

    try:
        data["net_income"] = financials.loc["Net Income"].iloc[0]
    except:
        data["net_income"] = None

    try:
        data["cash"] = balance_sheet.loc["Cash And Cash Equivalents"].iloc[0]
    except:
        data["cash"] = None

    try:
        data["debt"] = balance_sheet.loc["Total Debt"].iloc[0]
    except:
        data["debt"] = None

    try:
        data["operating_cash_flow"] = cashflow.loc["Operating Cash Flow"].iloc[0]
    except:
        data["operating_cash_flow"] = None

    return data