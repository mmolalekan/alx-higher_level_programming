#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    key, best = 'temp', 0
    for k, v in a_dictionary.items():
        if v > best:
            key = k
            best = v
    return key
