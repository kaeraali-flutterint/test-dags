install:
	pip install --constraint https://raw.githubusercontent.com/apache/airflow/constraints-3.0.6/constraints-3.12.txt -e .

@phony: check
check:
	ruff check

@phony: test
test:
	AIRFLOW_HOME=$(pwd) python tests/test_dag_integrity.py
