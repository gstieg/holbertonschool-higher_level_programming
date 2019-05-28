#!/usr/bin/python3
class Rectangle:
    """class for the rectangle"""
    def __init__(self, width=0, height=0):
        """ args: width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """property for the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """property for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """property for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
