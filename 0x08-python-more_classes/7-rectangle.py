#!/usr/bin/python3
"""defines a rectangle class."""


class Rectangle:
    """defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialises the rectangle values"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """get/set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get/set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """string representation"""
        if self.__width == 0 or self.__height == 0:
            return ""
        new_list = []
        for i in range(self.__height):
            for j in range(self.__width):
                new_list.append(str(self.print_symbol))
            if i != self.__height - 1:
                new_list.append('\n')
        return "".join(new_list)

    def __repr__(self):
        """string representation"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """print a message for evebry deletion of a rectangle"""
        type(self).number_of_instances -= 1
        print("{}".format("Bye rectangle..."))
