#!/usr/bin/python3
"""
Module: 100-my_int
creates a rebellious version of the
'==' and '!=' operators
"""


class MyInt(int):
    """inherits from int"""
    def __init__(self, num):
        """initialization"""
        self.num = num

    def __eq__(self, other):
        """reverses the equality boolean return"""
        return self.num != other

    def __ne__(self, other):
        """reverses the inequality boolean return"""
        return self.num == other
