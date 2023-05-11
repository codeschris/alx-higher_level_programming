#!/usr/bin/python3

from sys import argv

if __name__ == '__main__':
    result = 0
    i = 0
    for arg in argv:
        if i != 0:
            result += int(arg)
        else:
            i += 1
    print("{:d}".format(result))
