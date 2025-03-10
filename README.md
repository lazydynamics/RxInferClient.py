# RxInferClient

A Python client for interacting with RxInfer, a probabilistic programming framework.

> **Note:** This project is currently a work in progress. The implementation is under active development and may undergo significant changes.

## Overview

RxInferClient provides a simple and intuitive interface to work with RxInfer from Python. It allows you to define models, run inference, and process results with a clean API.

## Installation

```bash
pip install rxinferclient
```

## Requirements

- Python 3.9+
- Dependencies are listed in `requirements.txt`

## Contributing

### Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/RxInferClient.py.git
   cd RxInferClient.py
   ```

2. Create a virtual environment and install development dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   pip install -e ".[dev]"
   ```

### Building the Package

To build the package, run:

```bash
python -m build
```

This will create both source distribution and wheel packages in the `dist/` directory.

### Testing

Run tests using pytest:

```bash
pytest tests/
```

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

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the Apache License, Version 2.0 - see the LICENSE file for details.