class Father:
    def height(self):
        print('I have inherited my height from my father')


class Mother:
    def intelligence(self):
        print('I have inherited my intelligence from my mother')


class Child(Father, Mother):
    def my_experience(self):
        print('My experience are all my own')


print(help(Child))


# | Method
# resolution
# order:
# | Child
# | Father
# | Mother
# | builtins.object


class Child2(Mother, Father):
    pass


print(help(Child2))
# | Method
# resolution
# order:
# | Child2
# | Mother
# | Father
# | builtins.object

c = Child()

print(c.height())
print(c.intelligence())
print(c.my_experience())


class Employee:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def show_name(self):
        print(self.__name)

    def show_age(self):
        print(self.__age)


class Salary:
    def __init__(self, salary):
        self.__salary = salary

    def show_salary(self):
        print(self.__salary)


class Database(Employee, Salary):

    def __init__(self, name, age, salary):
        Employee.__init__(self, name, age)
        Salary.__init__(self, salary)


empl = Database('Robin', 26, 3000)

print(empl.show_salary())
print(empl.show_age())
print(empl.show_name())