from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data.weather import fetch_weather_raw

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="weather_api_pipeline",
    default_args=default_args,
    description="Fetch daily weather data and store in Postgres",
    schedule_interval="0 */4 * * *",  # every 4 hours
    start_date=datetime(2025, 9, 14),
    catchup=False,
    tags=["api", "weather", "pipeline"],
) as dag:
    fetch_weather = PythonOperator(
        task_id="fetch_weather",
        python_callable=fetch_weather_raw,
    )

    fetch_weather
