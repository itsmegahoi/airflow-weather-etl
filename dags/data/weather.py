import requests
from datetime import datetime
from airflow.providers.postgres.hooks.postgres import PostgresHook
import json
from dotenv import load_dotenv
import os

load_dotenv()


def fetch_weather_raw():
    api_key = os.getenv("API_KEY")
    city = os.getenv("CITY")
    base_url = os.getenv("BASE_URL")

    URL = f"{base_url}?q={city}&appid={api_key}&units=metric"

    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4))
    else:
        print(
            f"Failed to fetch data. Status code: {response.status_code}, Response: {response.text}"
        )

    fetch_raw_data = (
        city,
        data["sys"]["country"],
        data["id"],
        data["weather"][0]["main"],
        data["weather"][0]["description"],
        data["main"]["temp_min"],
        data["main"]["temp_max"],
        data["main"]["humidity"],
        datetime.now(),
    )

    # Use the connection we created in Airflow UI
    hook = PostgresHook(postgres_conn_id="postgres_openweather")
    conn = hook.get_conn()
    cur = conn.cursor()

    cur.execute(
        """INSERT INTO weather_data (city, country_code, id, weather, description, min_temp, max_temp, humidity, timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        fetch_raw_data,
    )

    conn.commit()
    cur.close()
    conn.close()
    print(f"Inserted record: {fetch_raw_data}")


if __name__ == "__main__":
    fetch_weather_raw()
