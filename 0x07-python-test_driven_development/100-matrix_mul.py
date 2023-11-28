#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices."""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(type(row) == list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(type(row) == list for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all((type(el) == int or type(el) == float)
               for el in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((type(el) == int or type(el) == float)
               for el in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    invert_b = []
    for r in range(len(m_b[0])):
        n_row = []
        for c in range(len(m_b)):
            n_row.append(m_b[c][r])
        invert_b.append(n_row)
    n_mat = []
    for row in m_a:
        n_row = []
        for col in invert_b:
            prod = 0
            for i in range(len(invert_b[0])):
                prod += row[i] * col[i]
            n_row.append(prod)
        n_mat.append(n_row)
    return n_mat
