class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def breathe(self):
        print("Inhale, exhale!")

    def can_move(self):
        print("Can change location")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Can swim")

    def reproduction(self):
        print("Lays egg.")


azu = Fish()
azu.swim()
azu.can_move()
azu.breathe()
azu.reproduction()
