import os

import pendulum
from airflow.providers.amazon.aws.hooks.ses import SesHook
from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import dag

dag_id = os.path.basename(__file__).replace(".py", "")


def send_ses_notification(context):
    ses_hook = SesHook(aws_conn_id="aws_default")
    ses_hook.send_email(
        to=["alice@example.com"],
        subject=f"Task Failed: {context['dag'].dag_id} - {context['task'].task_id}",
        html_content=f"Task {context['task'].task_id} failed in DAG {context['dag'].dag_id}",
        mail_from="airflow@airflow.example.com",
    )


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": pendulum.today() - pendulum.duration(2),
    "retries": 0,
}


def hello_world(x):
    print(f"hello {x}")
    # This should always fail
    assert True == False


@dag(
    dag_id=dag_id,
    default_args=default_args,
    tags=["alice"],
    schedule=None,
    max_active_runs=1,
    catchup=False,
)
def alice_test_broken_dag():
    print("hi alice")
    hello = PythonOperator(
        task_id="hello",
        python_callable=hello_world,
        op_kwargs={"x": "world"},
        on_failure_callback=[send_ses_notification],
    )
    hello


alice_test_broken_dag()
