#!/usr/bin/python3
def print_last_digit(number):
    num = -number
    print("{}".format(num % 10 if number < 0 else number % 10), end="")
    return (num % 10 if number < 0 else number % 10)
