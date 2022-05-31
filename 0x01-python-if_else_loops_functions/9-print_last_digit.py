#!/usr/bin/python3
def print_last_digit(number):
    string = str(number)
    number = int(string[-1])
    print("{}".format(number), end='')
    return number
