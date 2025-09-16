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


