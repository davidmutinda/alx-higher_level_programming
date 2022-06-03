#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) == 0:
        a = 0
        b = 0
    elif len(tuple_b) == 1:
        a = tuple_b[0]
        b = 0
    else:
        a = tuple_b[0]
        b = tuple_b[1]
    tuple_c = (tuple_a[0] + a, tuple_a[1] + b)
    return tuple_c
