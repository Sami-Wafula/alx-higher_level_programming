#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for i in number:
    if number > 0:
        print("is positive")
    elif number < 0:
        print("is negative")
    else:
        print("is zero")

