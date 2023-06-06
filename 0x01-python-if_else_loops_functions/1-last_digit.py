#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s1 = " and is greater than 5"
s2 = " and is 0"
s3 = " and is less than 6 and not 0"
if number < 0:
    last = number % -10
else:
    last = number % 10
if last > 5:
    print("Last digit of {} is {}".format(number, last) + s1)
elif last == 0:
    print("Last digit of {} is {}".format(number, last) + s2)
else:
    print("Last digit of {} is {}".format(number, last) + s3)
