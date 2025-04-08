"""
Test configuration and fixtures
"""
import os
import time
from datetime import datetime, timedelta
from aiohttp.client_exceptions import ClientConnectorError
import pytest
from rxinferclient import RxInferClient

def is_running_in_ci():
    """Check if we're running in a CI environment by looking for common CI environment variables"""
    ci_env_vars = [
        'CI',                    # Generic CI
        'GITHUB_ACTIONS',        # GitHub Actions
        'GITLAB_CI',            # GitLab CI
        'CIRCLECI',            # Circle CI
        'JENKINS_URL',         # Jenkins
        'TRAVIS',              # Travis CI
        'TF_BUILD',            # Azure Pipelines
        'TEAMCITY_VERSION'     # TeamCity
    ]
    return any(os.getenv(var) for var in ci_env_vars)

@pytest.fixture(autouse=True, scope="session")
async def wait_for_server():
    """Wait for the server to be available before running tests"""
    # Use longer timeout in CI, shorter locally
    is_ci = is_running_in_ci()
    timeout = timedelta(minutes=5) if is_ci else timedelta(seconds=5)
    retry_interval = 10 if is_ci else 1  # seconds
    
    start_time = datetime.now()
    
    while datetime.now() - start_time < timeout:
        try:
            client = RxInferClient()
            response = await client.server.ping_server()
            if response.status == 'ok':
                return  # Server is ready
        except ClientConnectorError:
            env_type = "CI" if is_ci else "local"
            print(f"Waiting for server to be available ({env_type} environment). Will retry in {retry_interval} seconds...")
            time.sleep(retry_interval)
    
    timeout_mins = timeout.total_seconds() / 60
    env_type = "CI" if is_ci else "local"
    pytest.fail(f"Server did not become available within {timeout_mins:.1f} minutes ({env_type} environment)")