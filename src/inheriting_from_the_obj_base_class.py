class Shape:
    pass


class Shape():
    pass


class Shape(object):
    pass


class Shape:

    def __init__(self, shape_type):
        self.__shape_type = shape_type

    def get_type(self):
        return self.__shape_type


circle = Shape('circle')

print(type(circle))

square = Shape('square')

print(type(square))


class Shape:
    def __init__(self, shape_type, color='Red'):
        self.__shape_type = shape_type
        self.__color = color

    def get_type(self):
        return self.__shape_type

    def get_color(self):
        return self.__color


circle = Shape('circle')

print(circle.get_color())

square = Shape('square', color='Blue')

print(square.get_color())
