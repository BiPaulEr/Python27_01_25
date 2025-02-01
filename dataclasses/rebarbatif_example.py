class Point():
    def __init__(self, x, y, z = 0):
        self.x  = x
        self.y  = y
        self.z = z
    
    def __eq__(self, point):
        return point.x == self.x and point.y == self.y and point.z == self.z

    def __repr__(self):
        return f"<Point x={self.x}, y={self.y}, z={self.z}>"
    
    def __add__(self, point):
        return Point(self.x + point.x , self.y + point.y, self.z + point.z)
    
point1 = Point(4, 5)
point2 = Point(4, 5)
point3 = Point(7, 8)

print(point1 == point2)
print(point1 == point3)
print(point1) #<__main__.Point object at 0x0000023E31097950> -> <Point x=4, y=5>

print(point1 + point3)