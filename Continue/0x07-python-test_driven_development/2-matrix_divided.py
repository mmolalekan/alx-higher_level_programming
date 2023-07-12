#!/usr/bin/python3
'''A function that divides all elements of a matrix'''


def matrix_divided(matrix, div):
    '''A function that divides all elements of a matrix.
    matrix must be a list of lists of integers or floats, otherwise
    raise a TypeError exception with the message
    matrix must be a matrix (list of lists) of integers/floats.
    '''
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    maxlen = 0
    new_list = []
    for i in range(len(matrix)):
        if len(matrix[i]) > maxlen:
            maxlen = len(matrix[i])

    for i in range(len(matrix)):
        if len(matrix[i]) != maxlen:
            raise TypeError("Each row of the matrix must have the same size")
        inner_list = []
        e = "matrix must be a matrix (list of lists) of integers/floats"
        for j in range(maxlen):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError(e)
            inner_list.append(round(matrix[i][j] / div, 2))
        new_list.append(inner_list)
    return new_list
