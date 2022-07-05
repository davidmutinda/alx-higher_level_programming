#!/usr/bin/python3
"""
This module contains the append_write function
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file

    Args:
        filename(str) : file directory
        text(str) : string to be appended to file

    Return:
        the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
