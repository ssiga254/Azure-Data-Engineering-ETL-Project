# Azure Sales Data Engineering Project

## Project Overview

This project demonstrates an end-to-end Azure Data Engineering solution using Medallion Architecture (Bronze, Silver, and Gold layers). The pipeline simulates a real-world retail sales data processing workflow where raw sales data is ingested, transformed, validated, and prepared for business reporting.

The project showcases Azure Data Engineering concepts including data ingestion, data cleansing, PySpark transformations, aggregations, SQL validation, and reporting-ready datasets.

---

## Business Problem

A retail company receives daily sales data from multiple sources. The business requires a scalable solution to:

- Ingest raw sales data
- Clean and standardize records
- Create business-ready datasets
- Generate aggregated sales metrics
- Support reporting and dashboarding

---

## Solution Architecture

Source CSV Files

↓

Azure Data Lake Storage (Bronze Layer)

↓

PySpark Data Transformations (Silver Layer)

↓

Business Aggregations (Gold Layer)

↓

Power BI Dashboard

---

## Medallion Architecture

### Bronze Layer

- Stores raw source data
- Preserves original records
- Used for auditing and reprocessing

### Silver Layer

- Removes duplicate records
- Handles missing values
- Standardizes data formats
- Improves data quality

### Gold Layer

- Creates business-ready datasets
- Generates aggregated metrics
- Supports reporting and analytics

---

## Technologies Used

- Azure Data Lake Storage Gen2
- Azure Data Factory
- Azure Databricks
- PySpark
- SQL
- Power BI
- GitHub

---

## Project Structure

```text
Azure-Sales-Data-Engineering-Project
│
├── README.md
├── Interview_Explanation.md
│
├── data
│   ├── customers.csv
│   ├── products.csv
│   └── sales.csv
│
├── pyspark
│   ├── bronze_to_silver.py
│   └── silver_to_gold.py
│
├── sql
│   └── validation_queries.sql
│
├── architecture
│   └── architecture_diagram.png
│
└── screenshots
```

## Data Pipeline Workflow

### Step 1: Data Ingestion

- Source sales files are received in CSV format.
- Data is stored in the Bronze Layer without modification.

### Step 2: Data Cleansing

- Duplicate records are removed.
- Missing values are handled.
- Data quality checks are performed.

### Step 3: Data Transformation

- Business transformations are applied using PySpark.
- Data is standardized and enriched.

### Step 4: Data Aggregation

- Sales metrics are generated.
- Customer-level summaries are created.
- Gold layer datasets are produced.

### Step 5: Data Validation

- SQL queries are used to validate transformed datasets.
- Aggregated metrics are verified.

---

## Sample PySpark Transformations

### Bronze to Silver

- Read source CSV files
- Remove duplicates
- Handle null values

### Silver to Gold

- Aggregate sales metrics
- Generate reporting datasets
- Create customer-level summaries

---

## SQL Validation

SQL queries are used to validate business metrics generated during transformations.

Example:

```sql
SELECT
    customer_id,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY customer_id;
```

---

## Key Learnings

- Medallion Architecture
- Azure Data Engineering Concepts
- Data Ingestion
- Data Cleansing
- Data Transformation
- PySpark Development
- SQL Validation
- Data Aggregation
- Reporting Layer Design

---

## Business Benefits

- Improved data quality
- Centralized data processing
- Faster reporting
- Scalable architecture
- Better decision-making through analytics

---

## Future Enhancements

- Incremental Data Loads
- Slowly Changing Dimensions (SCD Type 1 & Type 2)
- Azure Data Factory Pipelines
- Delta Lake Implementation
- Automated Data Quality Checks
- Power BI Dashboard Integration

---

## Author

Sruthi

Aspiring Azure Data Engineer | SQL | PySpark | Azure Data Factory | Databricks
