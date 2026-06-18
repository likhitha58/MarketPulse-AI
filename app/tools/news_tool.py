import yfinance as yf

def get_company_news(ticker):

    stock = yf.Ticker(ticker)

    news = stock.news[:5]

    cleaned_news = []

    for article in news:

        content = article.get("content", {})

        cleaned_news.append(
            {
                "title": content.get("title"),
                "summary": content.get("summary"),
                "publisher": content.get("provider", {}).get("displayName"),
                "date": content.get("pubDate")
            }
        )

    return cleaned_news