#!/usr/bin/python3

import sys

if (len(sys.argv) == 1):
    print("{} argument:".format(len(sys.argv)))
else:
    print("{} arguments:".format(len(sys.argv)))

for i in range(0, len(sys.argv)):
    print("{}: {}".format(i, sys.argv[1]))
