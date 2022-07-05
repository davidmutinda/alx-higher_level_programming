#!/usr/bin/python3
"""
This module contains from_json_string function
"""
import json


def from_json_string(my_str):
    """
    returns an object (Python data structure) represented by a JSON string

    Args:
        my_str(str) : json string

    Returns:
        object
    """
    return json.loads(my_str)
