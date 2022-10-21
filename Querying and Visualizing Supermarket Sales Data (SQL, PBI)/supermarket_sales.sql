# Alex Ilski
# Querying and Visualizing Supermarket Sales Data
# https://alexilski.github.io/

# Convert date to proper format
UPDATE portfolioproject.supermarket_sales
SET Date = str_to_date(Date, '%m/%d/%Y');

# Drop unneeded columns, change datatypes
ALTER TABLE portfolioproject.supermarket_sales
DROP COLUMN `Tax 5%`,
DROP COLUMN Time,
DROP COLUMN cogs,
DROP COLUMN `gross margin percentage`,
MODIFY Date date,
MODIFY UnitPrice decimal(7, 2),
MODIFY Revenue decimal(7, 2),
MODIFY Profit decimal(7, 2),
ORDER BY Date;

# Main dataset
SELECT * 
FROM portfolioproject.supermarket_sales;

# Totals
SELECT SUM(Quantity) AS TotalQuantity, SUM(Revenue) AS TotalRevenue, SUM(Profit) AS TotalProfit, Round(SUM(Revenue)/SUM(Quantity), 2) AS OverallAvgPrice, ROUND(AVG(Rating), 1) AS OverallAvgRating
FROM portfolioproject.supermarket_sales
WHERE Profit IS NOT NULL;

# Daily totals for each branch
SELECT Date, Branch, City, SUM(Quantity) AS Quantity, SUM(Revenue) AS Revenue, SUM(Profit) AS Profit, Round(SUM(Revenue)/SUM(Quantity), 2) AS AvgPrice, ROUND(AVG(Rating), 1) AS AvgRating
FROM portfolioproject.supermarket_sales
WHERE Profit IS NOT NULL
GROUP BY Date, Branch
ORDER BY Date, Branch;

# Monthly totals for each branch
SELECT MONTHNAME(Date) AS Month, Branch, City, SUM(Quantity) AS Quantity, SUM(Revenue) AS Revenue, SUM(Profit) AS Profit, Round(SUM(Revenue)/SUM(Quantity), 2) AS AvgPrice, ROUND(AVG(Rating), 1) AS AvgRating
FROM portfolioproject.supermarket_sales
WHERE Profit IS NOT NULL
GROUP BY MONTHNAME(Date), Branch
ORDER BY MONTH(Date), Branch;

# Overall totals for each branch
SELECT Branch, City, SUM(Quantity) AS Quantity, SUM(Revenue) AS Revenue, SUM(Profit) AS Profit, Round(SUM(Revenue)/SUM(Quantity), 2) AS AvgPrice, ROUND(AVG(Rating), 1) AS AvgRating
FROM portfolioproject.supermarket_sales
WHERE Profit IS NOT NULL
GROUP BY Branch
ORDER BY Branch;

# Daily totals for each product line
SELECT Date, ProductLine, SUM(Quantity) AS Quantity, SUM(Revenue) AS Revenue, SUM(Profit) AS Profit, Round(SUM(Revenue)/SUM(Quantity), 2) AS AvgPrice
FROM portfolioproject.supermarket_sales
WHERE Profit IS NOT NULL
GROUP BY Date, ProductLine
ORDER BY Date, ProductLine;

# Monthly totals for each product line
SELECT MONTHNAME(Date) AS Month, ProductLine, SUM(Quantity) AS Quantity, SUM(Revenue) AS Revenue, SUM(Profit) AS Profit, Round(SUM(Revenue)/SUM(Quantity), 2) AS AvgPrice
FROM portfolioproject.supermarket_sales
WHERE Profit IS NOT NULL
GROUP BY MONTHNAME(Date), ProductLine
ORDER BY MONTH(Date), ProductLine;

# Overall totals for each product line
SELECT ProductLine, SUM(Quantity) AS Quantity, SUM(Revenue) AS Revenue, SUM(Profit) AS Profit, Round(SUM(Revenue)/SUM(Quantity), 2) AS AvgPrice
FROM portfolioproject.supermarket_sales
WHERE Profit IS NOT NULL
GROUP BY ProductLine
ORDER BY ProductLine;

# Preferred payment type based on customer type
SELECT CustomerType, Payment, COUNT(Payment) AS Count, ROUND(((COUNT(Payment) / 1000) * 100), 2) AS Percent
FROM portfolioproject.supermarket_sales
WHERE Profit IS NOT NULL
GROUP BY CustomerType, Payment
ORDER BY CustomerType DESC, Payment;

# General preferred payment type
SELECT Payment, COUNT(Payment) AS Count, ROUND(((COUNT(Payment) / 1000) * 100), 2) AS Percent
FROM portfolioproject.supermarket_sales
WHERE Profit IS NOT NULL
GROUP BY Payment
ORDER BY Payment;

# Preferred product line based on gender
SELECT Gender, ProductLine, COUNT(ProductLine) AS Count, ROUND(((COUNT(ProductLine) / 1000) * 100), 2) AS Percent
FROM portfolioproject.supermarket_sales
WHERE Profit IS NOT NULL
GROUP BY Gender, ProductLine
ORDER BY GENDER DESC, ProductLine;

# General preferred product line
SELECT ProductLine, COUNT(ProductLine) AS Count, ROUND(((COUNT(ProductLine) / 1000) * 100), 2) AS Percent
FROM portfolioproject.supermarket_sales
WHERE Profit IS NOT NULL
GROUP BY ProductLine
ORDER BY ProductLine;