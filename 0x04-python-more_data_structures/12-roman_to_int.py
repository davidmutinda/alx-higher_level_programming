#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0
    integer, prev = 0, 1000
    dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    for char in roman_string:
        for key, value in dictionary.items():
            if char is key:
                if prev < value:
                    integer += value - (2 * prev)
                else:
                    integer += value
                prev = value
                break

    return integer
