#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return
    new_matrix = [[], [], []]
    j = 0
    for row in matrix:
        for i in range(len(matrix)):
            new_matrix[j].append(row[i] ** 2)
        j += 1
    return new_matrix
