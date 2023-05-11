#!/usr/bin/python3

from sys import argv

if __name__ == '__main__':
    if (len(argv) == 1):
        print("{} argument:".format(len(argv)))
    else:
        print("{} arguments:".format(len(argv)))

for i in range(0, len(argv)):
    print("{}: {}".format(i, argv[1]))
