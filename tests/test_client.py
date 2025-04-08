"""
Tests for the RxInfer client
"""
import pytest
from unittest.mock import patch, MagicMock
from rxinfer_client import RxInferClient

def test_client_initialization(mock_base_url, mock_api_key):
    """Test client initialization with and without API key"""
    # Test with API key
    client = RxInferClient(mock_base_url, mock_api_key)
    assert client._api_client.configuration.host == mock_base_url
    assert client._api_client.configuration.api_key['Authorization'] == f"Bearer {mock_api_key}"
    
    # Test without API key
    client = RxInferClient(mock_base_url)
    assert client._api_client.configuration.host == mock_base_url
    assert 'Authorization' not in client._api_client.configuration.api_key