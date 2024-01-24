#!/usr/bin/python3
import sys


def listme(argv):
    argvs = len(argv)
    if argvs == 0:
        print("0 arguments.")
    elif argvs == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argvs))
    for i in range(1, argvs + 1):
        print("{}: {}".format(1, argv[i - 1]))


if __name__ == "__main__":
    listme(sys.argv[1:])
