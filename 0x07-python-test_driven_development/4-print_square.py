#!/usr/bin/python3
"""
This module defines `print_square`
The function prints a square with the character #
"""


def print_square(size):
    """
    prints a square with character #

    Args:
        size (int) : determines size of square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0

    Returns:
        nothing
    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
