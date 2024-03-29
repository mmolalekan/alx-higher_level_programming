#!/usr/bin/python3
"""defines a function that adds a new attribute to an object"""


def add_attribute(obj, attr_name, value):
    """ adds a new attribute to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, value)
