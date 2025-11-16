#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
b = str(number)
a = b[-1]
a = int(a)
if a > 5:
    print(f'Last digit of {number} is {a} and is greater than 5')
elif a == 0:
    print(f'Last digit of {number} is {a} and is 0')
elif a < 6 & a != 0:
    print(f'Last digit of {number} is {a} and is and is less than 6 and not 0')
