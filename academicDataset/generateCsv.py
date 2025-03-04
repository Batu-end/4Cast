import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

tickers = ["AAPL", "GOOG", "TSLA", "AMZN", "MSFT", "NVDA", "QQQ"]
end_date = datetime.today()
# print(end_date)
start_date = end_date - timedelta(days=365 * 30)
# print(start_date)

close_df = pd.DataFrame()
for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    close_df[ticker] = data['Close']
# print(close_df)
output_path = os.path.join(os.getcwd(), 'academicDataset', 'close_data.csv')
close_df.to_csv(output_path)