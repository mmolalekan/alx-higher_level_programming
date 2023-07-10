#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """Square class based on 3-square.py"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        elif isinstance(value, int):
            self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparision to a Square."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Define the > comparision to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparision to a Square."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Define the < comparision to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparision to a Square."""
        return self.area() <= other.area()
