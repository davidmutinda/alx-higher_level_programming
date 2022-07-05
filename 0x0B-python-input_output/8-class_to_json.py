#!/usr/bin/ython3
"""
This module contains the class_to_json function
"""


def class_to_json(obj):
    """
    returns dictionary description with simple data structure

    Args:
        obj(object) : the object
    """
    return obj.__dict__
