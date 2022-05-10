#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list is None:
        return
    list_val = []
    for item in my_list:
        list_val.append(item % 2 == 0)
    return list_val
