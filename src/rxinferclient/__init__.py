"""
RxInfer Client - Python client for the RxInfer probabilistic programming framework.

This package provides a client interface to interact with RxInfer models and inference algorithms.
"""

__version__ = "0.1.0"

from .wrapper.client import RxInferClient

__all__ = [
    "RxInferClient",
]
