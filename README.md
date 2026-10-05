# E-Commerce Data Engineering Pipeline

## Overview

An end-to-end data engineering pipeline for processing
e-commerce data from CSV sources, transforming the data
using Python, loading it into PostgreSQL, building a
dimensional data warehouse, and visualizing business
metrics using Power BI.

## Architecture

CSV Files
    ↓
Python ETL
    ↓
Data Cleaning & Transformation
    ↓
PostgreSQL Staging
    ↓
Data Warehouse
    ↓
Power BI

## Tech Stack

- Python
- Pandas
- SQL
- PostgreSQL
- SQLAlchemy
- Power BI
- Git

## Data Warehouse

The project uses a Star Schema consisting of:

- dim_customer
- dim_product
- dim_date
- fact_sales

## ETL Process

### Extract

Read raw e-commerce data from CSV files.

### Transform

- Remove duplicates
- Handle missing values
- Convert data types
- Calculate total sales
- Validate records

### Load

Load transformed data into PostgreSQL staging tables
and populate the dimensional data warehouse.

## Data Quality

The pipeline includes validation checks for:

- Duplicate records
- Missing values
- Invalid quantities
- Missing dimension records
- Referential integrity

## Dashboard

The Power BI dashboard provides:

- Total Sales
- Total Orders
- Total Customers
- Average Order Value
- Sales by Month
- Sales by Category
- Top 10 Products
- Interactive filters