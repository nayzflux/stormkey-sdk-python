# Stormkey

## Introduction

Stormkey is a Python library that provides a convenient interface for managing API keys for your applications. Whether you need to create, update, verify, or delete API keys, Stormkey simplifies the process with easy-to-use methods.

## Installation

You can install Stormkey via pip:

```bash
pip install stormkey
```

## Usage

To use Stormkey in your Python project, first import the `Stormkey` class and initialize it with your application ID, service key, and optional host URL.

```python
from stormkey import Stormkey

app_id = "your_application_id"
service_key = "your_service_key"
host = "https://api.stormkey.app"  # Optional host URL

stormkey = Stormkey(app_id, service_key, host)
```

### Methods

- **create(name: str, ownerId: str) -> str**: Creates a new API key with the specified name and owner ID.
- **update(name: str, ownerId: str) -> str**: Updates the specified API key with a new name and owner ID.
- **verify(key: str) -> dict**: Verifies the validity of the provided API key.
- **delete(name: str) -> str**: Deletes the API key with the specified name.

## Examples

Here's a simple example demonstrating how to use Stormkey to create a new API key:

```python
key_name = "MyAPIKey"
owner_id = "user123"

key = stormkey.create(key_name, owner_id)
print("New API Key:", key["secretKey"])
```

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests on [GitHub](https://github.com/nayzflux/stormkey-sdk-python).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
