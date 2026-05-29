install:
	pip install --constraint https://raw.githubusercontent.com/apache/airflow/constraints-3.2.1/constraints-3.12.txt -e .

@phony: check
check:
	ruff check

@phony: test
test:
	AIRFLOW_HOME=$(shell pwd) AIRFLOW__LOGGING__BASE_LOG_FOLDER=./logs airflow db reset -y
	AIRFLOW_HOME=$(shell pwd) AIRFLOW__LOGGING__BASE_LOG_FOLDER=./logs airflow db migrate
	AIRFLOW_HOME=$(shell pwd) AIRFLOW__LOGGING__BASE_LOG_FOLDER=./logs python tests/test_dag_integrity.py
	AIRFLOW_HOME=$(shell pwd); export AIRFLOW_HOME; \
		for file in $(shell find dags -type f -name '*.py'); do \
			python "$$file" || exit 1; \
		done
