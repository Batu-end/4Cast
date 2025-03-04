"""
data_fetch.py

This module fetches historical stock price data using the Yahoo Finance API.

Functions:
- fetch_stock_data
"""

import yfinance as yf # previous price data API (free)
import pandas as pd
from datetime import datetime, timedelta
from src.indicators import add_indicators

def fetch_stock_data(ticker, period="5y", interval="1d"):
    """
    Fetch historical stock data from Yahoo Finance.

    Args:
    ticker (str): The stock ticker symbol (e.g., 'AAPL', 'GOOG').
    period (str): The period for which to fetch data (e.g., '1mo', '1yr', '5d').
                  If '1yr', the function will calculate a custom start date.
    interval (str): The data interval (e.g., '1d', '1h', '5m').

    Returns:
    pandas.DataFrame: A DataFrame containing the stock data.
    """

    end_date = datetime.now()

    if period == '1yr':
        start_date = end_date - timedelta(days=365)
        stock_data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
    else:
        stock_data = yf.download(ticker, period=period, interval=interval)

    data = add_indicators(stock_data)

    return stock_data

# write the data to an Excel file for visual representation
def write_to_excel(data):

    ticker = "NVDA"
    start_date = "2020-01-01"
    end_date = "2025-02-21"

    data = yf.download(ticker, start=start_date, end=end_date)

    # save the data to an Excel file
    excel_file = "stock_data.xlsx"
    data.to_excel(excel_file)

    print(f"Data for {ticker} saved to {excel_file}")