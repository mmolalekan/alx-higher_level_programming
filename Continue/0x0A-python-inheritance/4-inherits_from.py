#!/usr/bin/python3
'''implements a function that checks is an object
is an instance if a class that inherited from the specified class'''


def inherits_from(obj, a_class):
    '''returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.
    '''
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    False
