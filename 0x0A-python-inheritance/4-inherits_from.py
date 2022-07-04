#!/usr/bin/python3
"""
This module checks if instance of class is inherited
"""


def inherits_from(obj, a_class):
    """
    This function returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise False
    """
    return issubclass(obj.__class__, a_class) and type(obj) != a_class
