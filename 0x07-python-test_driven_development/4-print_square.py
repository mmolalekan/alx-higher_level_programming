#!/usr/bin/python3
"""this module defines print_square function"""


def print_square(size):
    """prints a square with the character #"""
    if type(size) != int or (type(size) == float and size < 0):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for i in range(size):
            print("{}".format('#'), end='')
        print()
