#!/usr/bin/python3

def common_elements(set_1, set_2):
    com = []
    for elem in set_1:
        if elem in set_2:
            com.append(elem)
    return com
