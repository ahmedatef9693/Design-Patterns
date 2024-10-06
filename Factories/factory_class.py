from math import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"""\n x : {self.x} \n y : {self.y}"""
    
    class FactoryPoint:

        
        def new_cartesian_point(self,x, y):
            return Point(x, y)
        
        def new_polar_point(self,rho, theta):
            return Point(rho* sin(theta), rho* cos(theta))
    
    factory = FactoryPoint()




print(Point.factory.new_cartesian_point(4,7))
print(Point.factory.new_polar_point(1,7))




