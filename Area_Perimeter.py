#!/usr/bin/python3
""" Area and Perimeter.

"""
from math import pi


class Area_Perimeter:
    """ This class calculates the area and perimeter of the
    following geometric figures: circle, square, and rectangle.

    """
    def __init__(self):
        """ This constructor method initialize the area
        and the perimeter in zero.

        """
        self.__area = 0
        self.__perimeter = 0

    def circle(self, r):
        """ This method calculates the area and the
        perimeter of the circle.

        """
        self.__area = pi * r**2
        self.__perimeter = 2 * pi * r
        return "The area: {} and the perimeter: {} of a circle".format(
            self.__area, self.__perimeter)

    def square(self, s):
        """ This method calculates the area and the
        perimeter of the square.

        """
        self.__area = s**2
        self.__perimeter = s * 4
        return "The area: {} and the perimeter: {} of a square".format(
            self.__area, self.__perimeter)

    def rectangle(self, h, w):
        """ This method calculates the area and the
        perimeter of the rectangle.

        """
        self.__area = h * w
        self.__perimeter = 2 * h + 2 * w
        return "The area: {} and the perimeter: {} of a rectangle".format(
            self.__area, self.__perimeter)


figure = Area_Perimeter()
print(figure.circle(3))
print(figure.square(4))
print(figure.rectangle(4, 2))
