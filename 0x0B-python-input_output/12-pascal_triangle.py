#!/usr/bin/python3
"""
Module contains pascal_triangle function
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle

    Args:
        n(int) : size of triangle
    """
    if n <= 0:
        return list()

    new_list = []
    for i in range(n):
        col = []
        for k in range(i + 1):
            if not k or k == i:
                col.append(1)

            else:
                col.append(new_list[i - 1][k] + new_list[i - 1][k - 1])
        new_list.append(col)

    return new_list
