#!/usr/bin/python3
# 2-square by Sheriffdeen
""" Define a Square """


class Square:
    """square attribute with size protected """
    def __init__(self, size=0):
        """the initialization function for the square class
        checks for input errors for size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
