#!/usr/bin/python3
def remove_char_at(s, n):
    string = ''
    for i in range(0, len(s)):
        if i != n:
            string += s[i]
    return (string)
