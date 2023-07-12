#!/usr/bin/python3
'''defines a function that reads text file'''


def read_file(filename=""):
    ''' reads a text file (UTF8) and prints it to stdout'''
    with open(filename, encoding='utf-8') as my_file:
        read_data = my_file.read()
        print(read_data)
