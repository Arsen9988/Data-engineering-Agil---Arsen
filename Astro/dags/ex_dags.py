

from airflow.decorators import dag, task
from pendulum import datetime

@dag(
    start_date=datetime(2024, 1, 1),
    schedule="*/1 * * * *",
    catchup=False,
    doc_md=__doc__,
    default_args={"owner": "Astro", "retries": 3},
    tags=["example"],
)
def ex_dugs():

    @task
    def hello_world():
        print("Heffffffffffffffffffhjll")
    
    hello_world()

ex_dugs()
