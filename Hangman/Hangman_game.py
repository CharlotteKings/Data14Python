# class that runs the game side, i.e keeping score
# handle game logic, get guesses off player, keeping score

# List of underscores
# Ask for letter
# Check letter against word
    # go through each letter one by one

# Replace underscore with correct guess
    # return index of letter from brain
    # Iterate through word
    # If right - return index
    # add index to list pf indices to return
    # increase the count - move onto next letter
    #after loop return the list of indices - return index_return
    # for loop through index return to actually replace underscore with letter
# Failed attempts += 1 if wrong

from Hangman_brain import Brain
class Game:


    index = [1, 2, 3, 4]

    def __init__(self):
        self.lives = 10
        self.brain = Brain()
        self.word = self.brain.get_word()
        self.game_board = self.brain.dash()



    def guess_letter(self):
        while self.lives > 0:
            guess = input("Guess a letter!").upper()
            indicies = self.brain.letter_check(guess)
            self.update(guess,indicies)
            if indicies == []:
                self.lives -= 1
                print(f"That letter isn't in the word. {self.lives}left!")
            elif indicies != []:
                print(self.game_board)
        print(f"You lose. The correct word was {self.word}")


    def update(self, guess, indicies):
        for i in indicies:
            self.game_board[i] = guess
        return self.game_board



new_guess = Game()

print(new_guess.word)
print(new_guess.guess_letter())
print(new_guess.update())


