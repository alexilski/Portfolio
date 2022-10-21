## Overview

Looking to brush up on my visualization skills, I came across a random supermarket sales dataset on kaggle consisting of over a dozen columns with varying data types. Using SQL and Power BI I was able to clean the dataset, run multiple queries, explore the data, make calculations, and create a final interactive dashboard.

## Data

The dataset used for this project can be found at: https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales. It ranges from 01/01/2019 to 03/30/2021 and consists of 1000 unique invoice IDs followed by several columns that pertain to branch information, customer information, and purchase information. Certain data types had to be changed when the dataset was imported into SQL and unneeded columns were dropped. Overall, much cleaning wasn't needed due to the dataset being fairly small and well-organized.

## Results

This project consists of two main files:

**supermarket_sales.sql** - SQL file containing 12 queries for data exploration along with some commands for cleaning the dataset. UPDATE and ALTER is used to convert the date column into a proper format, drop unneeded columns, change several columns to the appropriate data type, and order the dataset by date in ascending order. Following the cleaning commands are 12 queries which explore and breakdown the dataset in various ways. The first set of queries explores the daily, monthly, and overall totals for each supermarket branch location. The next set of queries explores the daily, monthly, and overall totals for each product line within all 3 branches. The final set of queries explores the preferred payment type based on the customer, general preferred payment type, preferred product line based on gender, and the general preferred product line.

**supermarket_sales_dashboard.pbix** - Interactive dashboard consisting of 8 visualizations describing the entire dataset and totals for units sold, revenue, profit, and rating. The two slicers included allow you to choose a specific date range and branch location which will update every visualization in the dashboard accordingly. This dashboard provides financial insight into the performance of the supermarket based primarily on its revenue and profit.
