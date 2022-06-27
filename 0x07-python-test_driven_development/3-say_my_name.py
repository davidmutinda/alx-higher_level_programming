#!/usr/bin/python3
"""
This module defines `say_my_name`
The function prints names
"""


def say_my_name(first_name, last_name=""):
    """
    prints names

    Args:
        first_name (str) : the first name
        last_name (str) : the last name

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string

    Returns:
        nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
