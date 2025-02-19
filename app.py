import streamlit as st
import yfinance as yf
import plotly.graph_objects as go # for creating candlestick chart
import pandas as pd

# cache the stock data for faster loading, from 2020 to 2025
@st.cache_data
def fetch_stock_data(ticker, start_date='2020-01-01', end_date='2025-01-01'):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data



# using plotly, create a chart for the stock data
def create_candlestick_chart(data, ticker):
    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name=ticker,
    )])

    # option to add moving averages if selected by the user
    if st.sidebar.checkbox('Show Moving Averages'):
        data['SMA_50'] = data['Close'].rolling(window=50).mean() # SMA stands for Simple Moving Average. finance shit. basically the avg price over specified period.
        data['SMA_200'] = data['Close'].rolling(window=200).mean()

        # plot the moving averages
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data['SMA_50'],
            mode='lines',
            name='50-Day SMA'
        ))

        fig.add_trace(go.Scatter(
            x=data.index,
            y=data['SMA_200'],
            mode='lines',
            name='200-Day SMA'
        ))


    fig.add_trace(go.Scatter(
        x=data.index,
        y=data['Close'],
        mode='lines',
        name=f"{ticker} Close Price",
        line=dict(color='purple', width=2)
    ))
    
    # customize the chart layout
    fig.update_layout(
        title=f"{ticker} Chart with closing prices.",
        # label x-axis as Date and y-axis as Price (USD)
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        xaxis_rangeslider_visible=False # to disable the range slider
    )

    

    st.plotly_chart(fig)

# create a dropdown for stock ticker
st.title("4Cast - как дела вдаб")
stock_ticker = st.selectbox("Select a Stock", ["AAPL", "GOOG", "TSLA", "AMZN", "MSFT", "NVDA"]) # currently only 6 stocks available.

# fetch the data for the selected stock
data = fetch_stock_data(stock_ticker)

data.index = pd.to_datetime(data.index)


if data.empty:
    st.error("СУКА БЛЯТЬ")
    st.stop()

st.write(data.head()) # added a table to show the first 5 rows of the data, in order to see if the data is fetched correctly.

# create a trading-view like chart for the stock
create_candlestick_chart(data, stock_ticker)