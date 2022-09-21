#!/usr/bin/python3
def uppercase(str):
    for i in str:
        a_char = chr(ord(i) - 32) if 96 < ord(i) < 123 else i
        print("{}".format(a_char), end = "")
    print()
