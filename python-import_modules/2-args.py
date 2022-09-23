#!/usr/bin/python3
import sys

#if __name__ == "__main__":
py_args = sys.argv
py_args.pop(0)
py_len = len(py_args)
j = 0

if py_len == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(py_len))

for i in py_args:
    j += 1
    print("{}: {}".format(j, i)) 
