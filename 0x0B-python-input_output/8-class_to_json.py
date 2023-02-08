#!/usr/bin/python3
"""

Function that returns the dictionary
description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object

Function: class_to_json
        returns: dictionary of obj

"""


def class_to_json(obj):
    """returns dict of class"""
    return obj.__dict__
