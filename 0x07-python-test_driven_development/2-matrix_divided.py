#!/usr/bin/python3
"""
This module defines `matrix_divided`
The function returns the matrix divided by div
"""


def matrix_divided(matrix, div):
    """divide each element of a matrix by div
    Args:
        matrix (list): matrix to divide
        div (int): divisor
    Raises:
        TypeError: div must be a number
        TypeError: Each row of the matrix must have the same size
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        ZeroDivisionError
    Returns:
        list: matrix divided by div
    """

    if not isinstance(matrix, list) or not len(matrix):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    row_length = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        row_length.append(len(row))
        col = []
        for key in row:
            if not isinstance(key, (int, float)):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
            col.append(round(key / div, 2))
        new_matrix.append(col)
    for i in row_length:
        if i != row_length[0]:
            raise TypeError("Each row of the matrix must have the same size")

    return new_matrix
