#!/usr/bin/python3
def islower(c):
    for alpha in range(97, 123):
        if ord(c) == alpha:
            return True
    return False
