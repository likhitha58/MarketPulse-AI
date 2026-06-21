import yfinance as yf


# --------------------------------
# Indian Stocks
# --------------------------------

INDIAN_STOCKS = {

    # Banking
    "hdfc bank": "HDFCBANK.NS",
    "icici bank": "ICICIBANK.NS",
    "sbi": "SBIN.NS",
    "kotak bank": "KOTAKBANK.NS",
    "axis bank": "AXISBANK.NS",
    "indusind bank": "INDUSINDBK.NS",

    # IT
    "tcs": "TCS.NS",
    "infosys": "INFY.NS",
    "wipro": "WIPRO.NS",
    "hcl": "HCLTECH.NS",
    "hcl tech": "HCLTECH.NS",
    "tech mahindra": "TECHM.NS",

    # Conglomerates
    "reliance": "RELIANCE.NS",
    "l&t": "LT.NS",
    "lt": "LT.NS",
    "adani enterprises": "ADANIENT.NS",
    "adani ports": "ADANIPORTS.NS",
    "adani green": "ADANIGREEN.NS",

    # Finance
    "bajaj finance": "BAJFINANCE.NS",
    "bajaj finserv": "BAJAJFINSV.NS",
    "motilal oswal": "MOTILALOFS.NS",
    "jio financial": "JIOFIN.NS",

    # FMCG
    "hindustan unilever": "HINDUNILVR.NS",
    "hul": "HINDUNILVR.NS",
    "itc": "ITC.NS",
    "britannia": "BRITANNIA.NS",
    "nestle india": "NESTLEIND.NS",
    "dabur": "DABUR.NS",

    # Auto
    "maruti": "MARUTI.NS",
    "maruti suzuki": "MARUTI.NS",
    "tata motors": "TATAMOTORS.NS",
    "mahindra": "M&M.NS",
    "mahindra and mahindra": "M&M.NS",
    "bajaj auto": "BAJAJ-AUTO.NS",
    "hero motocorp": "HEROMOTOCO.NS",

    # Pharma
    "sun pharma": "SUNPHARMA.NS",
    "cipla": "CIPLA.NS",
    "dr reddy": "DRREDDY.NS",
    "apollo hospitals": "APOLLOHOSP.NS",

    # Telecom
    "bharti airtel": "BHARTIARTL.NS",
    "airtel": "BHARTIARTL.NS",

    # Energy
    "ongc": "ONGC.NS",
    "coal india": "COALINDIA.NS",
    "ntpc": "NTPC.NS",
    "power grid": "POWERGRID.NS",

    # Consumer
    "asian paints": "ASIANPAINT.NS",
    "titan": "TITAN.NS",

    # New Age Tech
    "zomato": "ETERNAL.NS",
    "paytm": "PAYTM.NS",
    "nykaa": "NYKAA.NS"
}


# --------------------------------
# US Stocks
# --------------------------------

US_STOCKS = {

    "nvidia": "NVDA",
    "apple": "AAPL",
    "microsoft": "MSFT",
    "google": "GOOGL",
    "alphabet": "GOOGL",
    "amazon": "AMZN",
    "tesla": "TSLA",
    "meta": "META",
    "facebook": "META",
    "netflix": "NFLX",
    "amd": "AMD",
    "intel": "INTC",
    "oracle": "ORCL",
    "salesforce": "CRM",
    "uber": "UBER",
    "palantir": "PLTR",
    "openai": "MSFT",
    "broadcom": "AVGO",
    "qualcomm": "QCOM",
    "adobe": "ADBE",
    "spotify": "SPOT",
    "airbnb": "ABNB"
}


# --------------------------------
# Resolve Ticker
# --------------------------------

def resolve_ticker(user_input):

    query = user_input.lower().strip()

    # Indian Stocks

    if query in INDIAN_STOCKS:

        return INDIAN_STOCKS[query]

    # US Stocks

    if query in US_STOCKS:

        return US_STOCKS[query]

    # Yahoo Search

    try:

        search = yf.Search(
            query=user_input,
            max_results=10
        )

        quotes = search.quotes

        if quotes:

            for quote in quotes:

                symbol = quote.get("symbol")

                if symbol:

                    return symbol

    except Exception as e:

        print(
            "Ticker Search Error:",
            e
        )

    # Fallback

    return user_input.upper()