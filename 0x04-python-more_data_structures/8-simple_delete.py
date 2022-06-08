#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for k in a_dictionary:
        if k is key:
            a_dictionary.pop(key)
            break
    return a_dictionary
