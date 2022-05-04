#!/usr/bin/python3

def uppercase(str):
    for char in str:
        asc = ord(char)
        if asc > 96 and asc < 123:
            char = chr(asc - 32)
        print(f"{char}", end="")
    print("")
