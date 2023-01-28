#!/usr/bin/python3
"""
Module: 10-square

Inherits from 9-rectangle.py
The Class Rectangle

"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """inherits from the rectangle class
    Methods:
        __init__(self,size)
    """
    def __init__(self, size):
        """initializes the Square class
        Args:
            size (int): private
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        super().area()
