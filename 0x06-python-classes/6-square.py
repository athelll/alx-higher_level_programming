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
    def __init__(self, size=0, position=(0, 0)):
        """
        initializes a square
        with size __size

        Args:
            size: size of square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        getter for position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) == 2 and\
           type(value[0]) is int and type(value[1]) is int and\
           value[0] > 0 and value[1] > 0:
            self.__position = position
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def my_print(self):
        """
        This prints the Area of the Square
        """
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            print('\n'.join([' ' * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)]))
