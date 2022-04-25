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

    def __init__(self):
        Shape.__init__(self, 'circle')


class Square(Shape):

    def __init__(self):
        Shape.__init__(self, 'square')


circle = Circle()

square = Square()

print(type(circle))
print(type(square))

print(circle.get_type())
print(circle.get_color())
print(square.get_type())
print(square.get_color())


class Circle(Shape):

    def __init__(self, color='Green'):
        Shape.__init__(self, 'circle', color)


circle = Circle()

print(circle.get_color())

circle = Circle('Yellow')

print(circle.get_color())


class Square(Shape):

    def __init__(self, color):
        Shape.__init__(self, 'square', color)


square = Square('Orange')

print(square.get_color())

