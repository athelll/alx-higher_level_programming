#!/usr/bin/python3
"""Module: 4-inherits_from"""


def inherits_from(obj, a_class):
    """checks if a subclass"""
    return (type(obj) is not a_class and issubclass(obj, a_class))
