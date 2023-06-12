#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    counter_i = len(matrix)
    counter_j = len(matrix[0])

    for i in range(counter_i):
        for j in range(counter_j - 1):
            print("{} ".format(matrix[i][j]), end="")
        if counter_j > 0:
            print("{}".format(matrix[i][counter_j - 1]))
        else:
            print()
