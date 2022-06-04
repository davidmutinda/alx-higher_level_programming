#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in range(0, len(my_list)):
        string = "{:d}"
        print(string.format(my_list[i]))
