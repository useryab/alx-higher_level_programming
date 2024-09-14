#!/usr/bin/python3


'''
   0-add_integer function

   a function that adds integers
'''


def add_integer(a, b=98):
    '''
    Python function to sum two integers
    '''
    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return int(a) + int(b)
        else:
            raise TypeError('b must be an integer')
    else:
        raise TypeError('a must be an integer')
