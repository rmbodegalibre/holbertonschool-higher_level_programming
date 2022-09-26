#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):

    def multiplyBy(num):
        #return num * number
        return num * number

    multipliedNumbers = list(map(multiplyBy, my_list))
    return multipliedNumbers
