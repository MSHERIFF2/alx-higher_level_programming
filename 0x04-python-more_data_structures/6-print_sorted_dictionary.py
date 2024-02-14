#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorts = sorted(a_dictionary)
    for k in sorts:
        print("{}: {}".format(k, a_dictionary[k]))
