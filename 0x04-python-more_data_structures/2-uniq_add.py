#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return
    result = my_list[0]
    j = 0
    for num in my_list:
        for i in range(j):
            if my_list[i] is num:
                break
            elif i is j - 1:
                result += num
        j += 1
    return result
