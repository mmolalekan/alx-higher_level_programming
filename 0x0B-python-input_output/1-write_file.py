#!/usr/bin/python3
"""writes a string to a txt file (UTF8) and returns the no of chars written"""


def write_file(filename="", text=""):
    """returns the no of chars written"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
