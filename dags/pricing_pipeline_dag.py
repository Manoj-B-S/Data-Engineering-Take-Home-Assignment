from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "start_date": datetime(2024, 1, 1),
    "retries": 2
}

with DAG(
    "pricing_intelligence_pipeline",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False
) as dag:

    scrape = BashOperator(
        task_id="scrape_products",
        bash_command="python /opt/airflow/scripts/scrape_books.py"
    )

    exchange = BashOperator(
        task_id="fetch_exchange_rate",
        bash_command="python /opt/airflow/scripts/fetch_exchange_rate.py"
    )

    transform = BashOperator(
        task_id="transform_and_load",
        bash_command="python /opt/airflow/scripts/transform_products.py"
    )

    [scrape, exchange] >> transform