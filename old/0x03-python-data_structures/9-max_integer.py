#!/usr/bin/python3
def max_integer(my_list=[]):
    if isinstance(my_list, list):
        if my_list == []:
            return None
        max = float('-inf')
        for i in my_list:
            if i > max:
                max = i
        return max
