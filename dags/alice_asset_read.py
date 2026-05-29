from airflow.sdk import Asset, PartitionedAssetTimetable, StartOfDayMapper, dag, task

alice_asset = Asset("alice_partitioned_asset")


@dag(
    schedule=PartitionedAssetTimetable(
        assets=alice_asset,
        partition_mapper_config={alice_asset: StartOfDayMapper()},
    )
)
def alice_asset_read():
    @task
    def alice_read_asset(**context):
        print(context["dag_run"].partition_key)

    alice_read_asset()


alice_asset_read()

if __name__ == "__main__":
    alice_asset_read().test()
