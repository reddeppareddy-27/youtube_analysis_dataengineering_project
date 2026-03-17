
# 📊 AWS Athena SQL Queries – YouTube Analytics

## 📌 Overview

This document contains advanced SQL queries to analyze YouTube trending data using **Amazon Athena** and the **AWS Glue Data Catalog**.

All queries run against the final analytics table in the Glue Data Catalog.

---

## 📍 Table Reference

**Catalog:** `AwsDataCatalog`  
**Database:** `db_youtube_analytics`  
**Table:** `final-anaytics-youtube-27`

---

## 🚀 Advanced SQL Queries

---

# 1️⃣ Top Trending Categories by Region

```sql
SELECT 
    region,
    category_id,
    COUNT(*) AS total_videos
FROM "AwsDataCatalog"."db_youtube_analytics"."final-anaytics-youtube-27"
GROUP BY region, category_id
ORDER BY region, total_videos DESC;
```

---

# 2️⃣ Most Popular Categories (Views)

```sql
SELECT 
    category_id,
    SUM(views) AS total_views
FROM "AwsDataCatalog"."db_youtube_analytics"."final-anaytics-youtube-27"
GROUP BY category_id
ORDER BY total_views DESC
LIMIT 10;
```

---

# 3️⃣ Engagement Rate (Likes / Views)

```sql
SELECT 
    title,
    views,
    likes,
    ROUND((likes * 1.0 / views), 4) AS engagement_rate
FROM "AwsDataCatalog"."db_youtube_analytics"."final-anaytics-youtube-27"
WHERE views > 100000
ORDER BY engagement_rate DESC
LIMIT 10;
```

---

# 4️⃣ Top Videos by Likes per Region (Window Function)

```sql
SELECT *
FROM (
    SELECT 
        region,
        title,
        views,
        likes,
        ROW_NUMBER() OVER (PARTITION BY region ORDER BY likes DESC) AS rank
    FROM "AwsDataCatalog"."db_youtube_analytics"."final-anaytics-youtube-27"
) t
WHERE rank <= 5;
```

---

# 5️⃣ Category Performance (Avg Views)

```sql
SELECT 
    category_id,
    COUNT(*) AS total_videos,
    AVG(views) AS avg_views
FROM "AwsDataCatalog"."db_youtube_analytics"."final-anaytics-youtube-27"
GROUP BY category_id
ORDER BY avg_views DESC;
```

---

# 6️⃣ Top Channels by Total Views

```sql
SELECT 
    channel_title,
    SUM(views) AS total_views
FROM "AwsDataCatalog"."db_youtube_analytics"."final-anaytics-youtube-27"
GROUP BY channel_title
ORDER BY total_views DESC
LIMIT 5;
```

---

# 7️⃣ Daily Trending Count

```sql
SELECT 
    trending_date,
    COUNT(*) AS total_trending_videos
FROM "AwsDataCatalog"."db_youtube_analytics"."final-anaytics-youtube-27"
GROUP BY trending_date
ORDER BY trending_date;
```

---

# 8️⃣ Viral Videos Detection

```sql
SELECT 
    title,
    views,
    likes,
    comment_count,
    (views + likes + comment_count) AS total_engagement
FROM "AwsDataCatalog"."db_youtube_analytics"."final-anaytics-youtube-27"
ORDER BY total_engagement DESC
LIMIT 10;
```

---

# 9️⃣ Category Ranking by Likes (Window Function)

```sql
SELECT *
FROM (
    SELECT 
        category_id,
        AVG(likes) AS avg_likes,
        RANK() OVER (ORDER BY AVG(likes) DESC) AS rank
    FROM "AwsDataCatalog"."db_youtube_analytics"."final-anaytics-youtube-27"
    GROUP BY category_id
) t;
```

---

# 🔟 Region-wise Performance

```sql
SELECT 
    region,
    AVG(views) AS avg_views,
    AVG(likes) AS avg_likes,
    AVG(comment_count) AS avg_comments
FROM "AwsDataCatalog"."db_youtube_analytics"."final-anaytics-youtube-27"
GROUP BY region
ORDER BY avg_views DESC;
```

---

# 1️⃣1️⃣ Top Category per Region (ADVANCED)

```sql
SELECT *
FROM (
    SELECT 
        region,
        category_id,
        COUNT(*) AS total_videos,
        RANK() OVER (PARTITION BY region ORDER BY COUNT(*) DESC) AS rank
    FROM "AwsDataCatalog"."db_youtube_analytics"."final-anaytics-youtube-27"
    GROUP BY region, category_id
) t
WHERE rank = 1;
```

---

# 1️⃣2️⃣ Above Average Videos (Subquery)

```sql
SELECT 
    title,
    views
FROM "AwsDataCatalog"."db_youtube_analytics"."final-anaytics-youtube-27"
WHERE views > (
    SELECT AVG(views)
    FROM "AwsDataCatalog"."db_youtube_analytics"."final-anaytics-youtube-27"
);
```

---

# 1️⃣3️⃣ Engagement Distribution by Category

```sql
SELECT 
    category_id,
    SUM(likes) AS total_likes,
    SUM(comment_count) AS total_comments
FROM "AwsDataCatalog"."db_youtube_analytics"."final-anaytics-youtube-27"
GROUP BY category_id
ORDER BY total_likes DESC;
```

---

# 🔥 BONUS – Like/View Ratio (VERY IMPORTANT)

```sql
SELECT 
    category_id,
    AVG(views) AS avg_views,
    AVG(likes) AS avg_likes,
    AVG(likes * 1.0 / views) AS like_view_ratio
FROM "AwsDataCatalog"."db_youtube_analytics"."final-anaytics-youtube-27"
GROUP BY category_id
ORDER BY like_view_ratio DESC;
```

---

## 📌 How to Use These Queries

1. **Open Amazon Athena Console**
2. **Select Database:** `db_youtube_analytics`
3. **Copy & Paste** any query from above
4. **Execute** and view results
5. **Export** results as CSV or Parquet

---

## 🎯 Query Categories

| Category | Queries | Purpose |
|----------|---------|---------|
| **Trending Analysis** | #1, #7 | Find trending categories and videos by date |
| **Engagement Metrics** | #3, #13, #14 | Analyze likes, views, and comments |
| **Regional Performance** | #10, #11 | Compare metrics across regions |
| **Window Functions** | #4, #9, #11 | Advanced ranking and partitioning |
| **Performance Optimization** | #5, #6 | Category and channel analysis |

---

## 💡 Key Insights You Can Derive

✅ Most trending categories by region  
✅ Engagement rates across videos  
✅ Channel performance metrics  
✅ Viral content detection  
✅ Category-wise trends  
✅ Regional content preferences  
✅ Like-to-view ratios for content strategy  

---

## 👨‍💻 Author

**Reddeppa Reddy Masireddy**  
Aspiring Data Engineer | Cloud & Data Enthusiast

