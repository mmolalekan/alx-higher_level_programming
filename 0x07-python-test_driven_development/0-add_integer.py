#!/usr/bin/python3
"""defines a funtion that adds 2 integers"""


def add_integer(a, b=98):
    """returns the addition of 2 integers"""
    if type(a) != int:
        if type(a) == float:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if type(b) != int:
        if type(b) == float:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return (a + b)
