#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (0, None)
    max_n = my_list[0]

    for num in my_list:
        if num > max_n:
            max_num = num
    return max_n
