from airflow.sdk import DAG, task
from pendulum import datetime

with DAG(
    dag_id="alice_test_dag",
    schedule=None,
    start_date=datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["alice"],
) as dag:

    @task()
    def hello_world():
        print("hello world")
