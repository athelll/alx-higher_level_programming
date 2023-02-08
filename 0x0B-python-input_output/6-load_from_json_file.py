#!/usr/bin/python3
"""

Load from json file
converts the json string in a file
into a pythonic object

Func:
    load_from_json_file(filename)   
    Return: python object

"""


def load_from_json_file(filename):
    """function that loads for json file"""
    import json
    with open(filename) as f:
        return json.load(f)
