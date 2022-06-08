#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maxValue = 0
    maxKey = ""
    for key in a_dictionary:
        if a_dictionary[key] > maxValue:
            maxValue = a_dictionary[key]
            maxKey = key
    return maxKey
