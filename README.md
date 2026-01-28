# Pricing Intelligence Pipeline

## Run
docker-compose up --build

Airflow UI: http://localhost:8080
admin / admin

## About
No description, website, or topics provided.
That’s it — which works, but it’s not descriptive and not interview-ready. 

✨ Improved README (ready to paste into your repo)
Here is a fully written README.md that explains your project, how it works, and why it matters:

# Pricing Intelligence Pipeline

This repository contains a **data engineering pipeline** built using **Apache Airflow**, **Python**, and **PostgreSQL** — designed to daily collect product data from the web, enrich it with currency exchange rates, transform it into analytics-ready format, and load it into a database for reporting.

---

## 💡 Project Overview

The goal of this project is to build a reliable and automated data pipeline that:

1. **Scrapes product listings** (title, price in GBP, category, availability) from a sample e-commerce site (`books.toscrape.com`).
2. **Fetches the daily GBP → INR exchange rate** using a public API.
3. **Stores the exchange rate in a staging table**, ensuring it's reusable for the day.
4. **Cleans and transforms product data**, including:
   - Text cleaning (trimming, normalization)
   - Parsing availability
   - Currency conversion using the stored exchange rate
   - Deriving price tiers (e.g., cheap/moderate/expensive)
   - Stable product ID generation via hashing
5. **Stores the transformed data into a final PostgreSQL table** for analytics.

The entire pipeline is orchestrated by an Airflow DAG that runs daily.

---

## 🚀 Architecture

The pipeline consists of the following:

| Layer | Component | Responsibility |
|------|------------|----------------|
| Extraction | `scrape_books.py` | Scrapes product data from the web |
| Staging | `fetch_exchange_rate.py` | Gets daily exchange rate and loads staging table |
| Transformation | `transform_products.py` | Applies cleaning, enrichment, and loads final table |
| Orchestration | `pricing_pipeline_dag.py` | Airflow DAG coordinating all tasks |
| Storage | PostgreSQL | Stores staging + final analytics tables |

---

## 🧱 Tables

The pipeline uses 3 main tables:

- **staging_exchange_rates** — holds daily GBP → INR exchange rate
- **raw_products** — (optional) stores raw scraped data
- **products** — transformed, cleaned data ready for reporting

---

## 📦 Tech Stack

| Technology | Purpose |
|------------|---------|
| Apache Airflow | Workflow orchestration |
| Python | Data extraction and transformation |
| PostgreSQL | Data storage |
| Docker & Docker Compose | Environment reproducibility |
| BeautifulSoup | Web scraping |
| Requests | HTTP requests |

---

## 🛠️ How to Run Locally

1. Clone this repo:
   ```bash
   git clone https://github.com/Manoj-B-S/Data-Engineering-Take-Home-Assignment
   cd Data-Engineering-Take-Home-Assignment
Build and start services:

docker-compose up --build
Access services:

Airflow UI: http://localhost:8080
Username: admin
Password: admin

Trigger the DAG manually or wait for the daily schedule.

🧪 Testing & Debugging
To test individual parts, run the Python scripts directly:

python scripts/scrape_books.py
python scripts/fetch_exchange_rate.py
python scripts/transform_products.py

## Run
docker-compose up --build

Airflow UI: http://localhost:8080
admin / admin
