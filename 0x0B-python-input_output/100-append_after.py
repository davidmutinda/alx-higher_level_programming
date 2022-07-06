#!/usr/bin/python3
"""
This module contains append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line to a file, after each line containing a specific string

    Args:
        filename(str) : the name of the file
        search_string(str) : the string you're searching for
        new_string(str) : the string to append to file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        contents = f.readlines()
        k = 0

        while k < len(contents):
            if search_string in contents[k]:
                contents.insert(k + 1, new_string)
            k += 1

    with open(filename, 'w', encoding="utf-8") as f:
        contents = "".join(contents)
        f.write(contents)
