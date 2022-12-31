#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

#algorithm to calculate last digit of number
if (number > 0):
    lastdigit = number % 10
elif (number % 10 == 0):
    lastdigit = 0
else:
    lastdigit = 10 - (number % 10)

#algorithm to print number last digit and state
if lastdigit > 5:
    print (f'Last digit of {number} is {lastdigit} and is greater than 5')
elif (lastdigit < 6) & (lastdigit != 0):
    print (f'Last digit of {number} is {lastdigit} and is less than 6 and not 0')
elif lastdigit == 0:
    print (f'Last digit of {number} is {lastdigit} and is 0')
