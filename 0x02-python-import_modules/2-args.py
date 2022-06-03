#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    length = len(argv)
    if length == 1:
        print("{} arguments.".format(length - 1))

    else:
        print("{} {}".format(length - 1, "argument:\
" if length == 2 else "arguments:"))

        for i in range(1, length):
            print("{}: {}".format(i, argv[i]))
