#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count = len(argv)
    add = 0
    if count == 1:
        print("{}".format(add))
    else:
        for x in range(1, count):
            add += int(argv.__getitem__(x))
        print("{}".format(add))
