#!/usr/bin/python3
'''
def square_matrix_simple(matrix=[]):
    return [[value**2 for value in row] for row in matrix]

def square_matrix_simple(matrix=[]):
    new_list = []
    for row in matrix:
        list_row = []
        for value in row:
            list_row.append(value**2)
        new_list.append(list_row)
    return new_list
'''


def square_matrix_simple(matrix=[]):
    return list(map(lambda row: [value**2 for value in row], matrix))
