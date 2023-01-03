#!/usr/bin/python3
import sys
import calculator_1 as calc

if __name__ == "__main__":

    argv = sys.argv[1:]
    operators = [["+", calc.add], ["-", calc.sub],
                 ["*", calc.mul], ["/", calc.div]]

    if len(argv) != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    for i, sublist in enumerate(operators):
        for j, element in enumerate(sublist):
            if argv[1] == element:
                result = operators[i][j+1](int(argv[0]), int(argv[2]))
                print('{} {} {} = {}'.format(
                    argv[0], argv[1], argv[2], result))
                exit()

    print('Unknown operator. Available operators: +, -, * and /')
    exit(1)
