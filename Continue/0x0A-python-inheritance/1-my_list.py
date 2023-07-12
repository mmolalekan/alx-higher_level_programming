#!/usr/bin/pyhton3
'''This module creates a class called MyList
'''


class MyList(list):
    '''a class MyList that inherits from list'''
    def print_sorted(self):
        '''pritns the list but sorted'''
        print(sorted(self))
