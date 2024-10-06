from math import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"""\n x : {self.x} \n y : {self.y}"""

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)
    
    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho* sin(theta), rho* cos(theta))




print(Point.new_polar_point(5,4))




