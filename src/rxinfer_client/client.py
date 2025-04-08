"""
Main client class for RxInfer API
"""

from typing import Optional
from rxinfer_client.generated import ApiClient

class RxInferClient:
    """
    High-level client for the RxInfer API.
    
    This class provides a more user-friendly interface to the RxInfer API,
    wrapping the auto-generated client code.
    """
    
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self._api_client = ApiClient(base_url=base_url, api_key=api_key)