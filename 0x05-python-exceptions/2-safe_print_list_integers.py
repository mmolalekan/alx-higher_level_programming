#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = j = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end='')
        except (TypeError, ValueError):
            j += 1
            pass
        i += 1
    print()
    return i - j
