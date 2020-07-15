class Animals:

    def __init__(self, name):
        self.name = name
        self._hunger = 5

    def breathe(self):
        print("Breathing in... ")
        print("Breathing out... ")
        self._hunger += 0.1


    def eat(self):
        print("nom nom nom")
        self._hunger = 0



class Mammal(Animals):  # Inheritance
    def __init__(self, name, legs, colour):
        super().__init__(name)  # Bring down from inherited class
        self.legs = legs
        self.colour = colour

    def give_birth(self):
        print("I have given birth to a child")

class Dog(Mammal):
    def __init__(self):
        super().__init__(name, legs=4, colour=colour)

    def wag_tail(self):
        print("wagging")
        super().breathe()  # From inheritance class. Just makes it more clear
        self._hunger += 1


class Labrador(Dog):

    def retrieve(self):
        print("I caught this stick")
        self._hunger += 1

my_dog = Dog()
print(my_dog.legs)