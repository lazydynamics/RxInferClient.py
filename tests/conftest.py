"""
Test configuration and fixtures
"""
import pytest
from rxinfer_client import RxInferClient

@pytest.fixture
def mock_base_url():
    """Mock base URL for testing"""
    return "http://localhost:8000"

@pytest.fixture
def mock_api_key():
    """Mock API key for testing"""
    return "test-api-key"

@pytest.fixture
def client(mock_base_url, mock_api_key):
    """Create a test client instance"""
    return RxInferClient(mock_base_url, mock_api_key) 