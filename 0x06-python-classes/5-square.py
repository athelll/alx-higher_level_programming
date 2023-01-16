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

    @property
    def size(self):
        """
        This is the setter of the function
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is the getter of the function
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):
        """
        This prints the Area of the Square
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print(self.__size*'#')
