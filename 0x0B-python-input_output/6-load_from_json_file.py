#!/usr/bin/python3
"""
This module contains the load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”

    Args:
        filename(str) :  the file name
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.loads(f.read())
