#!/usr/bin/python3
'''module to implement a class called BaseGeometry'''


class BaseGeometry:
    '''Based on previous tasks'''

    def area(self):
        '''raises an Exception with a custom message'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' validates value '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
