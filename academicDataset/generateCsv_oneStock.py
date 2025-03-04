import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

ticker = 'AAPL'
end_date = datetime.today()
# print(end_date)
start_date = end_date - timedelta(days=365 * 30)
# print(start_date)
data = yf.download(ticker, start=start_date, end=end_date)
output_path = os.path.join(os.getcwd(), 'academicDataset', 'data.csv')
data.to_csv(output_path)
