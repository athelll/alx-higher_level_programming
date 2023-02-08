#!/usr/bin/python3
"""
saves json repr.
of an object to a file

Func: save_to_json_file(my_obj, filename)

"""


def save_to_json_file(my_obj, filename):
    """sfunc saves json to file"""
    import json
    parsed_json = json.dumps(my_obj)

    with open(filename, mode="w") as f:
        f.write(parsed_json)
