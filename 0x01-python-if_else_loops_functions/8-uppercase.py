#!/usr/bin.python3
def uppercase(s):
    for i in s:
        print(
            "{}".format(
                chr(ord(i) - 32)
                if ord(i) >= 97 and ord(i) <= 122
                else i),
            end='')
    print()
