class Grandparent:
    def height(self):
        print('I have inherited my height from my grandparent')


class Parent(Grandparent):
    def intelligence(self):
        print('I have inherited my intelligence from my Parent')


class Child(Parent):
    def experience(self):
        print('My experience are all my own')


print(help(Child))

c = Child()

c.height()
c.intelligence()
c.experience()


class Grandparent(object):
    def __init__(self, city):
        self.__city = city

    def get_city(self):
        return self.__city


class Parent(Grandparent):
    def __init__(self, city, last_name):
        super().__init__(city)

        self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name


p1 = Parent('Kyiv', last_name='Horovyi')
print(p1.get_city())
print(p1.get_last_name())


class Person(Parent):
    def __init__(self, city, last_name, first_name):
        super().__init__(city, last_name)

        self.__first_name = first_name

    def get_first_name(self):
        return self.__first_name


person = Person('Kyiv', 'Horovyi', 'Matvii')
print(person.get_city(), person.get_last_name(), person.get_first_name())

print(help(Person))


class Person1(Parent):
    def __init__(self, city, last_name, first_name):
        Parent.__init__(self, city, last_name)

        self.__first_name = first_name

    def get_first_name(self):
        return self.__first_name

    def get_introduction(self):
        last_name = super().get_last_name()
        city = super().get_city()

        print(f'Hi I am {self.__first_name} {last_name} from {city}')

    def get_information(self):
        last_name = self.get_last_name()
        city = self.get_city()

        print(f'Hi I am {self.__first_name} {last_name} from {city}')


p = Person1('Kyiv', 'Horova', 'Mia')
p.get_introduction()
p.get_information()