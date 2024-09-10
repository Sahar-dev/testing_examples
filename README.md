# Python Testing Frameworks and Examples

This repository contains examples of using different Python testing frameworks and libraries. Each folder showcases a specific approach to testing, including unit tests, integration tests, API mocking, and performance tests. These examples demonstrate how to effectively test applications in real-world scenarios using the tools and strategies outlined.
## Structure of the folder
```bash
├───fastapi
│   ├───main.py                # Example FastAPI app
│   └───test_main.py           # Tests for FastAPI app using pytest
│
├───Integration                # Placeholder for integration testing
│
├───locust
│   └───hello.py               # Performance testing using Locust
│
├───Mocking_External_APIs
│   ├───scraper.py             # Example scraper
│   └───test_scraper.py        # Mocking external API requests using pytest
│
└───unittest
    ├───calculator.py          # Example calculator module
    ├───test_calculator_hypothesis.py  # Testing using hypothesis
    ├───test_calculator_nose2.py       # Testing using nose2
    ├───test_calculator_pytest.py      # Testing using pytest
    └───test_calculator_unittest.py    # Testing using unittest

```
## Libraries and Tools Used

- **pytest**: A framework that makes building simple and scalable test cases easy.
- **unittest**: The built-in Python unit testing framework.
- **hypothesis**: A property-based testing library for Python.
- **nose2**: A plugin-based test runner for Python.
- **FastAPI**: A high-performance Python web framework for building APIs.
- **Locust**: An open-source load testing tool that defines user behavior using Python code.
- **Mocking Libraries**: Tools for mocking external API responses in tests.

## How to Use

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/testing-examples.git
    ```
2. Navigate to the folder of the test type you're interested in:
    ```bash
    cd testing-examples/unittest
    ```
3. Run the tests:
    ```bash
    pytest test_calculator_pytest.py
    ```
   or for `unittest`:
    ```bash
    python -m unittest test_calculator_unittest.py
    ```

## Folder Overview

### FastAPI
This folder contains a simple FastAPI application and a corresponding test file showcasing how to test FastAPI routes using `pytest`.

### Integration
A placeholder for future integration test examples.

### Locust
Performance testing using Locust, simulating user behavior and load on a system.

### Mocking External APIs
This section demonstrates how to mock external APIs using libraries like `unittest.mock` and `responses` in combination with `pytest`.

### Unittest
This folder contains various examples of unit testing using different Python libraries like `unittest`, `pytest`, `nose2`, and `hypothesis`.

## Contributing
Feel free to fork this repository, add your own examples or tests, and submit a pull request. We welcome contributions that help others learn different testing methodologies.
