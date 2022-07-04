#!/usr/bin/python3
"""
This module returns list of available attributes of an object
"""


def lookup(obj):
    """
    Returns list of available attributes of an object
    """
    return dir(obj)
