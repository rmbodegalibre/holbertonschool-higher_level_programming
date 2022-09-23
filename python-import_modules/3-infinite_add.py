#!/usr/bin/python3
import sys

if __name__ == "__main__":
    py_args = sys.argv
    py_args.pop(0)
    py_len = len(py_args)
    j = 0

    if py_len == 0:
        print("{}".format(j))
    else:
        for i in py_args:
            j += int(i)
        print("{}".format(j))
