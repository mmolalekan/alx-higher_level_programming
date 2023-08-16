#!/usr/bin/python3
""" inserts a line of text to a file, after each line containing a string"""

def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each line containing a str"""
    with open(filename, 'r+', encoding='utf-8') as file:
        length = len(search_string)
        string = file.readline()
        for sn, i in enumerate(string):
            if string[sn:length] == search_string:
                file.write(new_string)
