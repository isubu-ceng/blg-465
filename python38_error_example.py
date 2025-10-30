"""
Python 3.8 Error Example

This file demonstrates code that will throw an error in Python 3.8
but works correctly in Python 3.10 and later versions.

The code uses the union type syntax (X | Y) which was introduced in
Python 3.10. In Python 3.8, this will raise a TypeError because the
'|' operator is not supported for type annotations.
"""


def process_value(value: int | str) -> str:
    """
    Process a value that can be either an integer or a string.

    This function uses the union type syntax (int | str) which is a
    Python 3.10+ feature. In Python 3.8, attempting to use '|' for
    type unions will cause a TypeError.

    Args:
        value: An integer or string value to process

    Returns:
        A string representation of the value

    Raises:
        TypeError: In Python 3.8, this will fail at function definition
                   time with "unsupported operand type(s) for |:
                   'type' and 'type'"
    """
    if isinstance(value, int):
        return f"Integer value: {value}"
    else:
        return f"String value: {value}"


def demonstrate_dict_merge(
    dict1: dict[str, int],
    dict2: dict[str, int]
) -> dict[str, int]:
    """
    Demonstrate dictionary merge using the | operator.

    This function uses two Python 3.9+ features:
    1. Generic dict type syntax: dict[str, int] instead of Dict[str, int]
    2. Dictionary merge operator: dict1 | dict2

    Args:
        dict1: First dictionary
        dict2: Second dictionary

    Returns:
        Merged dictionary

    Raises:
        TypeError: In Python 3.8, this will fail due to:
                   - Unsupported generic type syntax
                   - Unsupported dictionary merge operator
    """
    return dict1 | dict2


if __name__ == "__main__":
    # Example usage - these will only work in Python 3.10+
    print("Testing union type annotation...")
    result1 = process_value(42)
    print(result1)

    result2 = process_value("hello")
    print(result2)

    print("\nTesting dictionary merge...")
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}
    merged = demonstrate_dict_merge(d1, d2)
    print(f"Merged dictionary: {merged}")

    print("\nAll examples completed successfully!")
    print("Note: This code will fail in Python 3.8 with TypeError")
