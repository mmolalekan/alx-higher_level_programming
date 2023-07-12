#!/usr/bin/python3
''' defines integer addition function.'''


def add_integer(a, b=98):
    '''returns the addition of a and b
    if a or b is float, typecast before returning sum
    if a or b is not int or float, raise TypeError Exception
    '''

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
