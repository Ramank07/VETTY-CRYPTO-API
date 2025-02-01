## Running Tests

1. Install dependencies:
   ```bash
   pip install fastapi requests pytest pytest-cov


## Run the tests:
pytest --cov=app tests/

## Generate an HTML coverage report:
pytest --cov=app --cov-report=html tests/
