#!/usr/bin/python3
'''empty class Rectange that defines a rectangle
'''


class Rectangle():
    '''the funcion that defines Rectangle'''

    def __init__(self, width=0, height=0):
         """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the Rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __str__(self):
        
