from agents.news_agent import news_agent


from tools.news_tool import get_company_news

news = get_company_news("NVDA")

print(news)

report = news_agent("NVDA")

print(report)