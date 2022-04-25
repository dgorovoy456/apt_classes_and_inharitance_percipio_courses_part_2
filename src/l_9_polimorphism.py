class Hominidae():
    def communication(self):
        print('They use auditory calls and visual cues')

    def walk(self):
        print('They are knuckle-walkers, used to hang and swing from one tree to another')


class Human(Hominidae):

    def communication(self):
        print('They use language to communicate')

    def walk(self):
        print('They are bipeds')


class Gorrila(Hominidae):

    def communication(self):
        print('They use twenty-five distinct vocalizations to communicate')

    def walk(self):
        print('They are knuckle-walkers')


hominidae_1 = Hominidae()
human_1 = Human()
gorilla_1 = Gorrila()

hominidae_1.communication()
human_1.communication()
gorilla_1.communication()
