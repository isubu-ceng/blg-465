# blg-465

A sample Python project demonstrating CI/CD pipeline processes with testing, linting, and automated workflows.

## Project Description

This project provides a simple calculator module with basic mathematical operations. It serves as a demonstration of:
- Python best practices
- Unit testing with pytest
- CI/CD pipelines using GitHub Actions
- Code coverage reporting
- Automated linting

## Features

The calculator module provides the following operations:
- Addition
- Subtraction
- Multiplication
- Division (with zero-division protection)
- Power/Exponentiation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sametxpolat/blg-465.git
cd blg-465
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```python
from calculator import add, subtract, multiply, divide, power

# Basic operations
result = add(5, 3)        # 8
result = subtract(10, 4)  # 6
result = multiply(3, 7)   # 21
result = divide(15, 3)    # 5.0
result = power(2, 3)      # 8
```

## Running Tests

Run all tests:
```bash
pytest test_calculator.py -v
```

Run tests with coverage:
```bash
pytest test_calculator.py --cov=calculator --cov-report=term-missing
```

## Linting

Check code style with flake8:
```bash
flake8 calculator.py test_calculator.py
```

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration:

- **Python CI**: Runs tests on multiple Python versions (3.8, 3.9, 3.10, 3.11)
- **Python Linting**: Checks code quality and style

Workflows are automatically triggered on:
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop` branches

## Project Structure

```
blg-465/
├── .github/
│   └── workflows/
│       ├── ci.yml          # CI testing workflow
│       └── lint.yml        # Linting workflow
├── calculator.py           # Main calculator module
├── test_calculator.py      # Unit tests
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure all tests pass
5. Submit a pull request

## License

This is a sample educational project.