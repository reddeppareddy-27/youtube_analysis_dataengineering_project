# 🏗️ Microsoft Fabric Lakehouse – Analytics Layer

## 📌 Overview

In this project, **Microsoft Fabric Lakehouse** is used as the final analytics layer to perform:

- Data exploration  
- Querying  
- Dashboard creation  

The data is imported from **AWS S3 (Analytics Layer)** into Fabric for visualization and reporting.

---

## 🔗 Integration Flow

```

AWS S3 (Analytics Layer)
↓
Microsoft Fabric Lakehouse
↓
Tables (Structured Data)
↓
SQL / Notebook Analysis
↓
Dashboard (Power BI / Fabric)

```

---

## 📂 Data Source

| Source Type | Location |
|------------|---------|
| Cloud Storage | AWS S3 |
| Bucket | youtube-analytics-bucket-27 |
| Data Format | Parquet |
| Partitioning | region, category_id |

---

## 📥 Data Import into Fabric

### 🔹 Step 1: Connect to AWS S3

- Open **Microsoft Fabric Workspace**
- Navigate to **Lakehouse**
- Click on **Get Data**
- Select **Amazon S3**

---

### 🔹 Step 2: Provide Connection Details

| Parameter        | Value |
|----------------|------|
| Access Key      | AWS Access Key |
| Secret Key      | AWS Secret Key |
| Bucket Name     | youtube-analytics-bucket-27 |
| File Format     | Parquet |

---

### 🔹 Step 3: Load Data

- Selected **Analytics Layer Parquet Files**
- Imported into **Lakehouse Tables**
- Created table:

```

youtube_analytics

```

---

## 📊 Lakehouse Structure

```

Lakehouse
│
├── Tables
│   └── youtube_analytics
│
└── Files
└── youtube-analytics-bucket/
├── region=ca/
├── region=de/
├── region=fr/
├── region=gb/
├── region=in/
├── region=jp/
├── region=kr/
├── region=mx/

```

---

## 🧾 Table Schema (Sample)

| Column Name     | Description |
|----------------|------------|
| video_id       | Unique video identifier |
| title          | Video title |
| channel_title  | Channel name |
| category_id    | Video category |
| region         | Country code |
| views          | Total views |
| likes          | Total likes |
| comment_count  | Number of comments |
| trending_date  | Trending date |

---

## ⚙️ Operations Performed

### 🔹 1. Data Validation

- Verified row count  
- Checked null values  
- Ensured schema consistency  

---

### 🔹 2. Data Exploration

- Viewed table data inside Fabric  
- Filtered by region and category  
- Checked trending patterns  

---

### 🔹 3. Query Execution

Used SQL inside Fabric:

```sql
SELECT 
    region,
    category_id,
    SUM(views) AS total_views
FROM youtube_analytics
GROUP BY region, category_id
ORDER BY total_views DESC;
```

---

### 🔹 4. Aggregations

* Total views per category
* Average likes per region
* Engagement metrics

---

### 🔹 5. Partition Optimization

* Data already partitioned in S3
* Fabric automatically leverages partitions
* Faster query performance

---

## 📈 Visualization

* Connected Lakehouse table to **Power BI**
* Created dashboards:

### Example Insights:

* Most popular category → Music
* Highest engagement region → Germany
* Trending patterns by region

---

## 🚀 Benefits of Using Fabric

| Feature                | Benefit                 |
| ---------------------- | ----------------------- |
| Lakehouse Architecture | Unified data platform   |
| Direct S3 Integration  | No data duplication     |
| Built-in SQL Engine    | Easy querying           |
| Power BI Integration   | Fast dashboard creation |
| Scalable               | Handles large datasets  |

---

## ⚠️ Challenges & Solutions

| Issue              | Solution                    |
| ------------------ | --------------------------- |
| Connection errors  | Verified AWS credentials    |
| Schema mismatch    | Ensured Parquet consistency |
| Slow queries       | Used partitioned data       |
| Data format issues | Used Parquet instead of CSV |

---

## 🏗️ Final Architecture

```
AWS S3 (Analytics Layer)
        ↓
Microsoft Fabric Lakehouse
        ↓
SQL Queries / Notebooks
        ↓
Power BI Dashboard
```

---

## 📌 Summary

* Imported final processed data from AWS S3
* Built structured tables in Fabric Lakehouse
* Performed SQL-based analysis
* Created dashboards for business insights

This completes the **end-to-end data engineering pipeline** from ingestion to visualization.

---

## 👨‍💻 Author

**Reddeppa Reddy Masireddy**  
Aspiring Data Engineer | Cloud & Data Enthusiast
