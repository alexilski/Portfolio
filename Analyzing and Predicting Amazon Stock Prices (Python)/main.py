# Alex Ilski
# Analyzing and Predicting Amazon Stock Prices
# https://alexilski.github.io/

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# Function that returns a list of converted dates as datetime type in mm/dd/yyyy format
def convertDates(dates):
    new_dates = []
    convert_month = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '5', 'Jun': '6',
                     'Jul': '7', 'Aug': '8', 'Sep': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

    for date in dates:
        separator = '/'
        split_date = date.split()
        split_date[0] = convert_month[split_date[0]]
        new_date = separator.join(split_date)
        new_dates.append(new_date)

    return pd.to_datetime(new_dates)


# DATA CLEANING

# Read csv file, reverse df to order by ascending dates
df = pd.read_csv('stock_data.csv', usecols=['Date', 'Open', 'High', 'Low', 'Price'])
df.iloc[:] = df.iloc[::-1].values

# Rename column, reorder all columns, remove commas
df = df.rename(columns={'Price': 'Close'})
df = df[['Date', 'Open', 'High', 'Low', 'Close']]
df = df.replace({',': ''}, regex=True)

# Convert price columns to float type, create two columns to track change in price
df = df.astype({'Open': float, 'High': float, 'Low': float, 'Close': float})
df['Change'] = round(df['Close'] - df['Open'], 1)
df['%Change'] = round(((df['Close'] - df['Open']) / df['Open']) * 100, 2)

# Convert date to mm/dd/yyyy format
df['Date'] = convertDates(df['Date'])
df['Date'] = df['Date'].dt.strftime('%m/%d/%Y')

# Export csv file
df.to_csv('stock_data_cleaned.csv', index=False)

# LINEAR REGRESSION

# Create two columns to track 10-day and 50-day simple moving average
df['SMA10'] = df['Close'].rolling(10).mean()
df['SMA50'] = df['Close'].rolling(50).mean()

# Create new df, drop first 50 rows to remove empty SMA50 values
lr_df = df[['Close', 'SMA10', 'SMA50']]
lr_df = lr_df.iloc[50:]

# Variables used for the models
x = lr_df[['SMA10']]
x2 = lr_df[['SMA50']]
y = lr_df[['Close']]

# Model 1: split SMA10 data, fit data into model, predict output, get r2 value
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
model = LinearRegression()
model.fit(x_train, y_train)
predictions = model.predict(x_test)
r2_score = model.score(y_test, predictions)

# Model 2: split SMA50 data, fit data into model, predict output, get r2 value
x_train2, x_test2, y_train2, y_test2 = train_test_split(x2, y, test_size=0.3, random_state=0)
model2 = LinearRegression()
model2.fit(x_train2, y_train2)
predictions2 = model2.predict(x_test2)
r2_score2 = model2.score(y_test2, predictions2)

# ANALYSIS

# Create text file and write information to it
f = open('analysis.txt', 'w')
print('Dataset Range:', df['Date'][0], '-', df['Date'][len(df) - 1], file=f)
print('Total Days Reported:', len(df), file=f)
print('Overall Average Price:', round(df['Close'].mean(), 1), file=f)
print('First Half Average Price:', round(df['Close'].iloc[0:252].mean(), 1), file=f)
print('Second Half Average Price:', round(df['Close'].iloc[252:len(df)].mean(), 1), file=f)
print('Less than or equal to 1% change in price:', len(df[df['%Change'] <= 1]), 'days', file=f)
print('Greater than 1% change in price:', len(df[df['%Change'] > 1]), 'days', file=f)
print('Maximum Price:', df['Close'][df['Close'].idxmax()], 'on', df['Date'][df['Close'].idxmax()], file=f)
print('Minimum Price:', df['Close'][df['Close'].idxmin()], 'on', df['Date'][df['Close'].idxmin()], file=f)
print('Greatest Positive Change in Price:', df['Change'][df['%Change'].idxmax()], 'on',
      df['Date'][df['%Change'].idxmax()], 'by', df['%Change'][df['%Change'].idxmax()], '%', file=f)
print('Greatest Negative Change in Price:', df['Change'][df['%Change'].idxmin()], 'on',
      df['Date'][df['%Change'].idxmin()], 'by', df['%Change'][df['%Change'].idxmin()], '%', file=f)
print('Overall Change in Price Since First Date:', round(df['Close'][len(df) - 1] - df['Close'][0], 1), file=f)
print('Coefficient of Determination (SMA10):', r2_score, file=f)
print('Coefficient of Determination (SMA50):', r2_score2, file=f)
f.close()

# VISUALIZATION

# Graph 1: market summary
plt.figure(1, figsize=(12, 8))

# Plot data
df.plot(x='Date', y='Close', label='Closing Price', color='steelblue', ax=plt.gca())
df.plot(x='Date', y='SMA10', label='10-Day Simple Moving Average (SMA)', color='green', ax=plt.gca())
df.plot(x='Date', y='SMA50', label='50-Day Simple Moving Average (SMA)', color='red', ax=plt.gca())

# Graph styling
plt.title('Amazon Market Summary: 03/01/2019 - 03/01/2021', fontsize=18)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Closing Price', fontsize=14)
plt.legend()
plt.grid()

# Export graph
plt.savefig('market_summary.jpg')

# Graph 2: SMA10 model
plt.figure(2, figsize=(12, 8))

# Plot Data
plt.scatter(x_train, y_train, label='Actual Closing Price (Training Set)', color='red', alpha=0.5)
plt.scatter(x_test, y_test, label='Actual Closing Price (Testing Set)', color='green', alpha=0.5)
plt.plot(x_train, model.predict(x_train), label='Predicted Closing Price', color='steelblue')

# Graph Styling
plt.title('Predicting Closing Price Using SMA10', fontsize=18)
plt.xlabel('SMA10 Closing Price', fontsize=14)
plt.ylabel('Closing Price', fontsize=14)
plt.legend()
plt.grid()

# Export Graph
plt.savefig('sma10.jpg')

# Figure 3: SMA50 model
plt.figure(3, figsize=(12, 8))

# Plot Data
plt.scatter(x_train2, y_train2, label='Actual Closing Price (Training Set)', color='red', alpha=0.5)
plt.scatter(x_test2, y_test2, label='Actual Closing Price (Testing Set)', color='green', alpha=0.5)
plt.plot(x_train2, model2.predict(x_train2), label='Predicted Closing Price', color='steelblue')

# Graph Styling
plt.title('Predicting Closing Price Using SMA50', fontsize=18)
plt.xlabel('SMA50 Closing Price', fontsize=14)
plt.ylabel('Closing Price', fontsize=14)
plt.legend()
plt.grid()

# Export figure
plt.savefig('sma50.jpg')

# Show graphs
plt.show()
