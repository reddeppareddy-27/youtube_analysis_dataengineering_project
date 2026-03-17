# 🗄️ Amazon Athena – Query Layer

## 📌 Overview

Amazon Athena is used in this project as a **serverless query engine** to analyze data directly from **Amazon S3**.

It enables running **SQL queries on large datasets** without managing any infrastructure.

Athena works on top of the **AWS Glue Data Catalog**, which provides metadata about the datasets.

---

## 🧾 Athena Role in Project

| Function                | Description |
|------------------------|------------|
| Query Engine           | Executes SQL queries on S3 data |
| Data Exploration       | Analyze raw and processed datasets |
| Validation             | Validate ETL outputs |
| Reporting              | Query analytics layer for dashboards |

---

## 🏗️ Athena Workflow

```

S3 Data Lake
↓
Glue Data Catalog
↓
Amazon Athena
↓
SQL Queries
↓
Insights / Dashboard (Microsoft Fabric / Power BI)

```

---

## 📂 Databases Used

| Database Name            | Description |
|-------------------------|------------|
| de_youtube_raw          | Contains raw CSV data tables |
| de_youtube_clean        | Contains cleaned JSON + Parquet data |
| de_youtube_analytics    | Contains final reporting dataset |

---

## 📊 Tables in Athena

| Table Name             | Layer        | Description |
|----------------------|-------------|------------|
| raw_statistics       | Raw          | CSV video data |
| clean_category_data  | Cleansed     | JSON category metadata |
| final_analytics      | Analytics    | Joined and processed dataset |

---

## 🔍 Example Queries

### 1️⃣ Basic Data Preview

```sql
SELECT *
FROM de_youtube_clean.clean_category_data
LIMIT 10;
```

---

### 2️⃣ Join Query (CSV + JSON)

```sql
SELECT
    a.title,
    a.category_id,
    b.snippet_title
FROM de_youtube_raw.raw_statistics a
JOIN de_youtube_clean.clean_category_data b
ON CAST(a.category_id AS INT) = CAST(b.id AS INT);
```

---

### 3️⃣ Filter by Region

```sql
SELECT *
FROM de_youtube_raw.raw_statistics
WHERE region = 'ca';
```

---

### 4️⃣ Aggregation Query

```sql
SELECT
    category_id,
    COUNT(*) AS total_videos
FROM de_youtube_analytics.final_analytics
GROUP BY category_id
ORDER BY total_videos DESC;
```

---

## ⚡ Query Optimization Techniques

| Technique          | Description                           |
| ------------------ | ------------------------------------- |
| Partitioning       | Data partitioned by `region`          |
| Columnar Format    | Used Parquet for faster queries       |
| Reduced Scans      | Queries scan only required partitions |
| Precomputed Tables | Analytics layer avoids repeated joins |

---

## 📂 S3 Query Output Location

Athena stores query results in S3.

| Parameter     | Value                            |
| ------------- | -------------------------------- |
| Output Bucket | s3://athena-query-results-bucket |
| Format        | CSV                              |
| Usage         | Stores query execution results   |

---

## ⚠️ Challenges & Solutions

| Issue              | Solution                      |
| ------------------ | ----------------------------- |
| JSON parsing error | Preprocessed using Lambda     |
| Data type mismatch | Used CAST / Schema correction |
| Slow queries       | Implemented partitioning      |
| Large scans        | Used Parquet format           |

---

## 🔐 Permissions Required

Athena uses IAM role with access to:

| Service | Permission          |
| ------- | ------------------- |
| S3      | Read/Write data     |
| Glue    | Access Data Catalog |
| Athena  | Execute queries     |

---

## 🚀 Benefits of Using Athena

* Serverless (no infrastructure)
* Pay-per-query model
* Direct integration with S3
* Supports standard SQL
* Fast querying with Parquet + partitions

---

## 🏗️ Architecture Summary

```
S3 Raw Data
     ↓
Glue Catalog
     ↓
Athena Queries
     ↓
Processed Insights
     ↓
Microsoft Fabric / Power BI Dashboard
```

---

## 🔗 Integration in Project

Athena integrates with:

* AWS Glue (metadata)
* Amazon S3 (storage)
* AWS Lambda (preprocessing)
* Microsoft Fabric (analytics layer)

---

## 👨‍💻 Author

**Reddeppa Reddy Masireddy**  
Aspiring Data Engineer | Cloud & Data Enthusiast


