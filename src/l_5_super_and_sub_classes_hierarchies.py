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


race = Competition('Race', 100)

print(type(race))

print(help(Competition))

print(Competition.__dict__)

print('\n##############################################################\n')


class Sprint(Competition):
    pass


print(help(Sprint))

print(Competition.__dict__)

print('\n###################\n')

print(Sprint.__dict__)

print('\n###################\n')

sprint = Sprint('100m', 700)

print(type(sprint))

sprint.raise_prize()

print(sprint.get_prize())

print('\n####################################################\n')

chess = Competition('Chess', 1000)

print(chess.get_prize())

chess.raise_prize()

print(chess.get_prize())