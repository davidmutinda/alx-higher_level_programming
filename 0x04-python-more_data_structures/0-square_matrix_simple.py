#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return
    new_matrix = []
    for row in matrix:
        row_matrix = []
        for i in range(len(matrix)):
            row_matrix.append(row[i] ** 2)
        new_matrix.append(row_matrix)

    return new_matrix
