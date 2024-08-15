

from airflow.decorators import dag, task
from pendulum import datetime

@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",      #"*/1 * * * *" every minute
    catchup=False,
    doc_md=__doc__,
    default_args={"owner": "Astro", "retries": 3},
    tags=["example"],
)
def ex_dugs():

    @task
    def hello_world():
        print("Hello World")
    
    hello_world()

ex_dugs()
