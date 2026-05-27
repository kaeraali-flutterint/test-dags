# Alice's test DAGs

Example DAG code useful to test that basic Airflow 3.x functionality is working. These are designed for infrastructure engineers or less-experienced data developers and provide basic DAGs that you can upload to your new Airflow installation to validate a few things.

## Dependencies

These DAGs are written for an Airflow 3.2.1 installation, they've been tested in an AWS MWAA environment but should work anywhere as long as you have the right dependencies

- `apache-airflow==3.2.1`
- `apache-airflow[amazon]`
- `paramiko` for the paramiko DAG

## Usage

These DAGs are designed to be deployed to an Airflow installation without needing to test any code locally. That said, you will need to make some changes for some DAGs.

The DAGs are all in the `./dags` directory, but you should review the code before deploying

Specifically, you should change:

- `BUCKET` in the `alice_s3_processor.py` DAG so that you are accessing an S3 bucket of your own
- email addresses in the `alice_test_broken.py` and `alice_test_email_dag.py` to ensure you're sending emails to and from valid addresses

## Contributing

You probably want a virtual environment (`python3 -m venv venv && source ./venv/bin/activate`), and then:

- `make install` to install development dependencies
- `make check` to run lint checks
- `make test` to run tests

PRs to this repository will run all of the above via GitHub Actions

We like but do not enforce [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)
