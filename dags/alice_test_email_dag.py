import os

from airflow.providers.smtp.operators.smtp import EmailOperator
from airflow.sdk import dag
from pendulum import datetime

dag_id = os.path.basename(__file__).replace(".py", "")

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2021, 1, 1, tz="UTC"),
    "retries": 1,
}


@dag(
    dag_id=dag_id,
    default_args=default_args,
    schedule=None,
    tags=["alice"],
    max_active_runs=1,
    catchup=False,
)
def alice_test_email_dag():
    print("hi alice")
    email_alice = EmailOperator(
        task_id="email_alice",
        to="alice@example.com",
        subject="hello alice",
        html_content="hello alice",
    )

    email_alice


alice_test_email_dag()
