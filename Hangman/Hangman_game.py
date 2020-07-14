from Hangman_brain import Brain
class Game:

    def __init__(self):
        self.lives = 10
        self.brain = Brain()
        self.word = self.brain.get_word()
        self.game_board = self.brain.dash()


    def guess_letter(self):
        while self.lives > 0:
            guess = input("Guess a letter! \n").upper()
            indicies = self.brain.letter_check(guess)
            self.update(guess, indicies)
            if indicies == []:
                if not guess.isalpha():
                    print("That's not a letter!")
                else:
                    self.lives -= 1
                    print(f"That letter isn't in the word. {self.lives} lives left!")
            elif indicies != []:
                print(self.game_board)
            if "_" not in self.game_board:
                print("YOU WIN!!!")
                break
            elif self.lives == 0:
                print(f"You lose. The correct word was {self.word}")
                break


    def update(self, guess, indicies):
        for i in indicies:
            self.game_board[i] = guess
        return self.game_board


new_guess = Game()

print(new_guess.word)
print(new_guess.guess_letter())



