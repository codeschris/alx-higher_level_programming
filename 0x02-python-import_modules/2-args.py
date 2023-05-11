#!/usr/bin/python3

from sys import argv

if __name__ == '__main__':
    n = len(argv) - 1
    print("{} argument{}{}"
            .format(n, "" if n == 1 else "s", "." if n == 0 else ":"))
    for i in range(n):
        print("{}: {}".format(i + 1, argv[i + 1]))
