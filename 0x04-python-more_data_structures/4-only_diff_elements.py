#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if not set_1 or not set_2:
        return
    notCommon = set()
    for char in set_1:
        i = 0
        for new in set_2:
            if new is char:
                break
            elif i is len(set_2) - 1:
                notCommon.add(char)
            i += 1
    for char in set_2:
        i = 0
        for new in set_1:
            if new is char:
                break
            elif i is len(set_1) - 1:
                notCommon.add(char)
            i += 1

    return notCommon
