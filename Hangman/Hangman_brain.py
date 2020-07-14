# class that handles the 'brain' of hangman
# knows the word to guess
# returns how many letters the word is
# methods to return information about the word

from hangman_words import word_list
from random import choice

class Brain:

    def __init__(self):
        self._random_word = choice(word_list)
        self.length = len(self._random_word)
        self.failed = 0
        self.attempts_left = 10
        self.guess = " "


    def dash(self):
        word_length_dashes = ['_'] * self.length
       # print(f'Your word is {word_length_dashes} = {self.length} characters long')
        return word_length_dashes

    def get_word(self):
        return self._random_word

    # def guess_check(self):
    #     guess = imput("guess please")
    #     while not guess.isalpha():
    #         val = input("Please type a valid letter? \n")
    #     if guess.isalpha:
    #         return guess


    def letter_check(self,guess):
        indicies = []
        counter = 0
        for letter in self.get_word():
            if letter == guess:
                indicies.append(counter)  #  Notes index of correct letter
            counter += 1  # Checks next index in word
        return indicies




new_word = Brain()
# print(type(new_word.dash()))

# print(new_word.get_word())
# print(new_word.letter_check())



# third file to loads them in and read them