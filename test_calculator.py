"""
Unit tests for the calculator module.
Tests basic mathematical operations and edge cases.
"""

import pytest
from calculator import add, subtract, multiply, divide, power


class TestCalculator:
    """Test suite for calculator functions."""

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        assert add(-5, -3) == -8
        assert add(-10, 5) == -5

    def test_add_floats(self):
        """Test addition with floating point numbers."""
        assert add(2.5, 3.5) == 6.0
        assert add(1.1, 2.2) == pytest.approx(3.3)

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        assert subtract(10, 5) == 5
        assert subtract(20, 15) == 5

    def test_subtract_negative_result(self):
        """Test subtraction resulting in negative number."""
        assert subtract(5, 10) == -5
        assert subtract(0, 5) == -5

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        assert multiply(3, 4) == 12
        assert multiply(5, 6) == 30

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 10) == 0

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        assert multiply(-3, 4) == -12
        assert multiply(-3, -4) == 12

    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        assert divide(10, 2) == 5
        assert divide(15, 3) == 5

    def test_divide_with_remainder(self):
        """Test division with remainder."""
        assert divide(10, 3) == pytest.approx(3.333333, rel=1e-5)
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_power_positive_exponent(self):
        """Test power with positive exponent."""
        assert power(2, 3) == 8
        assert power(5, 2) == 25

    def test_power_zero_exponent(self):
        """Test power with zero exponent."""
        assert power(5, 0) == 1
        assert power(100, 0) == 1

    def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        assert power(2, -1) == 0.5
        assert power(10, -2) == 0.01
