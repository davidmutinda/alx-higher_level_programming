#!/usr/bin/python3
for num in range(0, 99):
    if num < 10:
        num = '0' + str(num)
    print("{}".format(num), end=", ")
    num = int(num)
    num += 1
print("{}".format(num))
