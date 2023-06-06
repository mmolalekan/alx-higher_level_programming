#!/usr/bin/python3
def remove_char_at(s, n):
    strlen = len(s)
    j = 0;
    for i in range(0, strlen - 1):
        if i == n:
            j -= 1
            continue
        else:
            string[j] = s[i]
            j += 1
    print(string)
