#pip install -U pytest
import random

class Scrabble:

    def __init__(self):
        self.dict_score = {1:{"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4,
                           "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3,
                           "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8,
                           "Y": 4, "Z": 10}}
        self.tile_bag = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
            "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
            "W", "X", "Y", "Z"]
        self.random_letters = []
        self.word = " "

    def get_word(self):
        word_accept = False
        while not word_accept:
            self.word = input(f"From the letters {self.random_letters}, please give a word \n").upper()
            list_word = list(self.word)
            for i in self.word:
                if list_word == list(filter(lambda  x: x in self.random_letters,list_word)):
                    print(f"Good word! That gives you a score of {self.score_calculator()}!")
                    break
                else:
                    self.word = input("Sorry! You can't use that word. Please use the letters given \n").upper()
            return True



    def letter_score(self, letter):
        for key in self.dict_score:
            return self.dict_score[1][letter]

    def generate_letters(self):
        for i in range(0, 7):
            random_letters_choice = random.choice(self.tile_bag)
            self.random_letters.append(random_letters_choice)
        return len(self.random_letters)


    def score_calculator(self):
        word_score = []
        for i in self.word:
            self.letter_score(i)
            word_score.append(self.letter_score(i))
        calculator = sum(word_score)
        return calculator


    # def word(self):
    #     word = input("Make a word from the letters provided \n").upper()
    #     valid = []
    #     counter = 1
    #     x = list(word)
    #     print(x)
    #     while counter > 0:
    #         for i in x:
    #             if i in self.random_letters:
    #                 word = "".join(word)
    #                 valid.append(counter)
    #                 counter += 1
    #                 #print(f"You guessed {word}. That scores you {self.letter_score(word)}")
    #             elif i not in self.random_letters:
    #                 word = input("try again \n").upper()
    #
    #     return True

new_game = Scrabble()
new_game.generate_letters()
new_game.get_word()

