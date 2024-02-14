#!/usr/bin/python3

def number_keys(a_dictionary):
    counter = 0
    for k, v in a_dictionary.items():
        counter = counter + 1
    return counter
