#!/usr/bin/python3
"""
Module 5-text_indentation
Contains method that prints text with 2 new lines after each ".", "?", and ":"
Takes in a string
"""

def text_indentation(text):
    """
    Prints text with 2 new lines after each ".", "?", and ":"
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    stripped_text = text.strip()
    new_text = ''
    add = ''
    for i in stripped_text:
        if i in ['?',':','.']:
            add += i
            add = add.strip()
            new_text += add + '\n\n'
            add = ''
        else:
            add += i
    new_text += add.strip()
    print(new_text, end='')
