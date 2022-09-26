#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        if len(my_list) == 0:
            return 0
        else:
            new_list = set(list(filter(lambda num:str(num).isdigit(), my_list)))
            print(new_list)
            return sum(new_list)


"""
            new_list = list(set(my_list))
            result = 0
            for i in new_list:
                result += i
            return result
"""