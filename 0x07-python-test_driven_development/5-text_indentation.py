#!/usr/bin/python3
"""
This module defines `text_indentation`
The function indents and prints text
"""


def text_indentation(text):
    """
    indents and prints text

    Args:
        text(str): string to be indented and printed

    Raises:
       TypeError: text must be a string

    Returns:
        doesn't return
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while(i < len(text)):
        if text[i] in (".", "?", ":"):
            print("{}\n".format(text[i]))
            while (text[i + 1] == ' '):
                i += 1
        else:
            print(text[i], end="")
        i += 1
