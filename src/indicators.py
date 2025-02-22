import ta
import ta.volume # technical analysis library

def add_indicators(df):
    df["Returns"] = df["Close"].pct_change() # daily %return
    df["Volatility"] = df["Returns"].rolling(window=30).std() # 30 day rolling volatility
    df.dropna(inplace=True)
    return df

def calculate_OBV(close, volume):
    obv = ta.volume.on_balance_volume(close, volume)
    return obv