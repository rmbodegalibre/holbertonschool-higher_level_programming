#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    first_c = "None" if lenght == 0 else sentence[0]
    return lenght, first_c
