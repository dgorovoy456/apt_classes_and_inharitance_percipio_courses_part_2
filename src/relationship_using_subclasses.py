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
    pass


circle = Circle('circle')

print(type(circle))


class Square(Shape):
    pass


square = Square('square')

print(type(square))
