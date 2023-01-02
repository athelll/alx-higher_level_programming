#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if((num % 3 == 0) & (num % 5 == 0)):
            print('FizzBuzz', end=' ')
            continue
        if num % 3 == 0:
            print('Fizz', end=' ')
            continue
        if num % 5 == 0:
            print('Buzz', end=' ')
            continue
        print(num, end=' ')
