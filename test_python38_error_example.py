"""
Unit tests for the python38_error_example module.

This test file imports from python38_error_example.py, which uses Python 3.10+
type annotation features. The import itself will fail on Python 3.8, causing
the CI pipeline to fail when running tests on Python 3.8.
"""

import pytest
from python38_error_example import process_value, demonstrate_dict_merge


class TestPython38ErrorExample:
    """Test suite for python38_error_example functions."""

    def test_process_value_with_integer(self):
        """Test process_value with integer input."""
        result = process_value(42)
        assert result == "Integer value: 42"
        assert isinstance(result, str)

    def test_process_value_with_string(self):
        """Test process_value with string input."""
        result = process_value("hello")
        assert result == "String value: hello"
        assert isinstance(result, str)

    def test_process_value_with_negative_integer(self):
        """Test process_value with negative integer."""
        result = process_value(-100)
        assert result == "Integer value: -100"

    def test_process_value_with_empty_string(self):
        """Test process_value with empty string."""
        result = process_value("")
        assert result == "String value: "

    def test_demonstrate_dict_merge_basic(self):
        """Test dictionary merge with basic dictionaries."""
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        result = demonstrate_dict_merge(dict1, dict2)
        
        assert result == {"a": 1, "b": 2, "c": 3, "d": 4}
        assert len(result) == 4

    def test_demonstrate_dict_merge_overlapping_keys(self):
        """Test dictionary merge with overlapping keys."""
        dict1 = {"a": 1, "b": 2}
        dict2 = {"b": 3, "c": 4}
        result = demonstrate_dict_merge(dict1, dict2)
        
        # Second dict values should override first dict
        assert result["b"] == 3
        assert result == {"a": 1, "b": 3, "c": 4}

    def test_demonstrate_dict_merge_empty_dicts(self):
        """Test dictionary merge with empty dictionaries."""
        dict1 = {}
        dict2 = {}
        result = demonstrate_dict_merge(dict1, dict2)
        
        assert result == {}
        assert len(result) == 0

    def test_demonstrate_dict_merge_one_empty(self):
        """Test dictionary merge with one empty dictionary."""
        dict1 = {"a": 1, "b": 2}
        dict2 = {}
        result = demonstrate_dict_merge(dict1, dict2)
        
        assert result == {"a": 1, "b": 2}
