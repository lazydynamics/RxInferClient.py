# RxInferClient

A Python client for interacting with RxInfer, a probabilistic programming framework.

> **Note:** This project is currently a work in progress. The implementation is under active development and may undergo significant changes.

## Overview

RxInferClient provides a simple and intuitive interface to work with RxInfer from Python. It allows you to define models, run inference, and process results with a clean API.

The client functionality is organized into several subfields:
- `server`: Access to server-related operations
- `authentication`: Authentication and token management
- `models`: Model management and operations

### Quickstart

```python
from rxinferclient import RxInferClient

# Initialize with default settings (auto-generates API key)
client = RxInferClient()

# Or initialize with custom server URL
client = RxInferClient(server_url="http://localhost:8000/v1")

# Or initialize with your own API key
client = RxInferClient(api_key="your-api-key")

# Ping the server to check if it's running
response = client.server.ping_server()
print(response.status)  # 'ok'

# Create a model instance
response = client.models.create_model_instance({ 
    "model_name": "BetaBernoulli-v1"
})
instance_id = response.instance_id

# Delete the model instance when done
client.models.delete_model_instance(instance_id=instance_id)
```

## Installation

```bash
pip install rxinferclient
```

## Requirements

- Python 3.9+
- Dependencies are managed through `pyproject.toml`

### Development Commands

The project uses a Makefile for common development tasks. Run `make help` to see all available commands.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the Apache License, Version 2.0 - see the LICENSE file for details.