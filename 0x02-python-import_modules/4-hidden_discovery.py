#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    new = dir(hidden_4)
    for i in range(0, len(new)):
        if new[i][:2] != "__":
            print("{}".format(new[i]))
