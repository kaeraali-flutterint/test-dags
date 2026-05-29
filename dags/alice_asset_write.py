from airflow.sdk import Asset, CronPartitionTimetable, dag, task

alice_asset = Asset("alice_partitioned_asset")


@dag(schedule=CronPartitionTimetable("0 0 * * *", timezone="UTC"))
def alice_asset_write():
    @task(outlets=[alice_asset])
    def alice_partitioned_write(**context):
        pass

    alice_partitioned_write()


alice_asset_write()

if __name__ == "__main__":
    alice_asset_write().test()
