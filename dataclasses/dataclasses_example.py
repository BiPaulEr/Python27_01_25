from dataclasses import dataclass, field
import math

@dataclass(order=True)
class Point():
    x : int = field(compare=False)
    y : int = field(compare=False)
    z : int = field(compare=False, default=0)
    length : float = field(init = False)

    def __post_init__(self):
        self.lentgh = math.sqrt(self.x**2 + self.y**2 * self.z**2)

    def __add__(self, point):
        return Point(self.x + point.x , self.y + point.y, self.z + point.z)
    
point1 = Point(4, 9)
point2 = Point(4, 5)
point3 = Point(7, 8)

print(point1 == point2)
print(point1 == point3)
print(point1) #<__main__.Point object at 0x0000023E31097950> -> <Point x=4, y=5>

print(point1 + point3)

print(point1 < point3) #TRue #False