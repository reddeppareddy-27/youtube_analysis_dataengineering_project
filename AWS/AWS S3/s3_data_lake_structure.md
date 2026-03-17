# 🗂️ S3 Data Lake Architecture

This project implements a **multi-layered Data Lake architecture on Amazon S3** for analyzing YouTube trending data.  
The data is organized into **Raw, Cleansed, and Analytics layers** following modern data engineering best practices.

---

# 🧱 Data Lake Layers

## 🔹 1. Raw Layer

Stores **original unprocessed data** directly from Kaggle.

**S3 Bucket:**
s3://project-youtube-s3-input-raw-dev-27/

### 📂 Structure

aws/

├── data/
│   ├── CA_category_id.json
│   ├── DE_category_id.json
│   ├── FR_category_id.json
│   ├── GB_category_id.json
│   ├── IN_category_id.json
│   ├── JP_category_id.json
│   ├── KR_category_id.json
│   ├── MX_category_id.json
│   ├── RU_category_id.json
│   └── US_category_id.json

└── raw_data/
    ├── region=ca/   (Canada)
    │   └── CAvideos.csv
    ├── region=de/   (Germany)
    │   └── DEvideos.csv
    ├── region=fr/   (France)
    │   └── FRvideos.csv
    ├── region=gb/   (United Kingdom)
    │   └── GBvideos.csv
    ├── region=in/   (India)
    │   └── INvideos.csv
    ├── region=jp/   (Japan)
    │   └── JPvideos.csv
    ├── region=kr/   (South Korea)
    │   └── KRvideos.csv
    ├── region=mx/   (Mexico)
    │   └── MXvideos.csv


---

## 🔹 2. Cleansed Layer

Stores **processed and transformed data** in **Apache Parquet format**.

**S3 Bucket:**
s3://cleaned-youtube-data-27/youtube/

### 📂 JSON → Parquet Output

029ee4b1529e4302943ec6df8636f7cb.snappy.parquet  
27ad4c5727cf44e68b78581e6503db5d.snappy.parquet  
515416b34da1409683adb9dfc7506ca1.snappy.parquet  
5c1b2ee627ed4c82a5e5ec2328be3f91.snappy.parquet  
6d0c2599f55c493dab0bc3176fac31de.snappy.parquet  
716818dc7e744c49007c2540378706f0.snappy.parquet  
96d13ae4f132404292df300371ad9a14.snappy.parquet  
b908c88efef441f4a67956bf6a93b028.snappy.parquet  
c2618366ef5545688673a3f9d69df090.snappy.parquet  
d7478c3944694fe12bd2f978413b5489.snappy.parquet  

### 📂 CSV → Parquet (Partitioned by Region)

raw_statistics/

├── region=ca/
│   └── part-00000.snappy.parquet
├── region=de/
│   └── part-00001.snappy.parquet
├── region=fr/
│   └── part-00004.snappy.parquet
├── region=gb/
│   └── part-00003.snappy.parquet
├── region=in/
│   └── part-00002.snappy.parquet
├── region=jp/
│   └── part-00007.snappy.parquet
├── region=kr/
│   └── part-00006.snappy.parquet
├── region=mx/
│   └── part-00005.snappy.parquet



## 🔹 3. Analytics Layer

Stores **final reporting-ready datasets** optimized for querying.

**S3 Bucket:**
s3://youtube-analytics-bucket-27/

### 📂 Structure

youtube/

├── region=ca/
│   ├── category_id=1/
│   ├── category_id=10/
│   ├── category_id=15/
│   ├── category_id=17/
│   ├── category_id=19/
│   ├── category_id=2/
│   ├── category_id=20/
│   ├── category_id=22/
│   ├── category_id=23/
│   ├── category_id=24/
│   ├── category_id=25/
│   └── category_id=26/

├── region=de/
├── region=fr/
├── region=gb/
├── region=in/
├── region=jp/
├── region=kr/
├── region=mx/



---

# 🔄 Data Flow Summary

Kaggle Dataset  
↓  
AWS S3 (Raw Layer)  
↓  
AWS Lambda (JSON Processing)  
↓  
AWS Glue ETL (CSV Processing)  
↓  
S3 Cleansed Layer (Parquet)  
↓  
AWS Glue Studio (Join & Transform)  
↓  
S3 Analytics Layer  
↓  
Microsoft Fabric Lakehouse  
↓  
Power BI Dashboard  

---

# ⚡ Key Features

- Multi-layer Data Lake Architecture  
- Partitioning by `region` and `category_id`  
- JSON → Parquet transformation using Lambda  
- CSV → Parquet transformation using Glue ETL  
- Optimized for Athena querying  
- Cross-cloud integration with Microsoft Fabric  

---

# 👨‍💻 Author

**Reddeppa Reddy Masireddy**  
Aspiring Data Engineer | Cloud & Data Enthusiast