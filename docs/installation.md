# Installation

## Requirements

- Python 3.9 or higher
- pip (Python package installer)

## Installation Methods

### From PyPI

The easiest way to install RxInferClient is using pip:

```bash
pip install rxinferclient
```

### From Source

If you want to install the latest development version or contribute to the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/lazydynamics/RxInferClient.py.git
   cd RxInferClient.py
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   # On Unix/macOS
   python -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the package in development mode with all dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

### Development Setup

For development, you'll need additional tools. The development setup includes:

1. Install development dependencies:
   ```bash
   make install-dev
   ```

2. Generate the OpenAPI client code:
   ```bash
   make generate-client
   ```

3. Run tests to verify the installation:
   ```bash
   make test
   ```
