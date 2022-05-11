#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniques = []
    sum_uni = 0
    for elem in my_list:
        if elem not in uniques:
            uniques.append(elem)
            sum_uni = sum_uni + elem
    return sum_uni
