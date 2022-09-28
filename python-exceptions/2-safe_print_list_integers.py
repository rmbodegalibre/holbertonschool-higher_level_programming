#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if my_list and x > 0:
        pos = 0
        for i in range(0, x):
            if isinstance(my_list[i], int):
                try:
                    print("{:d}".format(my_list[i]), end="")
                    pos += 1
                except TypeError:
                    print("", end="")
        print()
        return pos
