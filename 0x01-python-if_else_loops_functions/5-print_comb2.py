#!/usr/bin/python3

for num in range(0, 100):
    if num < 10:
        print('0', end='')
    if num == 99:
        print('99')
        break
    print('{}'.format(num), end=', ')
