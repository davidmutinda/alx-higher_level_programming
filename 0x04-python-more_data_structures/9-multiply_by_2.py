#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_list = list(a_dictionary[key] * 2 for key in a_dictionary)
    i = 0
    new_dict = {}
    for key in a_dictionary:
        new_dict[key] = new_list[i]
        i += 1
    return new_dict
