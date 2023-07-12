#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda row: [value ** 2 for value in row], matrix))
