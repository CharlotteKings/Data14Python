class Cat:

    def __init__(self):
        self._mood = 5
        self._hunger = 4
        self._energy = 7

    def _meow(self):
        print("meow")


    def sleep(self):
        self.energy = 10
        if self._hunger > 5:
            self._hunger = 10
        else:
            self._hunger += 3

    def play(self):
        self._meow()
        if self._mood > 8:
            self._mood = 10
        else:
            self._mood += 2
        if self.energy < 3:
            self._energy = 0
        else:
            self._energy -= 2


    def feed(self):
        self._meow()
        self._hunger = 0

    def get_stats(self):
        print(f"Mood = {self._mood} Hunger = {self._hunger} Energy = {self._energy}")



new_cat = Cat()
new_cat.feed()
print(new_cat.get_stats())