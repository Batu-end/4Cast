import streamlit as st
import yfinance as yf
import plotly.graph_objects as go # for creating candlestick chart
import pandas as pd
from src.data_fetch import fetch_stock_data


###########################################
## Data Pulling, Processing and Charting ##
###########################################

# cache the stock data for faster loading, from 2020 to 2025
# @st.cache_data

# wide layout for beter visualization
st.set_page_config(layout="wide")

# using plotly, create a chart for the stock data
def create_candlestick_chart(data, ticker):
    fig = go.Figure()

    # closing prices chart
    fig.add_trace(go.Candlestick(x=data.index,
                                 open=data['Open', ticker],
                                 high=data['High', ticker],
                                 low=data['Low', ticker],
                                 close=data['Close', ticker],
                                 name=f'{ticker} Daily Closing Prices'))

    show_moving_averages = st.sidebar.checkbox('Show Moving Averages', value=False)

    # option to add moving averages if selected by the user
    if show_moving_averages:
        data['SMA_50'] = data['Close'].rolling(window=50).mean() # SMA stands for Simple Moving Average. finance shit. basically the avg price over specified period.
        data['SMA_200'] = data['Close'].rolling(window=200).mean()

        # plot the moving averages
        # add the 50-Day SMA trace
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data['SMA_50'],
            mode='lines',
            name='50-Day SMA'
        ))

        # add the 200-Day SMA trace
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data['SMA_200'],
            mode='lines',
            name='200-Day SMA'
        ))


    
    # customize the chart layout
    fig.update_layout(
        title=f"Closing Prices - {ticker}.",
        # label x-axis as Date and y-axis as Price (USD)
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        height=600,
        width=1200,
        xaxis_rangeslider_visible=False # to disable the range slider below
    )


    
    st.plotly_chart(fig, use_container_width=True)


# create a dropdown for stock ticker
st.title("4Cast - спс влаб")
stock_ticker = st.selectbox("Select a Stock", ["AAPL", "GOOG", "TSLA", "AMZN", "MSFT", "NVDA", "QQQ"]) # currently only 6 stocks available.

# fetch the data for the selected stock, selected period and intervals
data = fetch_stock_data(stock_ticker, period='1yr', interval='1d')

data.index = pd.to_datetime(data.index)



####################
## Error handling ##
####################

    # streamlit's own charts
    # st.line_chart(data['Close'])
    
# if data.isnull().any().any():
#     st.error("The stock data contains missing values. Please try another stock.")
#     st.write(data.isnull().sum())  # Show which columns have missing values
#     st.stop()


# st.subheader("head of the data")
# st.write(data.head()) # added a table to show the first 5 rows of the data, in order to see if the data is fetched correctly.

# st.subheader("Data Types")
# st.write(data.dtypes) # added a table to show the data types of the columns in the data.

# st.subheader("length of data indexes x and y")
# st.write(len(data.index), len(data['Close']))

# st.subheader("check for missing closed values")
# st.write(data['Close'].isnull().sum())  # Check for missing values

# data['Close'].fillna(method='ffill', inplace=True)  # Forward fill missing values

# st.subheader("are the close types numeric?")
# st.write(pd.api.types.is_numeric_dtype(data['Close']))

# st.subheader("head of the close data")
# st.write(data['Close'].head())
# st.subheader("columns")
# st.write(data.columns)

# st.subheader("indexes to see if they are datetime")
# st.write(data.index)


##############################
## Create Candlestick Chart ##
##############################

# create a trading-view like chart for the stock
create_candlestick_chart(data, stock_ticker)