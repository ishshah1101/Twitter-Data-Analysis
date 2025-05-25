# 🛠️ Twitter Data Engineering Pipeline

An end-to-end data pipeline that extracts real-time tweets using the Twitter API, transforms and validates the data using Python, orchestrates the workflow via Apache Airflow, and loads it into AWS S3 — all deployed on an EC2 instance. Designed for scalable ingestion and monitoring of social media analytics.

## 🚀 Overview

This project automates the extraction, transformation, and loading (ETL) of Twitter data for downstream analytics. It leverages cloud infrastructure (AWS EC2 & S3) and open-source tools (Apache Airflow, Tweepy) to ensure a reliable and scalable data pipeline.

## 🔧 Tech Stack

- **Python** – Data extraction, transformation, and validation
- **Twitter API (Tweepy)** – Real-time tweet streaming
- **Apache Airflow** – Workflow orchestration and scheduling
- **AWS EC2** – Hosting and execution environment
- **AWS S3** – Data storage layer
- **Boto3** – Python SDK for AWS services
- **Pandas** – Data wrangling


## 🔄 ETL Workflow

1. **Extract**: Fetch tweets using Tweepy and store as raw JSON.
2. **Transform**: Parse and clean tweet data (text, timestamp, hashtags, etc.).
3. **Load**: Upload transformed data to an S3 bucket in `.csv` format.
4. **Schedule**: Run pipeline daily/hourly using Apache Airflow DAG.
5. **Monitor**: Track task success/failure using the Airflow web UI.

## 📦 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/twitter-etl-pipeline.git
   cd twitter-etl-pipeline


