#!/usr/bin/python3
def common_elements(set_1, set_2):
    if not set_1 or not set_2:
        return
    common = set()
    for num in set_1:
        for com in set_2:
            if num is com:
                common.add(num)
                break
    return common
