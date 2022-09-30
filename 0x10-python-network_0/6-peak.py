#!/usr/bin/python3
"""
Module contains find_peak()
"""


def find_peak(list_of_integers):
    """
     finds a peak in a list of unsorted integers
    """
    array = list_of_integers
    if not array:
        return None
    if len(array) == 1:
        return array[0]
    peak = None
    if array[0] >= array[1]:
        peak = array[0]
    if array[-1] >= array[-2]:
        peak = array[-1]
    for count, item in enumerate(array):
        try:
            if item >= array[count - 1] and item >= array[count + 1]:
                if not peak:
                    peak = item
                if item > peak:
                    peak = item
        except Exception:
            pass

    return peak
