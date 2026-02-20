class Shapes:

    def area(self,):

        return "The area of the shape"

class Rectangle(Shapes):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.142 * self.radius * self.radius

class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [Rectangle(5, 9), Circle(3), Triangle(8, 9), Shapes()]

for shape in shapes:
    print(shape.area())
