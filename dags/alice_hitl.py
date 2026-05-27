from airflow.providers.standard.operators.hitl import HITLEntryOperator
from airflow.sdk import DAG

with DAG("alice_hitl", schedule=None, tags=["alice"]) as dag:
    review_content = HITLEntryOperator(
        task_id="review_content",
        subject="Please review this content for publication",
    )
