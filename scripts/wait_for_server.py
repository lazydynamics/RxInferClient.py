#!/usr/bin/env python3
"""
Script to wait for RxInferServer to become available.
"""
import os
import sys
import time
from datetime import datetime, timedelta
from urllib3.exceptions import HTTPError
from rxinferclient import RxInferClient

def is_running_in_ci():
    """Check if we're running in a CI environment"""
    ci_env_vars = [
        'CI',                    # Generic CI
        'GITHUB_ACTIONS',        # GitHub Actions
        'GITLAB_CI',            # GitLab CI
        'CIRCLECI',             # Circle CI
        'JENKINS_URL',          # Jenkins
        'TRAVIS',               # Travis CI
        'TF_BUILD',             # Azure Pipelines
        'TEAMCITY_VERSION'      # TeamCity
    ]
    return any(os.getenv(var) for var in ci_env_vars)

def wait_for_server(timeout=None, retry_interval=None):
    """Wait for the server to be available.
    
    Args:
        timeout: Timeout in seconds. If None, uses default based on environment.
        retry_interval: Interval between retries in seconds. If None, uses default based on environment.
    """
    is_ci = is_running_in_ci()
    timeout = timeout or (300 if is_ci else 30)  # 5 minutes in CI, 30 seconds locally
    retry_interval = retry_interval or (10 if is_ci else 1)  # 10 seconds in CI, 1 second locally
    
    start_time = datetime.now()
    timeout_delta = timedelta(seconds=timeout)
    env_type = "CI" if is_ci else "local"
    
    print(f"Waiting for RxInferServer to become available ({env_type} environment)...")
    
    while datetime.now() - start_time < timeout_delta:
        try:
            client = RxInferClient()
            response = client.server.ping_server()
            if response.status == 'ok':
                print("RxInferServer is available!")
                return True
        except HTTPError:
            pass
        
        print(f"Server not available yet. Will retry in {retry_interval} seconds...")
        time.sleep(retry_interval)
    
    print(f"Error: RxInferServer did not become available within {timeout} seconds ({env_type} environment)")
    return False

if __name__ == "__main__":
    success = wait_for_server()
    sys.exit(0 if success else 1) 