## Overview

For a data science class final project, I have sourced a dataset containing information about the historical stock prices of Amazon. Using various python libraries, I was able to clean the dataset, apply numerous functions, analyze the data, make predictions by fitting a linear model, and create visualizations.

## Data

The dataset used for this project can be found at: https://www.investing.com/equities/amazon-com-inc-historical-data. It ranges from 03/01/2019 to 03/01/2021 and consists of a date column followed by open-high-low-close (OHLC) columns. The market operates from Monday to Friday, therefore, data for weekend dates is not included in the dataset. The dataset that was initially downloaded from the link was unclean and unorganized, therefore, multiple lines of code were written in the program that would clean the dataset and export a new one to be used for further analysis.

## Results

Running the python file with the stock_data.csv dataset will create 5 files:

**stock_data_cleaned.csv** - Cleaned version of the original dataset with several changes. The dates have been ordered by ascending, one column was renamed and all columns have been reordered, commas have been removed, price columns were converted to float type, two new columns were added to track change in price, and dates have been converted to mm/dd/yyyy format.

**analysis.txt** - Text file written by python containing various information gathered from the data. This information includes totals, averages, maximums and minimums, R^2 values, etc.

**market_summary.jpg** - Visualization that displays the change in stock price over time along with its moving averages. The stock price experiences a significant drop around the time of the pandemic and then continually increases after the price recovers. The 10-Day Simple Moving Average (SMA) and 50-Day SMA are calculations included to help with analysis and to be used for a machine learning algorithm.

**sma10.jpg and sma50.jpg** - Linear regression model visualizations for SMA10 and SMA50. The independent variables used are the SMA10 and SMA50 values, while the dependent variable used is the closing price. One model is created using SMA10, while the other is created using SMA50. Both are compared to see which SMA is able to predict the closing price better. The coefficient of determination for the SMA10 model yields 0.9858371894397706, while the SMA50 model yields 0.9131291114069102. As expected, the SMA10 model has a higher coefficient of determination due to it closely following the closing price, unlike SMA50, which is more so used for long-term trends.
