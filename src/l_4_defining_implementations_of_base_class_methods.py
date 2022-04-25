import math


class Shape:

    def __init__(self, shape_type, color='Red'):
        self.__shape_type = shape_type
        self.__color = color

    def get_type(self):
        return self.__shape_type

    def get_color(self):
        return self.__color

    def get_area(self):
        pass

    def get_perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        Shape.__init__(self, 'circle')

        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius * self.__radius

    def get_perimeter(self):
        return 2 * math.pi * self.__radius


circle = Circle(10)

print(circle.get_area())
print(circle.get_perimeter())


class Square(Shape):

    def __init__(self, side, color='Red'):
        Shape.__init__(self, 'square', color)

        self.__side = side

    def get_area(self):
        return self.__side * self.__side

    def get_perimeter(self):
        return 4 * self.__side


square = Square(5, color='Yellow')
square1 = Square(10)

print(square.get_area())
print(square.get_perimeter())
print(square.get_color())

print(square1.get_area())
print(square1.get_perimeter())
print(square1.get_color())
