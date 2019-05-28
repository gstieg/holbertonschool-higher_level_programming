 #!/usr/bin/python3
class Rectangle:
     """Rectangle class"""

     def __init__(self, width=0, height=0):
         """args: widht and height
         width = width of rectanglw
         height = height of Rectangl"""
         @property
         def width(self):
            """property of width"""
            return self.__width

            @width.setter
            def width(self, value):
                 """sets the width"""
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
            def height(self, value):
                """sets height"""

            if type(value) is not int:
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
                self.___height = value

            def area(self):
                """finds the area"""
                return self.__height * self.__width
            def perimeter(self):
                """ gets the perimeter"""
            return 2 * self.__width + 2 * self.__height

            def __str__(self):
                """prints area"""
                r = ""
                if self.width == 0 or self.height == 0:
                    return r
                r = (('#' * self.width + '\n') * self.__height)
                return r
