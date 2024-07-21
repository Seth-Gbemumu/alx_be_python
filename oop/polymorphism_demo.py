from math import pi

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        return area

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = pi * self.radius ** 2
        return area

# Create instances of Rectangle and Circle
# r1 = Rectangle(6, 2)
# print(r1.area())  # Should use the instance's own length and width

# c1 = Circle(6)
# print(c1.area())  # Should use the instance's own radius

