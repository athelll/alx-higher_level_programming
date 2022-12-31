#!/usr/bin/python3
for c in range(ord('a'), ord('z')+1):
    if (c == ord('q')) | (c == ord('e')):
        continue
    print('{}'.format(chr(c)), end='')
