"""
Tests for the RxInfer client
"""
import pytest
from unittest.mock import patch, MagicMock
from rxinferclient import RxInferClient

def test_autogenerated_code_should_be_accessible():
    """Test that the autogenerated code is accessible"""
    from rxinferclient.api_client import ApiClient
    assert ApiClient != None

def test_client_initialization():
    """Test client initialization with and without API key"""
    # Test with API key
    client = RxInferClient()
    assert client != None
    
async def test_simple_ping_to_the_server():
    client = RxInferClient()
    response = await client.server.ping_server()
    assert response != None
    assert response.status == 'ok'