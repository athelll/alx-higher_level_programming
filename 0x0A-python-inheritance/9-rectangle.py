#!/usr/bin/python3
"""
Module: 8-rectangle

Contains parent class BaseGeometry

Contains subclass Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry
    Methods:
        __init_(self, width, height)
    """
    def __init__(self, width, height):
        """initializes the width and height
        Args:
            width(int)
            height(int)
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """extend parents empty class and returns the area"""
        return (self.__height * self.__width)

    def __str__(self) -> str:
        """returns the string [Rectangle] <width>/<height>"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
