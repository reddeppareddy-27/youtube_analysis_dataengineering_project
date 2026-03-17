# 🔐 IAM Role Configuration

## 📌 Overview

This project uses AWS Identity and Access Management (IAM) to securely manage access between AWS services such as:

- Amazon S3
- AWS Glue
- AWS Lambda
- Amazon Athena

A dedicated IAM role is created to allow these services to interact securely and perform ETL operations.

---

## 🧾 IAM Role Details

| Attribute                | Value                                |
|------------------------|--------------------------------------|
| Role Name              | project-youtube-role-27              |
| Purpose                | Enable AWS services to access resources |
| Created On             | March 13, 2026                       |
| Max Session Duration   | 1 Hour                               |
| ARN                    | arn:aws:iam::61054022402:role/project-youtube-role-27 |

---



## 🛠️ Attached Policies

| Policy Name                | Type         | Description                                      |
|---------------------------|-------------|--------------------------------------------------|
| AmazonS3FullAccess        | AWS Managed | Full access to S3 buckets                        |
| AWSGlueConsoleFullAccess  | AWS Managed | Full access to AWS Glue console                  |
| AWSGlueServiceRole        | AWS Managed | Allows Glue to interact with AWS services        |
| AWSLambda_FullAccess      | AWS Managed | Full access to AWS Lambda                        |
| AWSLambdaExecute          | AWS Managed | Allows Lambda to access S3 and CloudWatch logs   |

---

## 🔑 Permissions Breakdown

| Service        | Permissions                                                                 |
|----------------|------------------------------------------------------------------------------|
| Amazon S3      | Read raw data, write processed data (clean & analytics layers)              |
| AWS Glue       | Run crawlers, execute ETL jobs, manage Data Catalog                         |
| AWS Lambda     | Execute functions, process JSON data, access S3                             |
| Amazon Athena  | Query data stored in S3 via Glue Catalog                                    |

---

## 🔄 Role Usage in Project

| Component       | Usage Description |
|-----------------|------------------|
| AWS Glue        | Used for Crawlers and ETL jobs to read/write data from S3 |
| AWS Lambda      | Used for JSON → Parquet transformation and automation     |
| Amazon Athena   | Uses Glue Catalog to query processed data                |

---

## 🏗️ Role Architecture

```

AWS Services
↓
IAM Role (project-youtube-role-27)
↓
Permissions:

* S3 Access
* Glue Access
* Lambda Access
  ↓
  Data Engineering Pipeline

```

---

## ⚠️ Security Best Practices

- Do not use root account for daily operations  
- Use IAM roles instead of hardcoded credentials  
- Follow least privilege principle (in production)  
- Rotate access keys periodically  
- Never expose secret keys  

---

## 🚀 Key Highlights

- Centralized access control across AWS services  
- Enables secure service-to-service communication  
- Supports serverless data engineering pipeline  
- Simplifies permission management  

---

## 👨‍💻 Author

**Reddeppa Reddy Masireddy**  
Aspiring Data Engineer | Cloud & Data Enthusiast


