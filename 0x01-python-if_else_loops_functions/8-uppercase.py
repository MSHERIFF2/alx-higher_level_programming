#!/usr/bin/python3
def uppercase(s):
    for char in s:
        # Convert lowercase letters to uppercase using ASCII values
        if 'a' <= char <= 'z':
            print(chr(ord(char) - ord('a') + ord('A')), end='')
        else:
            print(char, end='')

    # Add a new line at the end
    print()
