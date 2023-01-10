#!/usr/bin/python3
# def search_replace(my_list, search, replace):
#     if my_list is not None:
#         new_list = my_list.copy()
#         for i in new_list:
#             if i is search:
#                 new_list[new_list.index(i)] = replace
#         return new_list
#     return None


# Optimzed version
def search_replace(my_list, search, replace):
    if my_list is not None:
        new_list = [x if x != search else replace for x in my_list]
        return new_list
    return None
