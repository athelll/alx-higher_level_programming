#!/usr/bin/python3
"""
Module: 0-add_integer
returns the summation of 2
numbers
"""


def add_integer(a, b=98):
    """
    func. returns summed args.
        Args: a <int>
              b <int>
    """
    typ = (float, int)
    if type(a) in typ:
        if type(b) in typ:
            return int(a) + int(b)
        else:
            raise TypeError('b must be an integer')
    else:
        raise TypeError('a must be an integer')
