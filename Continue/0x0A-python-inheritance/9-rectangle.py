#!/usr/bin/python3
'''module to ihnerit from basegeomtry class into rectange class'''
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''inherits from BaseGeometry'''
    def __init__(self, width, height):
        '''instantiation with width and height'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''computes the area of the rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''print'''
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
