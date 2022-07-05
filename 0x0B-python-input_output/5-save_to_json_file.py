#!/usr/bin/python3
"""
This module contains save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation

    Args:
        my_obj(object) : the object
        filename(str) : the file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
