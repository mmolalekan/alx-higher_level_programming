#!/usr/bin/python3
def remove_char_at(s, n):
    new_string = s[:n] + s[n + 1:]
    return new_string
