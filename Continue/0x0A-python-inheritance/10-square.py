#!/usr/bin/python3
'''module to inherit from Rectangle class into Square class'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''inherits from Rectangle'''
    def __init__(self, size):
        '''instantiation with size'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
