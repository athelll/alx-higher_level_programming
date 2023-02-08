#!/usr/bin/python3
"""form_json_string"""


def from_json_string(my_str):
    """json to string"""
    import json
    return json.loads(my_str)
