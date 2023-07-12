#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    num = denom = 0
    for x, y in my_list:
        num += x * y
        denom += y
    return (num / denom)
