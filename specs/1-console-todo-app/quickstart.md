# Quickstart: In-Memory Console Todo App

This guide explains how to set up and run the console-based todo application.

## Prerequisites

- Python 3.13+
- `uv` (for environment management)

## Setup and Installation

1.  **Create and activate a virtual environment:**
    ```bash
    uv venv
    uv sync
    ```
    (Assuming a `pyproject.toml` will be created later for dependencies like `pytest`)

2.  **Activate the environment:**
    - **Windows:**
      ```powershell
      .venv\Scripts\Activate.ps1
      ```
    - **macOS/Linux:**
      ```bash
      source .venv/bin/activate
      ```

## Running the Application

Once the environment is activated, you can run the application from the root of the project directory:

```bash
python -m src.main
```

The application will launch and present you with a menu of options to manage your todos.

## Running Tests

To run the unit tests for the application, use `pytest`:

```bash
pytest
```
