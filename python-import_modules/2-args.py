#!/usr/bin/python3
import sys

py_args = sys.argv
py_args.pop(0)
py_len = len(py_args)
j = 0

if py_len == 1:
    print("1 argument:")
elif py_len == 0:
    print("{} arguments.".format(py_len))
else:
    print("{} arguments:".format(py_len))

for i in py_args:
    j += 1
    print("{}: {}".format(j, i))
