#!/usr/bin/python3
"""This module defines text_identation() function"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these chars: ., ? and :"""
    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in ['.', '?', ':']:
            print("{}{}".format(text[i], '\n'))
            i += 1
        else:
            print("{}".format(text[i]), end='')
        i += 1
