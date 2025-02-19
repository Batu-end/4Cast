"""
data_fetch.py

This module fetches historical stock price data using the Yahoo Finance API.

Functions:
- fetch_stock_data
"""

import yfinance as yf # previous price data API (free)
import pandas as pd

def fetch_stock_data(ticker, period="5y", interval="1d"):
    """
    Fetch historical stock data for a given ticker.

    Parameters:
    - ticker (str): Stock symbol ("AAPL" for Apple).
    - period (str): Time range.
    - interval (str): Data granularity.

    Returns:
    - DataFrame: Stock price history containing Open, High, Low, Close, Volume.
    """

    df = yf.download(ticker, period=period, interval=interval)
    return df