#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = []
    idx = 0
    while idx < list_length:
        val = 0
        try:
            val = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except IndexError:
            print("out of range")
            break
        finally:
            idx += 1
            div.append(val)
    return div
