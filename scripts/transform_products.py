import psycopg2
import hashlib

def price_tier(price_inr):
    if price_inr < 500:
        return "cheap"
    elif price_inr < 1500:
        return "moderate"
    return "expensive"

def transform():
    conn = psycopg2.connect(
        host="postgres",
        dbname="airflow",
        user="airflow",
        password="airflow"
    )
    cur = conn.cursor()

    cur.execute("""
        SELECT gbp_to_inr FROM staging_exchange_rates
        ORDER BY rate_date DESC LIMIT 1
    """)
    rate = cur.fetchone()[0]

    cur.execute("TRUNCATE products")

    cur.execute("SELECT title, price_gbp, category, availability FROM raw_products")
    for title, price_gbp, category, availability in cur.fetchall():
        price_inr = round(price_gbp * rate, 2)
        availability_count = int("".join(filter(str.isdigit, availability)))
        tier = price_tier(price_inr)

        pid = hashlib.md5(f"{title}{category}{price_gbp}".encode()).hexdigest()

        cur.execute("""
            INSERT INTO products VALUES (%s,%s,%s,%s,%s,%s,%s,NOW())
        """, (
            pid,
            title.strip(),
            category.lower(),
            availability_count,
            price_gbp,
            price_inr,
            tier
        ))

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    transform()