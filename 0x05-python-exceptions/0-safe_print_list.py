#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    try:
        while x:
            print("{}".format(my_list[index]), end="")
            x -= 1
            index += 1
    except IndexError:
        print("")
        return index
    print("")
    return index
