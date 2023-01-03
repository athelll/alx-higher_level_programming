#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv = argv[1:]
    if len(argv) == 0:
        print('0 arguments.')
    elif len(argv) == 1:
        print('1 argument:')
    else:
        print('{} arguments:'.format(len(argv)))
    for i, args in enumerate(argv):
        print('{:d}: {:s}'.format(i+1, args))
