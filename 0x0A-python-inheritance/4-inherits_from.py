#!/usr/bin/python3
"""
returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.

    # method 1
    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    return False
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
