#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    qtty = 0
    try:
        for elem in range(0, x):
            qtty = qtty + 1
            print(f"{my_list[elem]}", end="")
    except IndexError:
        qtty = qtty - 1
        return qtty
    else:
        return qtty
    finally:
        print("")
