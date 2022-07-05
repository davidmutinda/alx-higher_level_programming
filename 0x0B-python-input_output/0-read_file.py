#!/usr/bin/python3
"""
This module reads a text file and prints it to stdout
"""


def read_file(filename=""):
    """
    This function reads file and prints it

    Args:
        filename(str) : the filename

    Return:
        Nothing
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
