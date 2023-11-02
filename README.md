# Python Project Template

This repository is a simple template for Python projects. It includes:

- Source code in the `src` directory
- Tests in the `tests` directory using `pytest`
- A simple `Makefile` to package common tasks
- A GitHub Action to run tests on every push

## Getting Started

### Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.8 or later
- make

### Setting Up the Development Environment

To set up your development environment, you'll use a `Makefile` which simplifies the process of creating a virtual environment, installing dependencies, and running tests. Here's how to use it:

1. Create a Virtual Environment:

   Run the following command to create a virtual environment. This will help you manage your Python dependencies separately from your system Python installation.

   ```bash
   make venv
   ```

2. After creating the virtual environment, you need to activate it:

   ```bash
   source venv/bin/activate
   ```

3. To install your project along with all dependencies, needed for development use:

   ```bash
   make install-test-dependencies
   ```

4. You can run tests using:

   ```bash
   make test
   ```

This will execute the pytest tests located in your project.

## Continuous Integration

This template includes a basic GitHub Action located in `.github/workflows/main.yml`. The action will run tests on every push to the remote repository.
