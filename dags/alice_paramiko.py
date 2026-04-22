import paramiko
import pendulum
from airflow.sdk import DAG, task

with DAG(
    dag_id="alice_paramiko",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["alice"],
) as dag:

    @task()
    def hello_paramiko():
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        print("paramiko is installed")
