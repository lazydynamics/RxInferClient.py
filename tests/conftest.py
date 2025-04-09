"""
Test configuration and fixtures
"""
import os
import sys
import pytest

# Add scripts directory to path to import wait_for_server
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from wait_for_server import wait_for_server # type: ignore

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
def wait_for_server_fixture():
    """Wait for the server to be available before running tests"""
    if not wait_for_server():
        pytest.fail("Server did not become available within the timeout period")