#!/usr/bin/python3
"""
saves json repr.
of an object to a file

Func: save_to_json_file(my_obj, filename)

"""


def save_to_json_file(my_obj, filename):
    """func saves json to file"""
    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
