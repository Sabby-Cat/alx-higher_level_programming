#!/usr/bin/python3
"""divide matrix finction"""



def matrix_divided(matrix, div):
    """Divides all elements in matrix"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    l = None
    for r in matrix:
        if type(r) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if l is None:
            l = len(r)
        elif l != len(r):
            raise TypeError("Each row of the matrix must have the same size")
        for c in r:
            if type(c) is not int and type(c) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
                                integers/floats")

    return [[round(c / div, 2) for c in r] for r in matrix]
