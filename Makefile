install:
	pip install --constraint https://raw.githubusercontent.com/apache/airflow/constraints-3.2.1/constraints-3.12.txt -e .

@phony: check
check:
	ruff check

@phony: test
test:
	AIRFLOW_HOME=$(pwd) AIRFLOW__LOGGING__BASE_LOG_FOLDER=./logs python tests/test_dag_integrity.py
	find dags -type f -name '*.py' -exec python {} \;
