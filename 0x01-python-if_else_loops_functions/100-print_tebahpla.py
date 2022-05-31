#!/usr/bin/python3
def printFunc(value):
    print("{}".format(value), end='')


for i in range(0, 26):
    if i % 2 == 0:
        printFunc(chr(ord('z') - i))

    else:
        printFunc(chr(ord('Z') - i))
