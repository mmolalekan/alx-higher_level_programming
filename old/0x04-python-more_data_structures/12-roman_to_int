#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_list = list(roman_string)
    total = curr = prev = 0
    sum_list = []
    for c in roman_list:
        if c == 'I':
            sum_list.append(1)
        elif c == 'V':
            sum_list.append(5)
        elif c == 'X':
            sum_list.append(10)
        elif c == 'L':
            sum_list.append(50)
        elif c == 'C':
            sum_list.append(100)
        elif c == 'D':
            sum_list.append(500)
        elif c == 'M':
            sum_list.append(1000)

    for i in sum_list:
        curr = i
        if len(sum_list) == 1:
            return i
        elif curr > prev: 
            total += curr - (2 * prev)
        else:
            total += curr
        prev = curr
    return total
