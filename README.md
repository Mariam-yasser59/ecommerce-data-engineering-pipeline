# E-Commerce Data Engineering Pipeline

An end-to-end data engineering project that builds a complete
e-commerce data pipeline from raw CSV data to a PostgreSQL
data warehouse and Power BI dashboard.

The project demonstrates data ingestion, data transformation,
relational data warehousing, data quality validation, and
business analytics.

---

## Project Architecture

```text
Raw CSV Files
      ↓
Python ETL
      ↓
PostgreSQL Staging Layer
      ↓
SQL Transformations
      ↓
Star Schema Data Warehouse
      ↓
Power BI Dashboard  ![E-Commerce Power BI Dashboard](screenshots/powerbi_dashboard.png)