#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = []
    idx = 0
    while idx < list_length:
        try:
            div.append(my_list_1[idx] / my_list_2[idx])
        except (ZeroDivisionError, ValueError):
            print("division by 0")
            div.append(0)
        except TypeError:
            print("wrong type")
            div.append(0)
        except IndexError:
            print("out of range")
            div.append(0)
            break
        finally:
            idx += 1
    return div
