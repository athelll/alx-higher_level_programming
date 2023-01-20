#!/usr/bin/python3
"""
Module: 4-print_square
prints square
"""


def print_square(size):
    """
    print_square function
        Args: size <int>
    """
    if type(size) is not int or (isinstance(size, float) and size < 0):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')

    if size == 0:
        print("", end="")
    else:
        print('\n'.join('#'*size for i in range(size)))
