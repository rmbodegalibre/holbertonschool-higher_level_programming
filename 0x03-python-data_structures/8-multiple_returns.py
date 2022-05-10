#!/usr/bin/python3

def multiple_returns(sentence):

    lngt = len(sentence)

    if lngt == 0:
        frst = None
    else:
        frst = sentence[0]
    return lngt, frst
