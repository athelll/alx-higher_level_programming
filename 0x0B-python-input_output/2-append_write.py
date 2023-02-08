#!/usr/bin/python3
"""

Append a string to
a file

Func:
    append_write(filename, text)

"""


def append_write(filename="", text=""):
    """appends to the file"""
    with open(filename, mode="a", encoding="UTF8") as f:
        f.write(text)
    return len(text)
