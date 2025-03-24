import pandas as pd
import matplotlib.pyplot as plt

# Load data and parse dates
df = pd.read_csv('academicDataset/data.csv', parse_dates=['Date'], index_col='Date')
print(df.head())  # Check the first few rows
print(df.isnull().sum())  # Check for missing values

# Generate a complete date range and forward-fill missing values
df = df.asfreq('D', method='ffill')  # Forward-fill prices on non-trading days
df = df[~df.index.duplicated(keep='first')] # Remove duplicate dates

df.to_csv('academicDataset/data_cleaned.csv')  # Save cleaned data to a new file


