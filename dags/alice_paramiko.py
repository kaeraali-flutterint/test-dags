import paramiko
from airflow.sdk import DAG, task
from pendulum import datetime

with DAG(
    dag_id="alice_paramiko",
    schedule=None,
    start_date=datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["alice"],
) as dag:

    @task()
    def hello_paramiko():
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        print("paramiko is installed")


if __name__ == "__main__":
    dag.test()
