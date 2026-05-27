from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from airflow.sdk import dag, task
from pendulum import datetime

# it's generally bad to set constants like this because this code gets run every 30 seconds
# however this also makes it a lot easier to test this DAG
BUCKET = "alice_test_dags"


@dag(
    description="DAG in charge of processing S3 data",
    start_date=datetime(2021, 1, 1),
    # ordinarily this would run shortly after midnight and wait for the partner to send their daily reports
    # schedule="@daily",
    schedule="None",
    catchup=False,
    tags=["alice"],
)
def alice_s3_processor():

    # Wait for any files named *.txt to land in the root of the bucket
    waiting_for_data = S3KeySensor(
        task_id="waiting_for_data",
        bucket_name=BUCKET,
        bucket_key=".+txt",
        use_regex=True,
        mode="reschedule",
        timeout=60 * 5,
    )

    @task
    def list_objects():
        """
        list objects in the s3 bucket matching *.txt
        """
        from airflow.providers.amazon.aws.hooks.s3 import S3Hook

        s3_hook = S3Hook(aws_conn_id="aws_default")
        files = s3_hook.list_keys(BUCKET)
        data_files = [file for file in files if file.endswith(".txt")]
        return data_files

    @task
    def process_object(filename):
        """
        print (log) the contents of an object in the bucket
        """
        from airflow.providers.amazon.aws.hooks.s3 import S3Hook

        s3_hook = S3Hook(aws_conn_id="aws_default")
        file = s3_hook.read_key(key=filename, bucket_name=BUCKET)
        print(file)

    # wait for the data, get a list of objects, dynamically run process_object for each object found
    waiting_for_data >> process_object.expand(filename=list_objects())


my_dag = alice_s3_processor()
