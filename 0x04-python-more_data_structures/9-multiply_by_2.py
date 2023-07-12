#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    '''
    implementation_1
    new_dict = {}
    for k, v in a_dictionary.items():
        new_dict[k] = v * 2
    return new_dict
    '''
    return dict((k, v * 2) for (k, v) in a_dictionary.items())
