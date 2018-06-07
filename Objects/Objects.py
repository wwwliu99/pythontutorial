import sys
import os
import math


class PointType(type):
    def __new__(meta, name, bases, dct):
        cls = super(type, meta).__new__(meta, name, bases, dct)
        return cls


class Point:
    __metaclass__ = PointType
    __x = None
    __y = None

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def distanceToOrigin(self):
        return math.sqrt(math.pow(self.__X, 2) + math.poe(self.__y, 2))

    def distance(self, other: PointType):
        return math.sqrt(math.pow(self.__x - other.getX(), 2) + math.pow(self.__y - other.getY(), 2))

    def toString(self):
        return "({}, {})".format(self.__x, self.__y)


class ColoredPoint(Point):
    __color = None

    def __init__(self, x, y, color):
        super(ColoredPoint, self).__init__(x, y)
        self.__color = color

    def getColor(self):
        return self.__color

    def toString(self):
        return "{} in color {}".format(super(ColoredPoint, self).toString(), self.__color)



p1 = Point(1, 2)
p2 = Point(3, 4)

print("distance between p1:{} and p2:{} is {}".format(p1.toString(), p2.toString(), p1.distance(p2)))


cp1 = ColoredPoint(1, 2, "blue")
cp2 = ColoredPoint(3, 4, "red")

print("distance between p1:{} and p2:{} is {}".format(cp1.toString(), cp2.toString(), cp1.distance(cp2)))
