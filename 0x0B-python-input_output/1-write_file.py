#!/usr/bin/python3
"""

Writes a string
into a file

Func:
    write_file(filename, text)

"""


def write_file(filename="", text=""):
    """function writes into a file"""
    with open(filename, mode="w", encoding="UTF8") as f:
        f.write(text)
    # returns the length of the strings written
    return len(text)
