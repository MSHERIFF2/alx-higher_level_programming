#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key == "":
        return a_dictionary
    else:
        del a_dectionary[key]
    return a_dictionary
