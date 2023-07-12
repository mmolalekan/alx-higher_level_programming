#!/usr/bin/python3
'''
def search_replace(my_list, search, replace):
    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
            continue
        new_list.append(item)
    return new_list

def search_replace(my_list, search, replace):
    return [replace if item == search else item for item in my_list]
'''


def search_replace(my_list, search, replace):
    return list(map(lambda item: replace if item == search else item, my_list))
