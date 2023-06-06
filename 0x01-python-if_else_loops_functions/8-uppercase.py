#!/usr/bin/python3
def uppercase(s):
    for i in range(len(s)):
        print("{:c}".format(ord(s[i]) - 32 if (ord(s[i]) >= 97 and ord(s[i]) <= 122) else (ord(s[i]))), end="")
    print("")
