#!/usr/bin/python3
"""
finds the peak in an unsorted
list of integers
"""


def find_peak(list_of_integers):
    """
    finds the peak using
    sn algorithm very similar to binary
    search
    """

    lst = list_of_integers
    n = len(lst)

    if n == 0:
        return None
    elif n == 1:
        return lst[0]
    # checks if first and last are the peak
    elif lst[0] >= lst[1]:
        return lst[0]
    elif lst[n-1] >= lst[n-2]:
        return lst[n-1]
    else:
        # checks the list excluding the
        # first amd last since they've already
        # been taken care of
        left, right = 1, n-2
        while left <= right:
            # gets the midpoint where the binary search will begin
            mid = (left + right)//2
            # check if a peak and returns
            if lst[mid] >= lst[mid - 1] and lst[mid] >= lst[mid + 1]:
                return lst[mid]
            # shifts the list to the left or right
            # by reducing the size depending on the
            # state of the current midpoint
            elif lst[mid] < lst[mid - 1]:
                right = mid - 1
            else:
                left = mid + 1
