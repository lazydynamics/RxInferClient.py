"""
Main client class for RxInfer API
"""

from typing import Optional
from rxinfer_openapi import ApiClient

class RxInferClient:
    """
    High-level client for the RxInfer API.
    
    This class provides a more user-friendly interface to the RxInfer API,
    wrapping the auto-generated client code.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        self._api_client = ApiClient()
        self._api_client.configuration.access_token = api_key