from prefect import flow, task, serve
from prefect.tasks import task_input_hash
from datetime import timedelta
import time


@task(retries=2, retry_delay_seconds=5)
def create_task():
    msg = 'Hello from task'
    return (msg)

#implement caching
@task(cache_key_fn=task_input_hash, 
      cache_expiration=timedelta(hours=1),
      )
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

@flow
def slow_flow(sleep: int = 60):
    "Sleepy flow - sleeps the provided amount of time (in seconds)."
    time.sleep(sleep)


@flow
def fast_flow():
    "Fastest flow this side of the Mississippi."
    return

if __name__ == "__main__":
    #Deploy multiple flows
    '''
    slow_deploy = slow_flow.to_deployment(name="sleeper", interval=45)
    fast_deploy = fast_flow.to_deployment(name="fast")
    serve(slow_deploy, fast_deploy)
    '''

    hello_world()