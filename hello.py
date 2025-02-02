from prefect import flow, task

@task(retries=2)
def create_task():
    msg = 'Hello from task'
    return (msg)

@flow
def something_else():
    result = 10
    return (result)

#decorator so that print statements within the flow-decorated function will be logged.
@flow(log_prints=True)
def hello_world():
    subflow_message = something_else()
    task_message = create_task()
    new_message = task_message + str(subflow_message)
    print(new_message)


if __name__ == "__main__":
    hello_world.serve(name="demot-deployment",
                    cron="* * * * *",
                    tags=["testing", "demo"],
                    description="Given a GitHub repository, logs repository statistics for that repo.",
                    version="tutorial/deployments",)