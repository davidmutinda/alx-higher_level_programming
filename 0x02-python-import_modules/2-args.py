#!/usr/bin/python3
import sys
i = 1
if len(sys.argv) == 1:
    print("{} arguments".format(0))

else:
    print("{} {}".format(len(sys.argv) - 1, "argument.\
" if len(sys.argv) == 2 else "arguments:"))

    while i < len(sys.argv):
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
