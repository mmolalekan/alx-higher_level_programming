#!/usr/bin/python3
"""module documentation"""
import importlib
Base = importlib.import_module('models.base').Base


class Rectangle(Base):
    """class documentation"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """function documentation"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(id)

    @property
    def width(self):
        """func documentation"""
        return self.__width

    @width.setter
    def width(self, value):
        """func documentation"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """func documentation"""
        return self.__height

    @height.setter
    def height(self, value):
        """func documentation"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """func documentation"""
        return self.__x

    @x.setter
    def x(self, value):
        """func documentation"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """func documentation"""
        return self.__y

    @y.setter
    def y(self, value):
        """func documentation"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """function documentation"""
        return self.__width * self.__height

    def display(self):
        """function documentation"""
        for a in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(' ', end='')
            for k in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """function documentation"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """function documentation"""
        if args and len(args) > 0:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for attr, arg in zip(attrs, args):
                setattr(self, attr, arg)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """function documentation"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
