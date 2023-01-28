#!/usr/bin/python3
"""
Module: 101-add_attribute

Contains functuon that adds an attribute to
an object
"""


def add_attribute(obj, name, value):
    """adds a non existing attributes to an object"""
    if '__dict__' in dir(obj):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
