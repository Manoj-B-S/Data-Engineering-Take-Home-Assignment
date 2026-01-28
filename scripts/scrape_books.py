import requests
from bs4 import BeautifulSoup
import psycopg2

URL = "http://books.toscrape.com/catalogue/category/books_1/index.html"

def scrape():
    conn = psycopg2.connect(
        host="postgres",
        dbname="airflow",
        user="airflow",
        password="airflow"
    )
    cur = conn.cursor()
    cur.execute("TRUNCATE raw_products")

    res = requests.get(URL)
    soup = BeautifulSoup(res.text, "html.parser")

    books = soup.select(".product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = float(book.select_one(".price_color").text.replace("£", ""))
        availability = book.select_one(".availability").text.strip()
        category = "Books"

        cur.execute(
            "INSERT INTO raw_products VALUES (%s, %s, %s, %s, NOW())",
            (title, price, category, availability)
        )

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    scrape()