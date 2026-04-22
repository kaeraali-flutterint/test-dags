import pendulum
from airflow.sdk import DAG, task

with DAG(
    dag_id="alice_test_dag",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["alice"],
) as dag:

    @task()
    def hello_world():
        print("hello world")
