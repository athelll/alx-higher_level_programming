#!/usr/bin/python3
def uppercase(str):
    for chars in str:
        if ord('a') <= ord(chars) <= ord('z'):
            chars = chr(ord(chars) - ord('a') + ord('A'))
        print('{}'.format(chars), end='')
    print()
