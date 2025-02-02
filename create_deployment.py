from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/salano/prefect-demo.git",
        entrypoint="hello.py:hello_world",
    ).deploy(
        name="first-deployment",
        work_pool_name="my-managed-pool",
        cron="0 1 * * *",
    )