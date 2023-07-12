#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    counter_i = len(matrix)
    counter_j = len(matrix[0])
    if isinstance(matrix, list):
        for i in range(counter_i):
            for j in range(counter_j - 1):
                print("{:d} ".format(matrix[i][j]), end="")
            if counter_j > 0:
                print("{:d}".format(matrix[i][counter_j - 1]))
            else:
                print()
