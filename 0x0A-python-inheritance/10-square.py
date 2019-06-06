#!/usr/bin/python3
""" class Rectangle that inherits from BaseGeometry"""

class Square(Rectangle):
    """ square class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
