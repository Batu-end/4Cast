'''
preproces.py

This module preprocesses the historical stock price data.
The first iteration will work with daily closing prices only.

Functions:
- preprocess_data: preprocess the stock data that has been provided from the data_fetch module and indicators.
'''

import numpy as np
from sklearn.preprocessing import MinMaxScaler
import yfinance as yf
from datetime import datetime
import math

sequence_length = 60

def preprocess_data(data):

    nvda = yf.Ticker('NVDA')
    end_date = datetime.now().strftime('%Y-%m-%d')

    nvda_hist = nvda.history(start='2019-01-01', end=end_date)

    nvda_close = nvda_hist['Close']
    nvda_values = nvda_close.values
    nvda_values = nvda_values.reshape(-1, 1)

    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(nvda_values)

    # X, y = [], []
    # for i in range(len(scaled_data) - sequence_length):
    #     X.append(scaled_data[i:i+sequence_length])
    #     y.append(scaled_data[i+sequence_length])

    # return np.array(X), np.array(y)
    training_split = math.floor(len(scaled_data) * 0.8)

    training_nvda = scaled_data[0:training_split]
    training_ind_nvda = []

    for i in range(sequence_length, len(training_nvda)):
        training_ind_nvda.append(training_nvda[i-sequence_length:i][0])
        training_dep_nvda.append(training_nvda[i][0])

    training_ind_nvda, training_dep_amzn = np.array(training_ind_nvda), np.array(training_dep_nvda)
    training_ind_nvda = np.reshape(training_ind_nvda, (training_ind_nvda.shape[0], training_ind_nvda.shape[1], 1))

# def train_test_split(X, y, test_ratio=0.8):
#     train_size = int(len(X) * test_ratio)

#     X_train, X_test = X[:train_size], X[train_size:]
#     y_train, y_test = y[:train_size], y[train_size:]

#     return X_train, X_test, y_train, y_test

