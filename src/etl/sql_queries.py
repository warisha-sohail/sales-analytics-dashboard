import sqlite3
import pandas as pd

#Load clean data
df = pd.read_csv("data/processed/superstore_clean.csv")

#Connect to a temporary SQL database
conn = sqlite3.connect("sales_analysis.db")
df.to_sql("sales", conn, if_exists="replace", index=False)

print("--- SQL PORTFOLIO QUERIES ---")

#1. Customer Segmentation Analysis
query_segments = """
SELECT Segment,
    COUNT(*) as Total_Orders,
    SUM(Sales) as Total_Revenue,
    SUM(Profit) as Total_Profut
FROM sales
GROUP BY Segment
ORDER BY Total_Revenue DESC;
"""

print("\n1.Performance by Customer Segment:")
print(pd.read_sql(query_segments, conn))

#2. Top-selling Sub-categories
query_subcat = """
SELECT [Sub-Category],
    SUM(Sales) as Total_Sales,
    SUM(Quantity) as Total_Units_Sold
FROM sales
GROUP BY [Sub-Category]
ORDER BY Total_Sales DESC
LIMIT 5;
"""
print("\n2. Top 5 Sub-Categories by Sales:")
print(pd.read_sql(query_subcat, conn))

#3. Regional Profit Margin Analysis
query_regions = """
SELECT Region,
    SUM(Sales) as Regional_Sales,
    AVG([Profit Margin]) as Avg_Profit_Margin
FROM sales
GROUP BY Region
ORDER BY Regional_Sales DESC;
"""
print("\n3. Regional Performance & Margins:")
print(pd.read_sql(query_regions, conn))

conn.close()

