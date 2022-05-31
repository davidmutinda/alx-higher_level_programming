#!/usr/bin/python3
def remove_char_at(str, n):
    if (n < 0):
        return str
    pathOne = str[:n]
    pathTwo = str[n+1:]
    return pathOne + pathTwo
