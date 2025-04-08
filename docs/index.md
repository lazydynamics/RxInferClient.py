# RxInfer Client

A Python client for interacting with RxInferServer.

## Features

- Simple and intuitive API
- Type hints for better IDE support
- Comprehensive documentation
- Built on top of OpenAPI specification
- Automatic API key generation
- Configurable server URL
- Organized functionality through logical subfields

## Client Structure

The client functionality is organized into several subfields:
- `server`: Access to server-related operations (e.g., ping, health checks)
- `authentication`: Authentication and token management
- `models`: Model management and operations (create, delete, etc.)

## Quick Examples

```python
from rxinferclient import RxInferClient

# Initialize with default settings
client = RxInferClient()

# Or with custom server URL
client = RxInferClient(server_url="http://localhost:8000/v1")

# Check server status
response = client.server.ping_server()
assert response.status == 'ok'

# Work with models
response = client.models.create_model_instance({
    "model_name": "BetaBernoulli-v1",
})
instance_id = response.instance_id

# Clean up
client.models.delete_model_instance(instance_id=instance_id)
```

## Documentation

- [Installation](installation.md) - How to install the client

## API Reference

::: rxinferclient.wrapper.client
