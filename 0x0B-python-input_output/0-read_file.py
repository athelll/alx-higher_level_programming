#!/usr/bin/python3
"""Read_File"""


def read_file(filename=""):
    """function that reads file"""
    with open(filename, mode="r", encoding="UTF8") as file:
        """prints the file"""
        print(file.read())
