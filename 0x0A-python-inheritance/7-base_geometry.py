#!/usr/bin/python3
"""
Module: 7-base_geometry
Class: BaseGeometry
"""


class BaseGeometry:
    """
    BaseGeometry

    Functions:
        area(self)
        integer_validator(self, name, value)
    """
    def area(self):
        """raise an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates if an value is aninteger"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
