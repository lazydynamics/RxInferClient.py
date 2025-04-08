# RxInferClient

A Python client for interacting with RxInfer, a probabilistic programming framework.

> **Note:** This project is currently a work in progress. The implementation is under active development and may undergo significant changes.

## Overview

RxInferClient provides a simple and intuitive interface to work with RxInfer from Python. It allows you to define models, run inference, and process results with a clean API.

## Installation

```bash
pip install rxinfer-client
```

## Requirements

- Python 3.9+
- Dependencies are managed through `pyproject.toml`

## Development

### Project Structure

```
RxInferClient.py/
├── src/
│   └── rxinfer_client/      # Main package code
├── openapi/
│   └── client/             # Auto-generated OpenAPI client
├── tests/                  # Test suite
├── Makefile               # Development commands
└── pyproject.toml         # Package configuration
```

### Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/lazydynamics/RxInferClient.py.git
   cd RxInferClient.py
   ```

2. Create a virtual environment and install development dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   pip install -e ".[dev]"
   ```

3. Generate the OpenAPI client:
   ```bash
   make generate-client
   ```

### Development Commands

The project uses a Makefile for common development tasks:

```bash
# Generate OpenAPI client code
make generate-client

# Run tests
make test

# Run tests with coverage
make test-cov

# Clean generated files
make clean

# Show all available commands
make help
```

### Testing

The project uses pytest for testing. You can run tests in two ways:

1. Using the Makefile:
   ```bash
   make test
   ```

2. Directly with pytest:
   ```bash
   pytest tests/
   ```

For coverage reports:
```bash
make test-cov
```

### Building the Package

To build the package, run:

```bash
python -m build
```

This will create both source distribution and wheel packages in the `dist/` directory.

### Publishing the Package

1. Make sure you have the latest versions of build tools:
   ```bash
   pip install --upgrade build twine
   ```

2. Build the distribution packages:
   ```bash
   python -m build
   ```

3. [Optional] Upload to TestPyPI first to verify everything works:
   ```bash
   python -m twine upload --repository testpypi dist/*
   ```

4. Once verified, upload to the real PyPI:
   ```bash
   python -m twine upload dist/*
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the Apache License, Version 2.0 - see the LICENSE file for details.