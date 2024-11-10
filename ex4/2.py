import math

class Shape:
    def __init__(self):
        self.area_value = 0
        self.perimeter_value = 0
    
    def area(self):
        pass
    
    def perimeter(self):
        pass


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height
    
    def area(self):
        self.area_value = 0.5 * self.base * self.height
    
    def perimeter(self):
        self.perimeter_value = self.base + 2 * math.sqrt((0.5 * self.base)**2 + self.height**2)


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        self.area_value = self.length * self.width
    
    def perimeter(self):
        self.perimeter_value = 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def area(self):
        self.area_value = math.pi * self.radius**2
    
    def perimeter(self):
        self.perimeter_value = 2 * math.pi * self.radius


triangle = Triangle(4, 5)
triangle.area()
triangle.perimeter()
print("Triangle Area:", triangle.area_value)
print("Triangle Perimeter:", triangle.perimeter_value)

rectangle = Rectangle(3, 6)
rectangle.area()
rectangle.perimeter()
print("Rectangle Area:", rectangle.area_value)
print("Rectangle Perimeter:", rectangle.perimeter_value)

circle = Circle(2)
circle.area()
circle.perimeter()
print("Circle Area:", circle.area_value)
print("Circle Perimeter:", circle.perimeter_value)