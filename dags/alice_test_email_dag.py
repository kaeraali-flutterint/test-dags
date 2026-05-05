import os

import pendulum
from airflow.providers.smtp.operators.smtp import EmailOperator
from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import dag

dag_id = os.path.basename(__file__).replace(".py", "")

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": pendulum.today() - pendulum.duration(2),
    "retries": 1,
}


def hello_world(x):
    return "Hello " + x


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
    hello = PythonOperator(
        task_id="hello",
        python_callable=hello_world,
        op_kwargs={"x": "world"},
    )
    email_alice = EmailOperator(
        task_id="email_alice",
        to="alice@example.com",
        subject="hello alice",
        html_content="hello alice",
    )

    hello.set_downstream(email_alice)


alice_test_email_dag()
