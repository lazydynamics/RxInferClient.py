# RxInferClient

A Python client for interacting with RxInfer, a probabilistic programming framework.

> **Note:** This project is currently a work in progress. The implementation is under active development and may undergo significant changes.

## Overview

RxInferClient provides a simple and intuitive interface to work with RxInfer from Python. It allows you to define models, run inference, and process results with a clean API.

### Quickstart

```python
from rxinferclient import RxInferClient

client = RxInferClient()

# Ping the server to check if it's running
response = client.server.ping_server()
print(response)

# Create a model instance
response = client.models.create_model_instance({ 
    "model_name": "BetaBernoulli-v1"
})
instance_id = response.instance_id

# Delete the model instance
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