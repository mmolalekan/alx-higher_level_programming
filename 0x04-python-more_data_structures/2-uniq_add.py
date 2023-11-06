#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = list(set(my_list))
    sum = 0
    for value in a:
        sum += value
    return sum

"""
from functools import reduce
def uniq_add(my_list=[]):
    return reduce(lambda x,y: x + y, set(my_list), 0)
"""