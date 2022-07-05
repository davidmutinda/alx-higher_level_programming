#!/usr/bin/python3
"""
This module contains the to_json_string function
"""
import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)

    Args:
        my_obj(object) : object

    Return:
        JSON reoresentation of object
    """
    return json.dumps(my_obj)
