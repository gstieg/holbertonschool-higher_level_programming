#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """rectngle base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ args
        width = width
        height = height
        x = 0(input x)
        y = 0(input y)
        id  = None
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            """args:
            value: value of width
            """
            if type(value) != int:
                raise TypeError("{:s} must be an integer")
            if value <= 0:
                raise ValueError("{:s} must be > 0")
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            """ args
            value: value of height
            """
            if type(value) != int:
                raise TypeError("{:s} must be an integer")
            if value <= 0:
                raise ValueError("{:s} must be > 0")
            self.__height = value

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            """args:
            value: value of x
            """
            if type(value) != int:
                raise TypeError("{:s} must be an integer")
            if value < 0:
                raise ValueError("{:s} must be >= 0")
            self.__x

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            """ args
            value = value of y
            """
            if type(value) != int:
                raise TypeError("{:s} must be an integer")
            if value < 0:
                raise ValueError("{:s} msut be >= 0")
            self.__y = value

        def area(self):
            """finds the area of the Rectangle"""
            return self.__width * self.__height
            
        def __str__(self):
            return ("[Rectangle] ({}) {}/{} - {}{}".format(self.id, self.__x,
                                                           self.__y,
                                                           self.__width,
                                                           self.__height))
        def update(self, *args, **kwargs):
            """ assigning arguments"""
            if args != None and len(args):
                for args in args:
                    if args > 0:
                        self.id = arg
                    if args > 1:
                        self.width = arg
                    if args > 2:
                        self.height = arg
                    if args > 3:
                        self.x = arg
                    if args > 4:
                        self.y = arg
            if kwargs != None:
                for key, value in kwargs.items():
                        setattr(self, key, value)

        def to_dictionary(self):
            """ returns a dictiornary"""
            new_dict = {}
            a = {"id": self.id, "width": self.__width, "height": self.__height,
                 "x": self.__x, "y": self.__y}
            return  new_dict
