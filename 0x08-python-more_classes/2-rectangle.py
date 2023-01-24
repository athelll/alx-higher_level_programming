#!/usr/bin/python3
"""
Module: 2-rectangle
"""


class Rectangle:
    """
    Defines a rectangle class

    Args:
        width (int): width
        height (int): height

    Functions:
        __init__(seld,width,height)
        width(self)
        width.setter(seld, value)
        height(self)
        height.setter(self, value)
        area(self)
        perimeter()
    """
    def __init__(self, width=0, height=0):
        """initializes rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """return the area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2*self.height + 2*self.width
