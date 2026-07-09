**Made by: Warisha Sohail
Email: warishasohail06@gmail.com**

# Sales & Operations Analytics Dashboard

An end-to-end data analytics project featuring an automated Python ETL pipeline,rigorous SQL business analysis, and an executive dashboard tracking retail profitability and customer segmentation.

## Project Overview
This project processes raw reatail transaction records, structures them via a custom programmatic ETL framework, and extracts core business performance matrices using SQL.

### Tech Stack
* **OS:** Ubuntu Linux
* **Data Engineering:** Python (Pandas)
* **Analytics Layer:** SQL (SQLite)
* **Data Visualization:** Power BI / Data Visualization tools

---

## Data Architecture & ETL Pipeline
The data follows a clean modular pipeline implemented in 'src/etl/pipeline.py':

1. **Extract:** Ingests raw transactional CSV data handling specific file encodings.
2. **Transform:** Dedupes rows, standardizes text data formatting, handles missing values dynamically, and engineers a custom 'Profit Margin' business metric.
3. **Load:** Outputs structured, clean analytics-ready data to 'data/processed'.

### How to Run the Pipeline
'''bash
# CLone the repository and navigate into it
git clone ,your-repo-link>
cd sales-analytics-dashboard

# Activate virtual enviornment and install dependencies
source venv/bin/activate
pip install -r requirements.txt

# Run ETL Pipeline
python3 src/etl/pipeline.py

# Run SQL Queries
python3 src/etl/sql_queries.py

## Core Business Insights (SQL Layer)
* **Segmentation:** Identified which customer segment drives the highest gross revenue vs. net profitability.
* **Product Performance:** Tracked top-performing Sub-Categories to optimize inventory allocation.
* **Regional Efficiency:** Evaluated geographical distribution of sales alongside localized profit margins.
 
 
