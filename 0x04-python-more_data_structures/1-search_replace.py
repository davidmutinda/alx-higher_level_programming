#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(replace if search is i else i for i in my_list)
    return new_list
