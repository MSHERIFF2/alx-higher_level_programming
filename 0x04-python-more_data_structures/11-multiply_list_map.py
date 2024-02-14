#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    
    gen =list(map(lambda x : x * number for x in my_list, my_list))

    return gen

