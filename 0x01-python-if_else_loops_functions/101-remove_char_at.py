#!/usr/bin/python3
def remove_char_at(str, n):
    pathOne = str[:n]
    pathTwo = str[n+1:]
    return pathOne + pathTwo
