# 📊 Dataset Overview – YouTube Trending Videos

## 📌 Introduction

YouTube, one of the world’s most popular video-sharing platforms, maintains a list of **top trending videos** based on user engagement.

According to Variety magazine:

> “To determine the year’s top-trending videos, YouTube uses a combination of factors including measuring users interactions (number of views, shares, comments, and likes).”

⚠️ Note: These are **not necessarily the most viewed videos**, but those gaining rapid engagement.

---

## 🎯 Objective of Dataset

This dataset is used to analyze:

- What makes a video trend on YouTube  
- How user engagement impacts popularity  
- Regional differences in trending content  
- Content category performance  

---

## 📂 Dataset Description

This dataset contains **daily records of trending YouTube videos** across multiple countries.

### 🌍 Supported Regions

| Region Code | Country |
|------------|--------|
| US         | United States |
| GB         | Great Britain |
| DE         | Germany |
| CA         | Canada |
| FR         | France |
| RU         | Russia |
| MX         | Mexico |
| KR         | South Korea |
| JP         | Japan |
| IN         | India |

---

## 📅 Data Coverage

- Daily trending videos  
- Multiple months of data  
- Up to **200 trending videos per day per region**

---

## 📁 Data Structure

Each region has a separate CSV file.

### Example Files

```

USvideos.csv
GBvideos.csv
DEvideos.csv
CAvideos.csv
FRvideos.csv
INvideos.csv
JPvideos.csv
KRvideos.csv
MXvideos.csv
RUvideos.csv

```

---

## 🧾 Features (Columns)

| Column Name      | Description |
|-----------------|------------|
| video_id        | Unique identifier for video |
| title           | Title of the video |
| channel_title   | Name of the channel |
| publish_time    | Video publish timestamp |
| tags            | Video tags |
| views           | Number of views |
| likes           | Number of likes |
| dislikes        | Number of dislikes |
| comment_count   | Number of comments |
| description     | Video description |
| trending_date   | Date when video trended |
| category_id     | Category identifier |

---

## 🧩 Category Mapping

The dataset includes **JSON files** for each region that map `category_id` to actual category names.

### Example JSON Files

```

US_category_id.json
IN_category_id.json
GB_category_id.json

```

### Usage

- Join `category_id` from CSV  
- Map it to category name from JSON  

---

## 📊 Data Characteristics

- Structured Data → CSV files  
- Semi-Structured Data → JSON files  
- Multi-region dataset  
- High-volume engagement data  

---

## 🛠️ Data Source

- Collected using **YouTube API**

---

## 🔍 Use Cases

This dataset enables multiple types of analysis:

### 📈 Data Analysis

- Identify top-performing categories  
- Region-wise content trends  
- Engagement metrics (likes, views, comments)  

---

### 🤖 Machine Learning

- Predict video popularity  
- Build recommendation systems  
- Train NLP models on comments  

---

### 💬 Sentiment Analysis

- Analyze audience reactions  
- Study engagement patterns  

---

### 📊 Business Insights

- Optimize ad campaigns  
- Understand viral content patterns  
- Improve content strategy  

---

## 🚀 Example Questions Answered

- Which category trends most in each region?  
- What factors influence video popularity?  
- How do views relate to likes and comments?  
- Which regions have highest engagement?  

---

## ⚠️ Notes

- Category IDs differ by region  
- JSON files must be used for category mapping  
- Dataset is continuously updated  

---

## 📌 Summary

This dataset provides a **real-world, large-scale, multi-region dataset** ideal for:

- Data Engineering projects  
- Analytics dashboards  
- Machine Learning models  

It forms the foundation for building a **complete end-to-end data pipeline**, as implemented in this project.

---

## 👨‍💻 Author

**Reddeppa Reddy Masireddy**  
Aspiring Data Engineer | Cloud & Data Enthusiast

