import yfinance as yf


# --------------------------------
# Company Information
# --------------------------------

def get_company_info(ticker):

    stock = yf.Ticker(ticker)

    info = stock.info

    return {
        "name": info.get("longName"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "market_cap": info.get("marketCap"),
        "summary": info.get("longBusinessSummary")
    }


# --------------------------------
# Dashboard Metrics
# --------------------------------

def get_stock_metrics(ticker):

    stock = yf.Ticker(ticker)

    info = stock.info

    market_cap = info.get("marketCap")

    if market_cap:

        if market_cap >= 1_000_000_000_000:
            market_cap = f"{market_cap / 1_000_000_000_000:.2f}T"

        elif market_cap >= 1_000_000_000:
            market_cap = f"{market_cap / 1_000_000_000:.2f}B"

        else:
            market_cap = str(market_cap)

    return {

        "price": info.get("currentPrice"),

        "market_cap": market_cap,

        "pe_ratio": info.get("trailingPE"),

        "sector": info.get("sector")
    }