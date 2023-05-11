#!/usr/bin/python3

from sys import argv

if __name__ == '__main__':
    argcount = len(argv) - 1
    if (argcount == 0):
        print("{} arguments.".format(argcount))
    elif (argcount == 1):
        print("{} argument:".format(argcount))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments".format(argcount))
        i = 1
        for arg in argv[1:]:
            print("{}: {}".format(i, arg))
            i += 1
