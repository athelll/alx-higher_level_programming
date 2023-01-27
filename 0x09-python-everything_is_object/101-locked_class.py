#!/usr/bin/python3
"""
Module: 101-locked_class
Creates a locked class
"""

class LockedClass:
    """
    only allows the instance attribute
    'first_name' to be created
    """

    __slots__ = "first_name"
