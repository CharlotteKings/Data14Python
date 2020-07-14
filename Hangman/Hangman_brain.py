from hangman_words import word_list
from random import choice

class Brain:

    def __init__(self):
        self._random_word = choice(word_list)
        self.length = len(self._random_word)
        self.failed = 0
        self.attempts_left = 10
        self.guess = " "


    def dash(self):  # Initial game board
        word_length_dashes = ['_'] * self.length
       # print(f'Your word is {word_length_dashes} = {self.length} characters long')
        return word_length_dashes


    def get_word(self):
        return self._random_word


    def letter_check(self,guess):
        indicies = []
        counter = 0
        for letter in self.get_word():
            if letter == guess:
                indicies.append(counter)  #  Notes index of correct letter
            counter += 1  # Checks next index in word
        return indicies


    def play_again(self):
        play_again = input("Would you like to play again? Y(Yes) or N(No) \n")
        while play_again != "Y" or play_again != "N":
            play_again = input("Please put Y or N \n").upper()
            if play_again == "Y":
                print("Ffi")
            elif play_again == "N":
                quit(Game)

#
# new_game = Brain()
# new_game.play_again()