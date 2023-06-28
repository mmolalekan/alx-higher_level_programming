#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
