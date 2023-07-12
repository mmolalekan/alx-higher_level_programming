#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary)
    for value in keys:
        print("{}: {}".format(value, a_dictionary[value]))
