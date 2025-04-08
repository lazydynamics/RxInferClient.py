# RxInfer Client

A Python client for interacting with RxInfer, a probabilistic programming framework.

## Features

- Simple and intuitive API
- Full support for RxInfer's features
- Type hints for better IDE support
- Comprehensive documentation
- Built on top of OpenAPI specification

## Quick Start

```python
from rxinfer_client import RxInferClient

# Initialize the client
client = RxInferClient("http://localhost:8000", "your-api-key")

# Check if the server is responding
if client.ping():
    # Get available models
    models = client.models.get_models()
    print(f"Available models: {models}")
```

## Documentation

- [Installation](installation.md) - How to install the client