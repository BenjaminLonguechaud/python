import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__X = x
        self.__Y = y

    def getx(self):
        return self.__X

    def gety(self):
        return self.__Y

    def distance_from_xy(self, x, y):
        return math.dist([self.__X, self.__Y], [x, y])

    def distance_from_point(self, point):
        return math.dist([self.__X, self.__Y], [point.getx(), point.gety()])

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__point1 = vertice1
        self.__point2 = vertice2
        self.__point3 = vertice3

    def perimeter(self):
        return self.__point1.distance_from_point(self.__point2) + \
        self.__point2.distance_from_point(self.__point3) + \
        self.__point3.distance_from_point(self.__point1)


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())