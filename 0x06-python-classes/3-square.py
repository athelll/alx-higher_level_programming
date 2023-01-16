#!/usr/bin/python3
"""
Module 3-square
defines a square with size
"""


class Square:
    """
    Square blueprint class
    
    Args:
        size: size of square
    """
    def __init__(self, size=0):
        """
        initializes a square
        with size __size

        Args:
            size: size of square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """
        returns the area of the square
        """
        return (self.__size)**2
