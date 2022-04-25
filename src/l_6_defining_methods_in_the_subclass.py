class Competition:
    __raise_amount = 1.10

    def __init__(self, name, prize):
        self.__name = name
        self.__prize = prize

    def get_name(self):
        return self.__name

    def get_prize(self):
        return self.__prize

    def raise_prize(self):
        self.__prize = self.get_prize() * self.__raise_amount


class Cycling(Competition):

    def __init__(self, name, prize, country):
        super().__init__(name, prize)

        self.__country = country

    def get_country(self):
        return self.__country


cycling = Cycling('10km', 7500, 'USA')

print(cycling.get_country())
print(cycling.get_name())
print(cycling.get_prize())

print(issubclass(Cycling, Competition))


class Shooting():

    def __init__(self, name):
        self.first = name


print(issubclass(Shooting, Competition))


class Shooting(Competition):

    def __init__(self, name, prize):
        super().__init__(name, prize)


print(issubclass(Shooting, Competition))

shooting = Shooting('Rifle', 10000)

print(shooting.get_prize())
print(shooting.get_name())
