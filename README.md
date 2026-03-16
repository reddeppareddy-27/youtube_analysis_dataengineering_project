

```markdown
# 🚀 End-to-End Data Engineering Project  
## YouTube Trending Data Analytics (AWS + Microsoft Fabric)

---

# 📌 Project Overview

This project demonstrates an **end-to-end data engineering pipeline** built using **AWS cloud services and Microsoft Fabric** to analyze **YouTube Trending Data**.

The goal of this project is to simulate a **real-world data engineering workflow** where raw datasets are ingested, processed, transformed into optimized formats, and integrated into an analytics platform for reporting and insights.

The project follows a **modern data lake architecture** and implements scalable **ETL pipelines** similar to those used in real-world data engineering environments.

---

# 🏗 Architecture

The system integrates **AWS for data engineering** and **Microsoft Fabric for analytics and reporting**.

### Data Flow

```

Source Data
↓
Amazon S3 (Data Lake)
↓
AWS Glue Crawlers (Schema Discovery)
↓
AWS Lambda (JSON Processing)
↓
AWS Glue ETL Jobs
↓
Parquet Data (Cleansed Layer)
↓
Microsoft Fabric Pipelines
↓
Fabric Lakehouse
↓
Power BI Dashboards

```

This architecture enables **scalable data ingestion, automated processing, and analytics-ready datasets**.

---

# ⚙️ Technologies Used

## AWS (Data Engineering Layer)

| Service | Purpose |
|-------|--------|
| Amazon S3 | Data Lake storage |
| AWS Glue | Data catalog, crawlers, ETL jobs |
| AWS Lambda | JSON preprocessing and transformation |
| Amazon Athena | SQL querying on S3 data |
| AWS IAM | Access management and security |
| Apache Parquet | Optimized columnar storage format |

---

## Microsoft Fabric (Analytics Layer)

| Service | Purpose |
|-------|--------|
| Fabric Pipelines | Data orchestration |
| Fabric Lakehouse | Central analytics storage |
| Fabric Notebooks | Data exploration |
| Power BI | Data visualization and reporting |

---

# 📂 Dataset

Dataset used:

**YouTube Trending Dataset (Kaggle)**

The dataset contains:

- Video statistics (CSV files)
- Video category metadata (JSON files)

Data fields include:

- Video ID
- Title
- Category
- Views
- Likes
- Comments
- Trending date
- Country

---

# 🔄 Data Pipeline Workflow

## 1️⃣ Data Ingestion

Raw datasets are downloaded from **Kaggle** and uploaded into an **Amazon S3 Data Lake**.

Example structure:

```

youtube-data-lake/

landing/
raw csv files
raw json files

cleansed/
parquet files

analytics/
aggregated datasets

```

The **Landing Layer** stores raw datasets without modifications.

---

# 2️⃣ Schema Discovery

**AWS Glue Crawlers** are used to:

- Scan S3 datasets
- Automatically detect schema
- Store metadata in **AWS Glue Data Catalog**

This allows the datasets to be easily queried using **Amazon Athena**.

---

# 3️⃣ Data Transformation

The dataset contains **semi-structured JSON files** with nested metadata.

To process these files:

- **AWS Lambda functions (Python)** are used
- JSON files are parsed and cleaned
- Data is converted into structured format

This step prepares the data for further ETL transformations.

---

# 4️⃣ ETL Processing

**AWS Glue ETL Jobs** perform data transformations such as:

- Joining video statistics with category metadata
- Cleaning and standardizing datasets
- Converting data into **Apache Parquet format**

Benefits of Parquet:

- Faster analytical queries
- Reduced storage usage
- Efficient columnar storage

---

# 5️⃣ Data Lake Architecture

The project follows a **three-layer data lake architecture**.

### Landing Layer
Stores raw datasets exactly as received.

### Cleansed Layer
Contains cleaned datasets stored in **Parquet format**.

### Analytics Layer
Contains aggregated datasets optimized for querying and reporting.

---

# 6️⃣ Cross-Cloud Data Integration

Processed data stored in **AWS S3** is integrated with **Microsoft Fabric**.

Using **Fabric Data Pipelines**:

- Data is ingested from S3
- Loaded into **Fabric Lakehouse**
- Prepared for analytics and reporting

---

# 7️⃣ Analytics & Reporting

The final datasets are stored in **Fabric Lakehouse**.

Using **Power BI within Microsoft Fabric**, dashboards were created to analyze:

- Trending video categories
- Country-wise trending patterns
- Engagement metrics (views, likes, comments)
- Video popularity trends

These dashboards help convert raw data into actionable insights.

---

# 📊 Example Insights

Some insights derived from the dataset include:

- Most trending YouTube categories by country
- Regional patterns in video popularity
- Engagement trends based on views and likes
- Category performance analysis

---

# 📁 Project Structure

```

youtube-data-engineering-project/

data/
raw datasets

lambda/
json_transformation_lambda.py

glue-jobs/
etl_transformation_script.py

fabric/
fabric_pipeline_configuration

queries/
athena_queries.sql

architecture/
architecture_diagram.png

README.md

```

---

# 🚀 Key Learning Outcomes

This project provided hands-on experience with:

- Designing **modern cloud data lake architectures**
- Building **serverless ETL pipelines**
- Processing **semi-structured JSON data**
- Optimizing datasets using **Apache Parquet**
- Implementing **cross-cloud data integration**
- Creating **analytics-ready data platforms**

The project helped simulate a **real-world data engineering workflow used in modern organizations**.

---

# 🔮 Future Improvements

Possible improvements include:

- Implement automated event-driven pipelines
- Add data quality validation
- Implement partitioning strategies
- Integrate Spark-based transformations
- Enhance dashboards with advanced analytics

---

# 👨‍💻 Author

**Reddeppa Reddy Masireddy**

Aspiring **Data Engineer | Data Analyst | Cloud & Data Enthusiast**

---

# ⭐ Support

If you found this project useful, consider giving this repository a **star ⭐**.
```

---

