#!/usr/bin/python3
"""
This module contains the write_file function
"""


def write_file(filename="", text=""):
    """
    writes a string to text file and returns the number of characters written

    Args:
        filename(str) : the file to  write in
        text(str) : string

    Return:
        Number of characters written
    """

    with open(filename, 'w', encoding="utf-8") as f:
        num = f.write(text)
        return num
