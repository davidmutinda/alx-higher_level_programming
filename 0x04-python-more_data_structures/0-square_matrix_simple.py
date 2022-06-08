#!/usr/bin/python3
def power(value):
    return value * value


def square_matrix_simple(matrix=[]):
    new_matrix = [[], [], []]
    j = 0
    for row in matrix:
        for i in range(len(matrix)):
            new_matrix[j].append(power(row[i]))
        j += 1
    return new_matrix
