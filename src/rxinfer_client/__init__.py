"""
RxInfer Client - A Python client for the RxInfer API
"""

__version__ = "0.0.1"

from .client import RxInferClient
from .exceptions import RxInferError

__all__ = ["RxInferClient", "RxInferError"] 