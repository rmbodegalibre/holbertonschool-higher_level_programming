#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return (0)
    else:
        nr = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        itg = 0
        ant = 0
        for i in roman_string:
            itg -= ant * 2 if ant < nr[i] else 0
            itg += nr[i]
            ant = nr[i]
        return itg
