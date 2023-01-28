#!/usr/bin/python3
"""Module: 2-is_same_class"""


def is_same_class(obj, a_class):
    """
    function returns a boolean if obj is
    an instance of a_class
    """

    return type(obj) == a_class
