#!/usr/bin/python3
def print_last_digit(number):
    if (number > 0):
        lastdigit = number % 10
    elif (number % 10 == 0):
        lastdigit = 0
    else:
        lastdigit = 10 - (number % 10)
    print(lastdigit, end='')
    return(lastdigit)
