import random as rn # Import whole random package as alias

# print(random.randint(1,100))  # Random integer between 2 given numbers

# print(random.random)  # Print random number between 0 and 1

# from random import randint  #  Import specific thing from random - no longer have to specify random.randint

from car_class import *  # Import all from car class file

#from hangman_words import word_list
#from random import choice

#print(choice(word_list))

# class that handles the 'brain' of hangman
    # knows the word to guess
    # methods to return information about the word

# class that runs the game side, i.e keeping score
    # handle game logic, get guesses off player, keeping score

# third file to loads them in and read them
word = "game"
word.find("a")