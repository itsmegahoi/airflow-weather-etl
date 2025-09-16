# 🌦️ Weather Data Pipeline with Apache Airflow

This project demonstrates a **data engineering pipeline** built with **Apache Airflow** that fetches real-time weather data from the [OpenWeather API](https://openweathermap.org/api) and stores it into a **PostgreSQL** database.  

The DAG is scheduled to run **every 4 hours**
---

## ⚙️ Features
- ⏱️ **Scheduled DAG** runs every 4 hours automatically  
- 🌍 **Fetch weather data** from OpenWeather API  
- 🗄️ **Store data in PostgreSQL** using Airflow’s PostgresHook  
- 🔄 **Retries enabled** (if API fails)  
- 📊 Designed to be extended with dbt/Power BI for analytics  

## 📸 Screenshots

- **Airflow DAG successfully executed** – The pipeline fetched weather data and stored it into Postgres as expected. 
<img width="750" height="344" alt="image" src="https://github.com/user-attachments/assets/3f6ec5f5-625b-4754-b9f7-7688b77d8236" />

- **Scheduled DAG runs** – Demonstrates how the pipeline automatically triggers every 4 hours as per the configured schedule.
  <img width="620" height="612" alt="image" src="https://github.com/user-attachments/assets/fc6ad2ff-6126-4343-b6d6-d3ad7fb65139" />

- **Postgres table output (optional)** – A snapshot of the weather data stored in the database for analytics use. It is also rows from the manual test runs.
  <img width="1506" height="829" alt="image" src="https://github.com/user-attachments/assets/d66f3f71-39f9-4d73-bda1-a43a5e344fc4" />

