#!/usr/bin/python3
for num in range(0, 99):
    print("{}".format('0' + str(num) if num < 10 else num), end=", ")
    num += 1
print("{}".format(num))
