#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matix.copy()
    for r in new:
        new[r] = list(map(lambda x: x ** 2, new[r]))
    return new
