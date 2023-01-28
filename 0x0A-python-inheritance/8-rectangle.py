#!/usr/bin/python3
"""
Module: 8-rectangle
"""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry

class Rectangle(BaseGeometry):
    """BaseGeometry"""
    def __init__(self, width, height):
        super().integer_validator(self, "width", self.__width)
        self.__width = width
        super().integer_validator(self, "height", self.__height)
        self.__height = height
