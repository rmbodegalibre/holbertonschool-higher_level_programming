#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    hid = dir(hidden_4)
    hid.sort()
    for i in hid:
        if "__" not in i:
            print("{}".format(i))
