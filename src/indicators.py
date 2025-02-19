import talib as ta # technical analysis library

def add_indicators(df):
    df["Returns"] = df["Close"].pct_change() # daily %return
    df["Volatility"] = df["Returns"].rolling(window=30).std() # 30 day rolling volatility
    df["RSI"] = ta.RSI(df["Close"], timeperiod=14) # momentum indicator
    df["MACD"], _, _ = ta.MACD(df["Close"], fastperiod=12, slowperiod=26, signalperiod=9) # trend-following momentum indicator
    df.dropna(inplace=True)
    return df