#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        return
    for i in sorted(a_dictionary):
        print("{}: {}".format(i, a_dictionary.get(i)))
