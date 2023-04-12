""" Inheritance & Polymorphism Lab"""


class horse():
    def __init__(self, _breed: str, _coat_color: str):
        self.breed = _breed
        self.coat_color = _coat_color

    def gallop(self):
        print("Slow down..", self.breed, self.coat_color, 'is a beautiful horse.')

    def talk(self):
        print('grunt')


class Ryder(horse):
    def __init__(self, _breed, _coat_color):
        super().__init__(_breed, _coat_color)
        self.breed = _breed
        self.coat_color = _coat_color

    def talk(self):
        print('squeal')


Bob = horse('Quarter horse', 'black')
Bob.gallop()
Bob.talk()






