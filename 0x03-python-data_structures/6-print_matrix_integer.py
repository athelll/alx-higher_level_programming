#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for digit in row:
            if digit == row[-1]:
                print('{:d}'.format(digit), end='')
            else:
                print('{:d}'.format(digit), end=' ')
        print()
