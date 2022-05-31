#!/usr/bin/python3
def rec(a, b):
    power = a
    while b < -1:
        power *= a
        b += 1
    return 1 / power


def pow(a, b):
    power = a
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b < 0:
        return rec(a, b)
    while b > 1:
        power *= a
        b -= 1
    return power
