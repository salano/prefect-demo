from prefect import flow
from prefect.runner.storage import GitRepository
from prefect_github import GitHubCredentials

if __name__ == "__main__":
    git_repo = GitRepository(
        url="https://github.com/salano/prefect-demo.git",
        credentials=GitHubCredentials.load("githubblock")
    )

    flow.from_source(
        source=git_repo,
        entrypoint="hello.py:hello_world",
    ).deploy(
        name="first-deployment",
        work_pool_name="my-managed-pool",
        cron="0 1 * * *",
    )