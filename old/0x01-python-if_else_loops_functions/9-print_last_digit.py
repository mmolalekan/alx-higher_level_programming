#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
        dec = (number % 10)
    else:
        dec = number % 10
    print(dec, end="")
    return (dec)
