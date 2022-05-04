#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = abs(number) % 10
criteria = "Nothing"
if lastd > 5:
    criteria = "and is greater than 5"
elif lastd == 0:
    criteria = "and is 0"
else:
    criteria = "and is less than 6 and not 0"
print(f"Last digit of {number} is {lastd} {criteria}")
