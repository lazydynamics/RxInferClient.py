"""
Tests for the RxInfer client
"""
import pytest
from unittest.mock import patch, MagicMock
from rxinferclient import RxInferClient
from rxinferclient.api_client import ApiClient

def test_client_initialization(mock_base_url, mock_api_key):
    """Test client initialization with and without API key"""
    # Test with API key
    client = RxInferClient(mock_api_key)
    
    assert client != None
    assert ApiClient != None