#!/usr/bin/python3
"""
"""


def text_indentation(text):
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
