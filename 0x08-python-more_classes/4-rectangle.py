#!/usr/bin/python3
class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """args: widht and height
        width = width of rectanglw
        height = height of Rectangl"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets height of rectangle"""
        return self.__height

    @height.setter
    def height(self,value):
        """sets height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.___height = value

    def area(self):
        """finds the area"""
        return self.__width * self.__height

    def perimeter(self):
        """ gets the perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return empty
        empty = ""
        empty = (('#' * self.__width + '\n') * self.__height)
        empty = empty [:-1]
        return empty
    def __repr__(self):
        """return a string representation of the rectangle to be able to recreate a new instance """
        return "Rectangle({}, {})".format(self.__width, self.__height)
