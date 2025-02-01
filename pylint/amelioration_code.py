"""
    Apprendre Pylint
"""
import math

def calculate_circle_area(radius):
    """
    calculate area from radius for a cricle
    """
    if radius < 0:
        return None
    return math.pi * radius * radius

class ShapeCalculator:
    """
    rectangle class
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calc_area(self):
        """
        calcule aire
        """
        return self.length * self.width
    def calc_perimeter(self):
        """
        calcule perimetre
        """
        return 2 * (self.length + self.width)

def function(shape : ShapeCalculator):
    """
    Display ShapeCalculator to the console
    """
    print(f"Area: {shape.calc_area()}")
    print(f"Perimeter: {shape.calc_perimeter()}")

def main():
    """
    main function to test
    """
    circle_area = calculate_circle_area(5)
    print(f"Circle Area: {circle_area}")
    rectangle = ShapeCalculator(10, 20)
    print(f"Rectangle Area: {rectangle.calc_area()}")
    print(f"Rectangle Perimeter: {rectangle.calc_perimeter()}")
    function(rectangle)

if __name__ == "__main__":
    main()
