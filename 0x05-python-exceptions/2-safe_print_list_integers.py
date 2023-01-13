#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    idx = 0
    missed = 0
    while idx < x:
        try:
            print('{:d}'.format(my_list[idx]), end="")
            idx += 1
        except (ValueError, TypeError):
            idx += 1
            missed += 1
            continue
        except IndexError:
            break
    print()
    return (idx - missed)
