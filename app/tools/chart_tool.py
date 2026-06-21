import yfinance as yf
import pandas as pd


def get_stock_history(ticker):

    stock = yf.Ticker(ticker)

    history = stock.history(
        period="1y"
    )

    return history