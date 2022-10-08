#!/usr/bin/python3
"""
5-text_indentacion.py
This program prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines
    after each of these characters: ., ? and :
    text must be a string,
    otherwise raise a TypeError exception with the message:
    "text must be a string"
    There should be no space at the beginning
    or at the end of each printed line
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
        return

    pos = -1
    lng = len(text)
    for i in text:
        pos += 1
        if i == " " and pos == 0:
            continue
        elif i == " " and text[pos-1] in [" ", ".", "?", ":"]:
            continue
        elif i == " " and text[pos+1] in [" ", ".", "?", ":"]:
            continue        
        elif i in [".", "?", ":"]:

            print(i)
            if pos + 1 < lng:
                print()
        else:
            print(i, end="")            
        

"""
    pos = -1
    lng = len(text)
    for i in text:
        pos += 1
        if i == " " and pos == 0:
            continue
        elif i == " " and text[pos-1] in [" ", ".", "?", ":"]:
            continue
        elif i in [".", "?", ":"]:
            print(i)
            if pos + 1 < lng:
                print()
        else:
            print(i, end="")
"""
