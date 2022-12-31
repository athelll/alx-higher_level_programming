#!/usr/bin/python3
count = 1
for num in range(9):
    dig = count 
    while dig < 10:
        if (num == dig):
            continue
        if (num == 8) & (dig == 9):
            print('89')
            break
        print('{}{}'.format(num, dig), end=', ')
        dig += 1
    count += 1
