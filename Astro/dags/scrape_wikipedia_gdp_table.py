from airflow import DAG
from airflow.operators.python import PythonOperator
from pendulum import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_wikipedia_gdp_table():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table
    table = soup.find('table', {'class': 'wikitable'})

    # Parse the table
    df = pd.read_html(str(table))[0]
    
    # Save to CSV
    df.to_csv('C:/Users/Ars/Documents/countries_by_gdp.csv', index=False)
    print("Table saved to CSV")

default_args = {
    'owner': 'Astro',
    'retries': 3
}

with DAG(
    dag_id='wikipedia_gdp_scraping_dag',
    default_args=default_args,
    description='A simple DAG to scrape GDP table from Wikipedia and save to CSV',
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['example']
) as dag:
    
    scrape_task = PythonOperator(
        task_id='scrape_wikipedia_gdp_table',
        python_callable=scrape_wikipedia_gdp_table
    )

    scrape_task
