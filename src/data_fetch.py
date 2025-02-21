"""
data_fetch.py

This module fetches historical stock price data using the Yahoo Finance API.

Functions:
- fetch_stock_data
"""

import yfinance as yf # previous price data API (free)
import pandas as pd
from datetime import datetime, timedelta

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
    
    # Handle custom period logic
    if period == '1yr':
        start_date = end_date - timedelta(days=365)
        stock_data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
    else:
        stock_data = yf.download(ticker, period=period, interval=interval)
    
    return stock_data