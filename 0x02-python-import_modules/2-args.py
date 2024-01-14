#!/usr/bin/python3
from sys import argv
length = len(argv) - 1
if length == 0:
    print("{} {}".format(length, 'arguments.'))
if length > 0:
    print("{} {}".format(length, 'argument:' if length == 1 else 'arguments:'))
    for sn, ac in enumerate(argv[1:], 1):
        print("{}: {}".format(sn, ac))
