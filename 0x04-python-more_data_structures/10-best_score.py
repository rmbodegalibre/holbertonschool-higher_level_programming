#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary:
        b_score = 0
        b_key = ""
        for key, value in a_dictionary.items():
            if value > b_score:
                b_score = value
                b_key = key
        return b_key
    else:
        return None
