#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    idx = 0
    value = 0
    while x:
        try:
            print("{:d}".format(my_list[idx]), end="")
            value += 1
        except ValueError:
            idx += 1
            x -= 1
            continue
        except TypeError:
            idx += 1
            x -= 1
            continue
        idx += 1
        x -= 1
    print("")
    return value
