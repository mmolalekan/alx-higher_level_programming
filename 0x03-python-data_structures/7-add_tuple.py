#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if isinstance(tuple_a, tuple) and isinstance(tuple_b, tuple):
        a = [0, 0]
        b = [0, 0]
        for index, i in enumerate(tuple_a):
            a[index] = tuple_a[index]

        for index, i in enumerate(tuple_b):
            b[index] = tuple_b[index]
        sum_a = a[0] + b[0]
        sum_b = a[1] + b[1]
        return (sum_a, sum_b)
