"""
Simple calculator module for basic mathematical operations.
This module provides functions for addition, subtraction, multiplication, and division.
"""


def add(a, b):
    """
    Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    """
    return a + b


def subtract(a, b):
    """
    Subtract b from a.

    Args:
        a: First number
        b: Second number

    Returns:
        The difference between a and b
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        The product of a and b
    """
    return a * b


def divide(a, b):
    """
    Divide a by b.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        The quotient of a divided by b

    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """
    Calculate a raised to the power of b.

    Args:
        a: Base number
        b: Exponent

    Returns:
        a raised to the power of b
    """
    return a ** b
