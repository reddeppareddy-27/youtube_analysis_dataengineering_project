# 🔧 AWS Glue – ETL Pipeline

## 📌 Overview

AWS Glue is used in this project to perform **data cataloging, schema discovery, and ETL (Extract, Transform, Load) operations**.

It plays a key role in transforming raw data stored in **Amazon S3** into **analytics-ready datasets** in Parquet format.

---

## 🧾 Glue Components Used

| Component            | Purpose |
|---------------------|--------|
| Glue Crawler        | Automatically detects schema from S3 data |
| Glue Data Catalog   | Stores metadata (tables, schema, location) |
| Glue ETL Jobs       | Transforms CSV → Parquet |
| Glue Studio         | Builds visual ETL pipeline (join + transform) |

---

## 🏗️ Glue Workflow in Project

```

Raw Data (S3)
↓
Glue Crawler (Schema Detection)
↓
Glue Data Catalog
↓
Glue ETL Job (CSV → Parquet)
↓
Cleansed Layer (S3)
↓
Glue Studio (Join JSON + CSV)
↓
Analytics Layer (S3)

```

---

## 🔍 1. Glue Crawlers

Glue Crawlers are used to scan S3 buckets and infer schema.

### 🔹 Crawlers Created

| Crawler Name       | Data Source              | Output Table |
|--------------------|-------------------------|-------------|
| json-crawler       | JSON category data      | clean_category_data |
| csv-crawler        | Raw CSV statistics      | raw_statistics |
| analytics-crawler  | Final analytics data    | final_analytics |

---

## 📚 2. Glue Data Catalog

The Glue Data Catalog acts as a **central metadata repository**.

### Example Tables

| Table Name            | Description |
|----------------------|------------|
| raw_statistics       | Raw CSV data from S3 |
| clean_category_data  | Processed JSON metadata |
| final_analytics      | Final joined dataset |

---

## 🔄 3. Glue ETL Job (CSV → Parquet)

### 📌 Purpose

Convert raw CSV data into optimized **Parquet format** for better performance.

### ⚙️ Configuration

| Parameter        | Value |
|-----------------|------|
| Job Type        | Spark (Python) |
| Source          | S3 (CSV files) |
| Target          | S3 (Parquet files) |
| Partition Key   | region |

---

### 🧠 Transformations Applied

- Converted CSV → Parquet
- Standardized schema (bigint, string)
- Applied partitioning by `region`
- Filtered invalid/unsupported data (UTF issues)

---

### 📂 Output Structure

```

clean_bucket/

raw_statistics/
region=ca/
region=us/
region=gb/

```

---

## 🔗 4. Glue Studio (Final ETL)

Glue Studio is used to create a **visual ETL pipeline**.

### 📌 Purpose

- Join processed CSV data with category metadata
- Create final analytics dataset

---

### 🔄 Join Logic

| Left Table        | Right Table         | Join Key |
|------------------|--------------------|----------|
| raw_statistics   | clean_category_data| category_id = id |

---

### 📂 Output

```

analytics_bucket/

region=ca/
category_id=10/
category_id=20/

region=us/
category_id=10/

```

---

## ⚡ Partitioning Strategy

| Column       | Purpose |
|-------------|--------|
| region       | Improves query performance |
| category_id  | Enables faster filtering |

---

## 🚀 Benefits of Using Glue

- Serverless ETL (no infrastructure needed)
- Automatic schema detection
- Integration with Athena
- Supports large-scale data processing
- Works with Parquet for optimized queries

---

## ⚠️ Challenges & Solutions

| Issue | Solution |
|------|--------|
| JSON schema issues | Used Lambda preprocessing |
| Data type mismatch | Updated schema + reprocessed data |
| UTF encoding errors | Filtered specific regions |
| Slow queries | Used partitioning + Parquet |

---

## 🔐 IAM Role Used

| Role Name |
|----------|
| project-youtube-role-27 |

Permissions include:

- S3 access
- Glue execution
- Lambda integration

---

## 🏗️ Architecture Summary

```

S3 Raw Data
↓
Glue Crawler
↓
Glue Catalog
↓
Glue ETL Job
↓
S3 Clean Data (Parquet)
↓
Glue Studio (Join)
↓
S3 Analytics Layer

```

---

## 📊 Integration

Glue integrates with:

- Amazon S3 (storage)
- AWS Lambda (JSON processing)
- Amazon Athena (querying)
- Microsoft Fabric (analytics)

---

## 👨‍💻 Author

**Reddeppa Reddy Masireddy**  
Aspiring Data Engineer | Cloud & Data Enthusiast

