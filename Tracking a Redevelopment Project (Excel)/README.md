## Overview

Working as a junior project manager for an architectural metal and glass company, I was given the task of developing an excel file that would track and visualize the progress of the company's largest redevelopment project, 111 Wall Street. Using excel, I was able to build a dataset from scratch, apply numerous formulas, visualize the building's elevations, and create a final dashboard. 

## Data

The dataset used for this project was created from scratch using information provided by the company. It is 2444 rows long, each representing a separate window unit, along with several columns. These columns consist of floor, unit, unit type, façade, position, G/L, and 6 other date columns that track the date of when the unit was fabricated, shipped, delivered, installed, inspected, and commissioned. These 6 columns have been filled with random dates to display the functionality of the workbook and how each sheet is automatically updated based on which columns are filled in.

## Results

In response to the given task, I have created an excel workbook consisting of 4 sheets:

**Dashboard** - A progress dashboard that consists of several graphs depicting the current status of the project and some calculations. Each graph utilizes numeric information from a separate sheet where formulas are used to do calculations on the main dataset. Changes or additions made to the main dataset are instantly reflected on the dashboard sheet as it does not require manual updating.

**Elevations** - Visualization that displays each façade of the building and is color-coded to represent the status of each window unit. The cells in the sheet are resized to fit within each window unit and each cell uses a formula to perform a two-way lookup via INDEX and MATCH. The lookup is performed on the main dataset and then the resulting value is color-coded based on conditional formatting. Changes or additions made to the main dataset are instantly reflected on the elevations sheet as they do not require manual updating.

**Master List** - Main dataset that keeps track of each individual window unit. Using a formula, the status column tracks the current status of the window unit in terms of whether or not it has been fabricated, shipped, delivered, installed, inspected, or commissioned. As the status is updated in any given row, all other sheets using information from the main dataset are updated automatically.

**Totals** - Condensed version of the main dataset that calculates the totals for the 6 date columns using various formulas. The first table calculates the totals by each floor, the second table calculates the totals by each façade, and the third table calculates the totals by each phase along with an overall total. The dashboard references each table in this sheet for its graphs and calculations. Changes or additions made to the main dataset are instantly reflected on the totals sheet as they do not require manual updating.
