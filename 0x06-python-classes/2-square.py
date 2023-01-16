#!/usr/bin/python3
"""
Module 2-square
Defines a square with specific size
"""


class Square:
    """
    Defines a square object

    Args:
        size: size of square side
    """
    def __init__(self, size=0):
        """
        defines the size of a Square
        size must be positive and an'
        integer

        Args:
            size: must be integer and positive
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
