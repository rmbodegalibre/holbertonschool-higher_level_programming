#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list2 = my_list
    qtty = len(my_list2)
    for i in range(qtty, 0, -1):
        print("{:d}".format(my_list[i-1]))
