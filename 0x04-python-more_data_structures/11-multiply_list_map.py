#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    d_my_list = my_list   
    return list(map(lambda x: x * number, d_my_list))
