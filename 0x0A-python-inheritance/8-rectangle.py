#!/usr/bin/python3
"""defines an empty class BaseGeometry"""


class BaseGeometry:
    """defines an empty class BaseGeometry"""

    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """defines a new class inheriting from an existing class"""

    def __init__(self, width, height):
        """instantiation with variables"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
