#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = -1 if number < 0 else 1
last_d = (abs(number) % 10) * sign
if last_d > 5:
    print(f"Last digit of {number} is {last_d} and is greater than 5")
elif last_d > 0 or last_d < 0:
    print(f"Last digit of {number} is {last_d} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last_d} and is 0")
