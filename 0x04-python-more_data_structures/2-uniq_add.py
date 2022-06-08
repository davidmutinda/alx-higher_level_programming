#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return
    i, result = 0, 0
    for num in sorted(my_list):
        if num is sorted(my_list)[i - 1]:
            i += 1
            continue
        result += num
        i += 1
    return result
