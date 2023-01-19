#!/usr/bin/python3
"""
Module: 3-say_my_name
Function that prints
first and last names
"""


def say_my_name(first_name, last_name=""):
    """
    Func: say_my_name
    Function says your name
        Args: first_name <str>,
              last_name <str>

    <Obvious Breaking Bad refrence>
    """
    if isinstance(first_name, str) and isinstance(last_name, str):
        print('My name is {} {}'.format(first_name, last_name))
    else:
        raise TypeError('{} must be a string'.
                        format('first_name' if isinstance(last_name, str)
                               else 'last_name'))
