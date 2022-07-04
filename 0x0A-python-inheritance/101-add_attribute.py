#!/usr/bin/python3
"""
This module adds an attribute to a class
"""


def add_attribute(obj, name, value):
    """
    This function sets attributes to an object
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
