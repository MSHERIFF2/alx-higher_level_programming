#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            print("{}".format(chr(ord(char) - ord('a') + ord('A'))), end='')
    print()
