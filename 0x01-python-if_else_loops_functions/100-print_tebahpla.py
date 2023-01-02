#!/usr/bin/python3
tracker = 0
for s in range(ord('z'), ord('a')-1, -1):
    if (tracker % 2 != 0):
        s = s - ord('a') + ord('A')
    print(chr(s), end='')
    tracker += 1
