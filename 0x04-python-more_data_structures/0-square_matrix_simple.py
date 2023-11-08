#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()
    for r in range(len(new)):
        new[r] = list(map(lambda x: x ** 2, new[r]))
    return new
