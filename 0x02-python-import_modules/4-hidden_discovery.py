#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    i = 0
    new = dir(hidden_4)
    while i < len(new)):
        if new[i][:2] != "__":
            print("{}".format(new))
        i += 1
