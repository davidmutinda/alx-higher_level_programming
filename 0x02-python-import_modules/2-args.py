#!/usr/bin/python3
from sys import argv
i = 1
if len(argv) == 1:
    print("{} arguments".format(0))

else:
    print("{} {}".format(len(argv) - 1, "argument:\
" if len(argv) == 2 else "arguments:"))

    while i < len(argv):
        print("{}: {}".format(i, argv[i]))
        i += 1
