#!/usr/bin/python3
"""defines matrix_divided function"""


def matrix_divided(matrix, div):
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    l_len = len(matrix[0])
    for row in matrix:
        if len(row) != l_len:
            raise TypeError("Each row of the matrix must have the same size")

        for value in row:
            if type(value) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) \
                                of integers/floats")

    return [[round(x / div, 2) for x in row] for row in matrix]
