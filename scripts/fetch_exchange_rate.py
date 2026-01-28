import requests
import psycopg2
from datetime import date

def fetch_rate():
    url = "https://api.exchangerate.host/latest?base=GBP&symbols=INR"
    rate = requests.get(url).json()["rates"]["INR"]

    conn = psycopg2.connect(
        host="postgres",
        dbname="airflow",
        user="airflow",
        password="airflow"
    )
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO staging_exchange_rates (rate_date, gbp_to_inr)
        VALUES (%s, %s)
        ON CONFLICT (rate_date)
        DO UPDATE SET gbp_to_inr = EXCLUDED.gbp_to_inr
    """, (date.today(), rate))

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    fetch_rate()