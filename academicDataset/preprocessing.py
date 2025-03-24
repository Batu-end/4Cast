import pandas as pd
import matplotlib.pyplot as plt

# Load data and parse dates
df = pd.read_csv('academicDataset/data.csv', parse_dates=['Date'], index_col='Date')
print(df.head())  # Check the first few rows
print(df.isnull().sum())  # Check for missing values

df = df.drop('Volume', axis=1)  # Drop the 'Volume' column

df['Range'] = df['High'] - df['Low']  # Create a new column 'Range'
df = df.drop(['High', 'Low'], axis=1)  # Drop the 'High' and 'Low' columns


# Fill missing values

# Generate a complete date range and forward-fill missing values
df = df.asfreq('D', method='ffill')  # Forward-fill prices on non-trading days
df = df[~df.index.duplicated(keep='first')] # Remove duplicate dates

df.to_csv('academicDataset/data_cleaned.csv')  # Save cleaned data to a new file


