#!/usr/bin/python3
"""
Module: 8-rectangle

Contains parent class BaseGeometry

Contains subclass Rectangle
"""


BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry
    Methods:
        __init_(self, width, height)
    """
    def __init__(self, width, height):
        """initializes the rectangle with 
        width and height

        Args:
            width(int)
            height(int)
        """
        super().integer_validator("width", self.__width)
        self.__width = width
        super().integer_validator("height", self.__height)
        self.__height = height
