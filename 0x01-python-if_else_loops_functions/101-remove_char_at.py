#!/usr/bin/python3
def remove_char_at(s, n):
    if n < 0:
        return s
    new_string = s[:n] + s[n + 1:]
    return new_string
