#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for num in a_dictionary:
        if num is key:
            a_dictionary[key] = value
            return a_dictionary
    a_dictionary[key] = value
    return a_dictionary
