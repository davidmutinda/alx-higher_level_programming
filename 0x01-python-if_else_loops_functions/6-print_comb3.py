#!/usr/bin/python3
for i in range(0, 89):
    if i / 10 >= i % 10:
        i += 1
        continue
    print("{}".format('0' + str(i) if i < 10 else i), end=", ")
    i += 1

print("{}".format(i))
