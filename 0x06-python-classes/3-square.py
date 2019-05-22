#!/usr/bin/python3
class Square:
    """Square Class that defines a square by: (based on 2-square.py"""
    def __init__(self, size=0):
        """Instantiation"""
        if size < 0:
            raise ValueError("size must be >= 0")
        elif size < 0:
            raise TypeError("size must be an integer")
        self.__size = size

    def area(self):
        """Returns current square area"""
        return self.__size ** 2
