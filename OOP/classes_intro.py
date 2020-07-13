# Class key word followed by name of class
# Camel case

#class GoodDog:

#    animal_type = "canine"  # Attribute (variable but in a class)

#    def bark(self):  # Method (function but in a class)
#        return "Woof!"


#fluffy = GoodDog()  # Created an instance of the class (an object)
#print(fluffy.animal_type)
#print(fluffy.bark())
# Issue with this is that you can change the blueprint of the dog too easily
# So we do this instead...

class Dog:

    def __init__(self, name, breed):  #Intitalisation - initially setting conditions
        self.name = name
        self.legs = 4
        self.animal_kind = "canine"
        self.breed = breed
        self._secret = "I can't eat chocolate"  # Private variable - Underscore 'hides' this from IDE
        self.__big_secret = "I love walks"  # Properly hides it. But can still be accessed by class

    def bark(self):
        return f"Woof! My name is {self.name}"

    def reveal_secret(self):  # Must reveal before use
        return self.__big_secret

    def get_secret(self):  # GETTER
        return self.__big_secret

    def set_secret(self):  # SETTER
        self.__big_secret = secret

big_dog = Dog("Pablo","Pug") # Instantiation - creating an instance of a class
small_dog = Dog("Lucky","Lab")

print(big_dog.bark())
print(small_dog.get_secret())
big_dog.set_secret("I hid my bone")
print(big_dog.get_secret)