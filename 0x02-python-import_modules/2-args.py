#!/usr/bin/python3
from sys import argv

argc = len(argv) - 1
index = 1

if argc == 0:
    print('{} arguments.'.format(argc))
elif argc == 1:
    print('{} argument:'.format(argc))
else:
    print('{} arguments:'.format(argc))

for args in argv[1:]:
    print('{}: {}'.format(index, args))
    index += 1
