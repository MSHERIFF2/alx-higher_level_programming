#!/usr/bin/python3
import sys
def adders():
    arguments = sys.argv[1:]
    result = sum(int(i) for i in arguments)
    print(result)
if __name__ == "__main__":
    adders()
