#!/usr/bin/python3
'''returns the JSON representation of an object '''
import json


def from_json_string(my_str):
    '''returns the JSON representation of an object (string)'''
    return json.loads(my_str)
