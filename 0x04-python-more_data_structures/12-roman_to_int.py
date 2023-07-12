#!/usr/bin/python3
def roman_to_int(roman_string):
    r_str = roman_string
    if not isinstance(r_str, str) or r_str is None:
        return 0
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total, i = 0, 0
    while i < len(r_str):
        if i + 1 < len(r_str) and my_dict[r_str[i + 1]] > my_dict[r_str[i]]:
            total += my_dict[r_str[i + 1]] - my_dict[r_str[i]]
            i += 2
        else:
            total += my_dict[r_str[i]]
            i += 1
    return total
