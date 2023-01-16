#!/usr/bin/python3
"""
Module 1-square
Defines a square with size attributes
"""


class Square:
    """
    defines a square class

    Args:
        size: size of a square side
    """

    def __init__(self, size):
        """initaializes the size attribute

        Attribues:
            size: size of a side of a square
        """

        self.__size = size
